# 統合メモ

## レーン設計（可視化の y 軸）
L1 sparse    固定・学習スパース
L2 linear    低ランク/カーネル/線形
L3 recur     再帰・外部メモリ → SSM/線形RNN
L4 exact     IO-aware 厳密（FlashAttention 系）
L5 kv-arch   KV アーキ（MQA/GQA/MLA）
L6 kv-post   KV 事後圧縮（eviction/量子化/層共有）
L7 sys       サービングシステム
L8 eval      ベンチマーク・批判

## レビューの論証の軸（4軸）
A FLOPs / B 実体化回避 / C 状態サイズ / D 厳密性

## 物語の骨格（第1稿）
1. 二つの問題は別物である（prefill vs decode, compute vs bandwidth）
2. 第一波(2018-22): 近似で A を攻めた → 全滅。理由5つ（LRA/因果性/定数/スケール則/スパイキー性）
3. 転回(2022): FlashAttention は A を下げず B を解いた → 近似の前提が消えた
4. 問題の移動: 学習から推論へ、FLOPs から帯域へ → KV キャッシュが主戦場に
5. KV への多方向攻撃（アーキ/退避/量子化/層共有/システム/事後低ランク）
6. 第二波(2023-25): C を定数にする再挑戦（SSM/線形RNN）。ただし表現力の壁
7. 収束点(2024-26): ハイブリッド + ネイティブ学習スパース（NSA/MoBA）
8. 評価の危機: NIAH で見えない劣化、SCBench、Retrieval Head
9. 未解決問題

## 要確認フラグ（本文で明示する）
- GPT-3 の Sparse Transformer 類似記述（高信頼だが本セッション未再取得）
- Titans の arXiv ID
- LLMLingua の arXiv ID
- Cartridges 後続 (2606.x) の詳細
- MQA の具体的速度数値
