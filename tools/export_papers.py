#!/usr/bin/env python3
"""map.html を唯一の情報源として、論文一覧を機械可読な形式へ書き出す。

出力:
  data/papers.json  すべてのフィールドを持つ構造化データ（引き継ぎ用の正本）
  data/papers.csv   表計算・grep 用のフラット表
  PAPERS.md         人が読む一覧（レーン別・年代順）

map.html を編集したら必ず本スクリプトを再実行すること。逆方向（この出力を
編集して map.html へ戻す）は想定していない。map.html が上流である。

    python3 tools/export_papers.py
"""
from __future__ import annotations

import csv
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
MAP = ROOT / "map.html"

# レーン id -> (表示名, 立場カテゴリ)。map.html の LANES と一致させること。
LANES = {
    "sparse": ("疎化 Attention", "approx"),
    "linear": ("線形・低ランク", "approx"),
    "recur": ("再帰・外部メモリ", "state"),
    "ssm": ("SSM・線形RNN", "state"),
    "exact": ("厳密カーネル", "exact"),
    "dist": ("分散・文脈並列", "exact"),
    "kvarch": ("KV アーキテクチャ", "kv"),
    "kvpost": ("KV 事後圧縮", "kv"),
    "sys": ("サービングシステム", "sys"),
    "hybrid": ("実運用モデル", "model"),
    "eval": ("理論・評価・批判", "theory"),
}
CATEGORIES = {
    "approx": "近似",
    "state": "定数状態",
    "exact": "厳密",
    "kv": "KV 圧縮",
    "sys": "システム",
    "model": "実運用モデル",
    "theory": "理論・評価",
}


class JsLiteral:
    """map.html に埋め込まれた JS 配列リテラルだけを読む最小のパーサ。

    対応するのは配列・単一引用符文字列・数値のみ。json.loads で読めないのは
    キーが引用符なしで文字列が単一引用符だからで、引用符の単純置換は本文中の
    アポストロフィや二重引用符で壊れるため、字句解析している。
    """

    def __init__(self, src: str, i: int = 0):
        self.s = src
        self.i = i

    def _ws(self) -> None:
        while True:
            while self.i < len(self.s) and self.s[self.i] in " \t\r\n":
                self.i += 1
            if self.s.startswith("//", self.i):
                nl = self.s.find("\n", self.i)
                self.i = len(self.s) if nl < 0 else nl + 1
                continue
            return

    def value(self):
        self._ws()
        c = self.s[self.i]
        if c == "[":
            return self.array()
        if c == "'":
            return self.string()
        return self.number()

    def array(self) -> list:
        assert self.s[self.i] == "["
        self.i += 1
        out: list = []
        while True:
            self._ws()
            if self.s[self.i] == "]":
                self.i += 1
                return out
            out.append(self.value())
            self._ws()
            if self.s[self.i] == ",":
                self.i += 1

    def string(self) -> str:
        assert self.s[self.i] == "'"
        self.i += 1
        buf = []
        while self.s[self.i] != "'":
            if self.s[self.i] == "\\":
                self.i += 1
            buf.append(self.s[self.i])
            self.i += 1
        self.i += 1
        return "".join(buf)

    def number(self) -> float:
        j = self.i
        while self.i < len(self.s) and self.s[self.i] not in ",]}":
            self.i += 1
        return float(self.s[j : self.i].strip())


def parse_nodes(src: str) -> list[list]:
    start = src.index("const D=[")
    return JsLiteral(src, src.index("[", start)).array()


def parse_meta(src: str) -> dict[str, list]:
    meta: dict[str, list] = {}
    for m in re.finditer(r"^([A-Za-z0-9_]+):\[", src, re.M):
        meta[m.group(1)] = JsLiteral(src, m.end() - 1).array()
    return meta


