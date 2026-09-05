# Attention O(n²) 問題と KV キャッシュ問題 — 研究系譜の調査

2018–2026 年にわたる「Attention の二次計算量」と「KV キャッシュ」をめぐる研究の積み上げを、
体系的に整理したレビュー論文と、論文間の系譜を辿れるインタラクティブな関係マップ。

調査基準日: **2026-09-04**

---

## 成果物

| ファイル | 内容 | 公開 URL |
|---|---|---|
| `review.html` | レビュー論文（全 10 章・195 論文） | https://claude.ai/code/artifact/9521444f-0400-4596-b94e-73fccbbdfb86 |
| `map.html` | インタラクティブ関係マップ（195 ノード / 214 系譜辺 / 11 レーン） | https://claude.ai/code/artifact/4cc0aa5e-4b03-474f-ab38-9381c9f45267 |

どちらも依存パッケージのない単一 HTML ファイルで、ブラウザで直接開けば動く。
外部から読み込むのは Google Fonts（IBM Plex / Noto Sans JP）のみ。

```bash
open review.html
open map.html
```

---

## ファイル構成

```
Attention_KVcash_SearchMap/
├── README.md
├── AGENTS.md              引き継ぎ規約（データモデル・不変条件・守るべきこと）
├── review.html            レビュー論文本体            ← 正本
├── map.html               関係マップ（論文データを内包） ← 正本
├── PAPERS.md              収録論文一覧（レーン別）      ← 生成物
├── data/
│   ├── papers.json        構造化データ（引き継ぎ用の正本形式） ← 生成物
│   └── papers.csv         表計算・grep 用のフラット表        ← 生成物
├── tools/
│   └── export_papers.py   map.html から上記 3 つを生成 + 整合性検査
└── notes/
    ├── DESIGN.md          配色・書体・レイアウトの設計方針
    ├── NOTES.md           レーン設計と論証の骨格（統合メモ）
    └── sec2_problem.md    第 2 章の初期草稿
```

**`map.html` が論文データの唯一の情報源**で、`PAPERS.md` と `data/` はそこから生成する。
`map.html` を編集したら再生成すること（整合性検査を兼ねており、id 重複・存在しない親 id・
`META` の欠落があれば終了コード 1 で落ちる）。

```bash
python3 tools/export_papers.py
```

---

## レビュー論文の構成

中心にあるのは、**この分野の論争の多くは意見の対立ではなく問題定義のすれ違いだった**という主張である。
「Attention が重い」という一文が四つの別々の主張を含んでいたため、各手法は次の 4 軸で分類して読む。

| 軸 | 問い | 達成する代表例 | 達成しない代表例 |
|---|---|---|---|
| **A. FLOPs** | 漸近計算量を下げたか | Linformer, Performer, Mamba | FlashAttention |
| **B. 実体化** | n×n をメモリに置かずに済むか | FlashAttention, Ring Attention | 素朴な Linformer 実装 |
| **C. 状態サイズ** | KV／再帰状態を劣線形にしたか | MLA, Mamba, StreamingLLM | FlashAttention, GQA |
| **D. 厳密性** | 出力が数学的に厳密か | FlashAttention, Ring Attention | ほぼ全ての近似手法 |

章立て:

1. **すれ違いの構造** — 4 軸の導入
2. **問題の定式化** — prefill / decode の非対称性、KV サイズ式、デコードのローフライン
3. **第一波：近似の時代**（2018–2022） — 疎化・線形・再帰の 5 系統と、全滅した 6 つの理由
4. **転回：FlashAttention** — FLOPs を下げずに IO 下界を達成し、近似の前提を消した
5. **戦場の移動：KV キャッシュ** — サイズ式の各項に対応する 6 系統
6. **第二波：定数状態への再挑戦** — SSM / 線形 RNN、SSD 双対性、二つの独立した壁
7. **収束点：ハイブリッドという妥協**（2024–2026） — ハイブリッドを「二つのスロット」として解剖し、
   両スロットの部品の入れ替わり（SWA→Mamba→Gated DeltaNet→KDA / フル MHA→GQA→MLA→学習可能疎性）、
   比率の下限、深さ方向の情報流を補償する機構（Attention Residuals / Gated Residual）を扱う
8. **評価の危機** — NIAH では見えない劣化、SCBench、Retrieval Head
9. **未解決問題**
10. **出典と検証状況**

---

## 関係マップの読み方と拡張

- **軸ラベルはズーム対象の外（chrome 層）に固定サイズで描く**。拡大率に関係なく常に同じ大きさで
  読めるので、最大ズームアウトでも横軸の年と縦軸のレーン名が判読できる。レーン名は帯が画面上端を
  またぐ間は見出し直下に貼り付き、年は左へ流れ切っても現在地の年だけ左端に残る
- **最もズームアウトした状態は画面形状に追従する**。年あたりの横幅 `XS` を自由変数として、
  描画全体の縦横比がペインの縦横比に一致するよう反復調整してからレイアウトを確定するため、
  レターボックスが出ない。ペイン形状が 8% を超えて変わると再フローする。
  軸フレームぶんの余白（左 `GUT` / 上 `HEADER_PX` / 下 `HINT_PX`）は画面 px で決め、
  縮尺が決まってから世界座標へ逆算している（縮尺と余白が相互依存するため数回反復する）
- **横軸** = 発表年（2018–2026）、**縦のレーン** = 研究系統（11 本）
- **色** = 研究の *立場*（近似 / 定数状態 / 厳密 / KV 圧縮 / システム / 実運用モデル / 理論・評価）
- ノードをクリックすると詳細パネルが開き、論文名・著者・**要約（150 字程度）**・中核機構・
  限界が表示され、祖先と子孫が全てハイライトされる
