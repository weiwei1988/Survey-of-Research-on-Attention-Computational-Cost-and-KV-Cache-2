# デザインプラン

## 主題
Attention の O(n^2) 問題と KV キャッシュ問題に関するサーベイ。
主題世界のマテリアル: ローフラインモデル、HBM/SRAM のメモリ階層、FLOPs、
バイト単位のキャッシュサイズ、arXiv ID、二次曲線と線形曲線の対比。

## Color (6 tokens)
- ink        #12161C  (青緑寄りのニアブラック)
- paper      #F6F7F4  (ごくわずかに冷たいオフホワイト)
- quad "hot" #B8431F  (二次コスト・メモリ壁を表す錆びた赤橙)
- lin  "acc" #0D6E76  (線形/効率を表す深いティール)
- muted      #6A737E  (青寄りのグレー)
- rule       hairline / graph-paper 罫

dark: paper #0D1114 / ink #E3E8EA / hot #EE7B4E / acc #45BFC6

配色は装飾ではなく意味論: 暖色 = 二次コスト、寒色 = 線形化された解。

## Type
- 本文: IBM Plex Serif (長文可読性・技術レポートの系譜)
- 見出し/UI: IBM Plex Sans Condensed (高密度・工学文書的)
- データ/ラベル/式: IBM Plex Mono

## Layout
- レビュー論文: 単一カラム 68ch + 左に節番号と年代を刻むレール。
  図版はフルブリード。広い画面では sticky TOC。
- 関係マップ: アプリ型フルハイト。x 軸 = 年 (2018-2026)、
  y 軸 = 研究系統のスイムレーン、辺 = 系譜。左にフィルタ、右に詳細パネル。
  ノードの位置そのものが情報を担う。