def parse_summaries(src: str) -> dict[str, str]:
    """SUM = {id: '要約'} を読む。値は単一引用符の文字列のみ。"""
    out: dict[str, str] = {}
    for m in re.finditer(r"^([A-Za-z0-9_]+):'", src, re.M):
        out[m.group(1)] = JsLiteral(src, m.end() - 1).string()
    return out


def split_year(ym) -> tuple[int, int | None]:
    """年月は 'YYYY-MM' 文字列。

    以前は 2025.10 のような小数で持っていたが、float にすると 2025.1 に潰れて
    10 月が 1 月に化け、さらに .11 が .5 より小さくなって年内の順序も壊れていた。
    """
    text = str(ym)
    if "-" in text:
        y, _, m = text.partition("-")
        return int(y), int(m)
    return int(float(text)), None


def classify_source(venue: str, arxiv: str) -> tuple[str, str | None]:
    """(種別, 一次ソース URL)。URL が確定できない場合は None を返す（捏造しない）。"""
    if arxiv:
        return "arxiv", f"https://arxiv.org/abs/{arxiv}"
    v = venue or ""
    if "GitHub" in v:
        return "github", None
    if "ブログ" in v or "blog" in v.lower():
        return "blog", None
    if "config.json" in v or "モデルカード" in v:
        return "model_card", None
    if any(k in v for k in ("OSDI", "SOSP", "ISCA", "MLSys", "ICML", "NeurIPS", "ICLR", "ACL", "EMNLP", "AAAI", "NAACL", "TACL", "CSUR")):
        return "proceedings", None
    if "発表" in v or "技術報告" in v:
        return "tech_report", None
    return "other", None


def build(nodes: list[list], meta: dict[str, list], sums: dict[str, str]) -> list[dict]:
    rows = []
    for n in nodes:
        nid, name, year, lane, venue, arxiv, summary, limitation, parents = n
        lane_label, category = LANES.get(lane, (lane, "?"))
        title, authors = (meta.get(nid) or ["", ""])[:2]
        src_type, url = classify_source(venue, arxiv)
        y, mo = split_year(year)
        rows.append(
            {
                "id": nid,
                "display_name": name,
                "title": title or None,
                "authors": authors or None,
                "year": y,
                "month": mo,
                "lane": lane,
                "lane_label": lane_label,
                "category": category,
                "category_label": CATEGORIES.get(category, category),
                "venue": venue or None,
                "arxiv_id": arxiv or None,
                "primary_source_url": url,
                "source_type": src_type,
                "needs_verification": ("要確認" in (venue or "")) or ("技術報告なし" in (venue or "")),
                "summary_ja": sums.get(nid) or None,
                "mechanism_ja": summary,
                "limitation_ja": limitation,
                "parents": parents,
            }
        )
    rows.sort(key=lambda r: (r["year"], r["month"] or 0, r["id"]))
    return rows


def write_json(rows: list[dict], path: pathlib.Path) -> None:
    payload = {
        "schema_version": 1,
        "source_of_truth": "map.html",
        "regenerate_with": "python3 tools/export_papers.py",
        "as_of": "2026-09-04",
        "count": len(rows),
        "field_notes": {
            "title": "論文の原題。確認できなかったものは null",
            "summary_ja": "アブストラクトと本文に基づく 150 字程度の日本語要約",
            "mechanism_ja": "中核機構を一行で述べたもの（要約より短い）",
            "authors": "著者。技術報告しかないものは組織名。確認できなかったものは null",
            "primary_source_url": "arXiv ID がある場合のみ確定。それ以外は null（URL を推測しない）",
            "needs_verification": "本文で 要確認 を付けた項目に対応",
            "parents": "直接の源流ノードの id。系譜の辺はここから生成される",
        },
        "papers": rows,
    }
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_csv(rows: list[dict], path: pathlib.Path) -> None:
    cols = [
        "id", "display_name", "title", "authors", "year", "month",
        "lane", "lane_label", "category_label", "venue", "arxiv_id",
        "primary_source_url", "source_type", "needs_verification",
        "summary_ja", "mechanism_ja", "limitation_ja", "parents",
    ]
    with path.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow({**r, "parents": " ".join(r["parents"])})