- 「系譜モード」は選択した論文に連なるノードだけを残す
- 操作: ドラッグで移動、ホイール／ダブルクリックで拡大、`+` `-` `0` キー

### ノードを追加する

`map.html` 内の `const D=[...]` に 1 行足すだけでよい。レイアウト（年による配置、
レーン内の行詰め、辺の描画）は読み込み時に自動計算される。

```js
// D: [id, 表示名, 'YYYY-MM', レーン, 会議/出典, arXiv ID, 概要, 限界・含意, [親ノードの id]]
['kimilinear','Kimi Linear (KDA)','2025-10','ssm','arXiv (Moonshot)','2510.26692',
 'Gated DeltaNet のスカラー減衰をチャネル毎の対角ゲートへ細粒度化',
 '3:1 KDA:MLA。KV −75% / decode 6×',['gateddelta']],
```

さらに、同じ id で 2 つの表に足す。どちらも詳細パネルに表示される。

```js
// META: id: [論文名（原題）, 著者]
kimilinear:['Kimi Linear: An Expressive, Efficient Attention Architecture','Moonshot AI (Kimi Team)'],

// SUM: id: 要約（アブストラクトと本文に基づく 150 字程度）
kimilinear:'Gated DeltaNet の大域的な忘却ゲートを、単一のスカラーからチャネルごとの…',
```

- `id` は小文字英数字のみ。重複不可。`D`・`META`・`SUM` の三つすべてに同じ id で入れる
- 年月は **`'YYYY-MM'` の文字列**。数値にしないこと（`2025.10` は float だと `2025.1` に潰れて
  10 月が 1 月に化け、`.11` が `.5` より小さくなって年内の順序も壊れる）
- レーン id: `sparse` `linear` `recur` `ssm` `exact` `dist` `kvarch` `kvpost` `sys` `hybrid` `eval`
- **確認できない論文名・著者は空文字にする**（このマップは捏造しない方針で作られている）。
  技術報告しかないものは著者欄に組織名を入れてある
- 親 id が存在しないと辺が描かれず静かに落ちるので、追加後は下記で検証する

検証は `tools/export_papers.py` が兼ねるが、単体で確認したい場合:

```bash
python3 -c "
import re
s=open('map.html').read()
ids=re.findall(r\"^\['([a-z0-9]+)',\", s, re.M)
print('nodes:', len(ids))
print('dupes:', [i for i in set(ids) if ids.count(i)>1])
bad=[]
for m in re.finditer(r\"^\['([a-z0-9]+)'.*?\[([^\]]*)\]\],?\$\", s, re.M):
    for x in re.findall(r\"'([a-z0-9]+)'\", m.group(2)):
        if x not in ids: bad.append((m.group(1), x))
print('missing parents:', bad)
mk=set(re.findall(r'^([a-z0-9]+):\[', s, re.M))
print('META なし:', [i for i in ids if i not in mk])
print('余分な META:', [k for k in mk if k not in ids])"
```

---

## 公開版を更新する場合の注意

公開済みアーティファクトは**ファイルパスで同一性が判定される**。
この README のあるディレクトリへ移動したことで、**元の公開時とはパスが変わっている**。
そのため、単に publish すると同じ URL を更新せず**別のアーティファクトが新規作成される**。

既存の URL を維持して更新するには、Artifact ツールに `url` を明示的に渡す。
また、公開前にその URL を `read` して現在の内容を取得し、その上に変更を重ねること
（読んでいないアーティファクトへの publish は拒否される）。

```
1. Artifact action="read"  url=<対象の URL>     ← 現在の公開内容を取得
2. ローカルで編集
3. Artifact file_path=<新しいパス>  url=<対象の URL>   ← 同じ URL を更新
```

---

## 検証状況

構造的な主張（4 軸の区別、prefill/decode の非対称性、FlashAttention が FLOPs を下げていないこと、
SSD 双対性、状態サイズと想起容量のトレードオフ、評価の危機）は複数の独立した一次情報で裏付けている。

一方、**個別の数値と最新世代の帰属は精度が落ちる**。一次情報に到達できなかった項目は
本文中に `要確認` を付し（現在 10 箇所）、第 10 章に全て列挙している。主なものは:

- **Qwen3.8-Max（2026-08）には専用の技術報告がない** — アーキテクチャの根拠は公開 `config.json` と GitHub README のみ。
  なお「フル Attention が 1 層だけ」という理解は誤りで、`full_attention_interval: 4` すなわち 92 層中 23 層（初版の記述を第 7.4 節で訂正済み）
- DeepSeek V4 の CSA / HCA の機構定義（定量値のみ確認）。R2 は未公開
- IBM Granite 4.0、Llama 4 iRoPE、Qwen3.5 以降 — 一次技術報告を特定できず二次情報に依拠
- Kimi K3 の層数内訳 69:24（KDA の漸化式自体は一次確認済み）
- ByteDance Doubao / Seed 2.0 のアーキテクチャは情報空白

第 7 章の後半（2025–2026 年に出荷された各社アーキテクチャ）は特に変動が速く、複数のラボが 1 年内に 2〜4 回の版更新を行っている。
版番号と帰属は調査基準日時点のものとして扱うこと。

---

## 調査方法

4 系統を並行して文献調査し（第一波の近似 Attention / IO 認識型厳密 Attention /
KV キャッシュ最適化 / SSM・線形再帰・ハイブリッド）、その後 2026 年の各社アーキテクチャについて
追加調査を 2 本行って統合した。2 本目は Qwen3.8-Max と、フル Attention 層の下限に関する
アブレーション研究を対象とし、初版の誤りの訂正に用いた。arXiv ID と会議名は可能な限り arxiv.org の
abstract ページまたは公式プロシーディングスに対して照合している。