def write_markdown(rows: list[dict], path: pathlib.Path) -> None:
    total = len(rows)
    with_url = sum(1 for r in rows if r["primary_source_url"])
    with_title = sum(1 for r in rows if r["title"])
    out = [
        "# 収録論文一覧",
        "",
        f"`map.html` にプロットした全 {total} 件。`tools/export_papers.py` が生成する。**直接編集しない。**",
        "",
        f"- 原題を特定できたもの: {with_title} / {total}",
        f"- 一次ソース URL が確定するもの（arXiv）: {with_url} / {total}",
        f"- 残りはブログ・GitHub・モデルカード・組織発表で、**URL を推測せず空欄にしてある**",
        "",
        "調査基準日: 2026-09-04",
        "",
    ]
    for lane, (label, cat) in LANES.items():
        group = [r for r in rows if r["lane"] == lane]
        if not group:
            continue
        out += [f"## {label} — {CATEGORIES.get(cat, cat)}（{len(group)} 件）", ""]
        out += ["| 年月 | 名称 | 論文名（原題） | 著者 | 一次ソース |", "|---|---|---|---|---|"]
        for r in group:
            date = f"{r['year']}.{r['month']:02d}" if r["month"] else str(r["year"])
            title = r["title"] or "—"
            authors = r["authors"] or "—"
            if r["primary_source_url"]:
                src = f"[arXiv:{r['arxiv_id']}]({r['primary_source_url']})"
            else:
                src = (r["venue"] or "—")
            flag = " ⚠" if r["needs_verification"] else ""
            out.append(f"| {date} | **{r['display_name']}**{flag} | {title} | {authors} | {src} |")
        out.append("")
    out += [
        "---",
        "",
        "⚠ は一次情報に到達できず、二次情報または組織発表に依拠している項目。",
        "レビュー論文の第 10 章「出典と検証状況」に理由を列挙している。",
        "",
    ]
    path.write_text("\n".join(out), encoding="utf-8")


def main() -> int:
    src = MAP.read_text(encoding="utf-8")
    nodes = parse_nodes(src)
    meta = parse_meta(src)
    sums = parse_summaries(src)

    ids = [n[0] for n in nodes]
    problems = []
    if len(ids) != len(set(ids)):
        problems.append("id が重複している")
    missing_parent = [(n[0], p) for n in nodes for p in n[8] if p not in set(ids)]
    if missing_parent:
        problems.append(f"存在しない親 id: {missing_parent}")
    missing_meta = [i for i in ids if i not in meta]
    if missing_meta:
        problems.append(f"META なし: {missing_meta}")
    stray_meta = [k for k in meta if k not in set(ids)]
    if stray_meta:
        problems.append(f"余分な META: {stray_meta}")
    missing_sum = [i for i in ids if i not in sums]
    if missing_sum:
        problems.append(f"SUM（要約）なし: {missing_sum}")
    if problems:
        print("map.html に不整合があります:", *problems, sep="\n  - ", file=sys.stderr)
        return 1

    rows = build(nodes, meta, sums)
    (ROOT / "data").mkdir(exist_ok=True)
    write_json(rows, ROOT / "data" / "papers.json")
    write_csv(rows, ROOT / "data" / "papers.csv")
    write_markdown(rows, ROOT / "PAPERS.md")

    with_url = sum(1 for r in rows if r["primary_source_url"])
    print(f"{len(rows)} 件を書き出しました "
          f"(原題 {sum(1 for r in rows if r['title'])} / 要約 {sum(1 for r in rows if r['summary_ja'])} / arXiv URL {with_url} / "
          f"要確認 {sum(1 for r in rows if r['needs_verification'])})")
    print("  data/papers.json  data/papers.csv  PAPERS.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
