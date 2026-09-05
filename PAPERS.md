# 収録論文一覧

`map.html` にプロットした全 195 件。`tools/export_papers.py` が生成する。**直接編集しない。**

- 原題を特定できたもの: 194 / 195
- 一次ソース URL が確定するもの（arXiv）: 185 / 195
- 残りはブログ・GitHub・モデルカード・組織発表で、**URL を推測せず空欄にしてある**

調査基準日: 2026-09-04

## 疎化 Attention — 近似（13 件）

| 年月 | 名称 | 論文名（原題） | 著者 | 一次ソース |
|---|---|---|---|---|
| 2018.01 | **Memory-Compressed Attention (T-DMCA)** | Generating Wikipedia by Summarizing Long Sequences | Liu, Saleh, Pot, Goodrich, Sepassi, Kaiser, Shazeer (Google Brain) | [arXiv:1801.10198](https://arxiv.org/abs/1801.10198) |
| 2018.02 | **Image Transformer** | Image Transformer | Parmar, Vaswani, Uszkoreit, Kaiser, Shazeer, Ku, Tran | [arXiv:1802.05751](https://arxiv.org/abs/1802.05751) |
| 2019.04 | **Sparse Transformer** | Generating Long Sequences with Sparse Transformers | Child, Gray, Radford, Sutskever (OpenAI) | [arXiv:1904.10509](https://arxiv.org/abs/1904.10509) |
| 2019.05 | **Adaptive Attention Span** | Adaptive Attention Span in Transformers | Sukhbaatar, Grave, Bojanowski, Joulin | [arXiv:1905.07799](https://arxiv.org/abs/1905.07799) |
| 2019.09 | **Adaptively Sparse Transformers** | Adaptively Sparse Transformers | Correia, Niculae, Martins | [arXiv:1909.00015](https://arxiv.org/abs/1909.00015) |
| 2019.11 | **BlockBERT** | Blockwise Self-Attention for Long Document Understanding | Qiu, Ma, Levy, Yih, Wang, Tang | [arXiv:1911.02972](https://arxiv.org/abs/1911.02972) |
| 2020.01 | **Reformer** | Reformer: The Efficient Transformer | Kitaev, Kaiser, Levskaya | [arXiv:2001.04451](https://arxiv.org/abs/2001.04451) |
| 2020.02 | **Sparse Sinkhorn Attention** | Sparse Sinkhorn Attention | Tay, Bahri, Yang, Metzler, Juan | [arXiv:2002.11296](https://arxiv.org/abs/2002.11296) |
| 2020.03 | **Routing Transformer** | Efficient Content-Based Sparse Attention with Routing Transformers | Roy, Saffar, Vaswani, Grangier | [arXiv:2003.05997](https://arxiv.org/abs/2003.05997) |
| 2020.04 | **ETC** | ETC: Encoding Long and Structured Inputs in Transformers | Ainslie, Ontañón, Alberti, Cvicek, Fisher, Pham, Ravula, Sanghai, Wang, Yang | [arXiv:2004.08483](https://arxiv.org/abs/2004.08483) |
| 2020.04 | **Longformer** | Longformer: The Long-Document Transformer | Beltagy, Peters, Cohan (Allen AI) | [arXiv:2004.05150](https://arxiv.org/abs/2004.05150) |
| 2020.07 | **BigBird** | Big Bird: Transformers for Longer Sequences | Zaheer, Guruganesh, Dubey, Ainslie, Alberti, Ontañón ほか (Google) | [arXiv:2007.14062](https://arxiv.org/abs/2007.14062) |
| 2021.12 | **LongT5** | LongT5: Efficient Text-To-Text Transformer for Long Sequences | Guo, Ainslie, Uthus, Ontañón, Ni, Sung, Yang | [arXiv:2112.07916](https://arxiv.org/abs/2112.07916) |

## 線形・低ランク — 近似（11 件）

| 年月 | 名称 | 論文名（原題） | 著者 | 一次ソース |
|---|---|---|---|---|
| 2018.12 | **Efficient Attention** | Efficient Attention: Attention with Linear Complexities | Shen, Zhang, Zhao, Yi, Li (SenseTime / CUHK) | [arXiv:1812.01243](https://arxiv.org/abs/1812.01243) |
| 2020.05 | **Synthesizer** | Synthesizer: Rethinking Self-Attention for Transformer Models | Tay, Bahri, Metzler, Juan, Zhao, Zheng | [arXiv:2005.00743](https://arxiv.org/abs/2005.00743) |
| 2020.06 | **Linear Transformer** | Transformers are RNNs: Fast Autoregressive Transformers with Linear Attention | Katharopoulos, Vyas, Pappas, Fleuret | [arXiv:2006.16236](https://arxiv.org/abs/2006.16236) |
| 2020.06 | **Linformer** | Linformer: Self-Attention with Linear Complexity | Wang, Li, Khabsa, Fang, Ma (Facebook AI) | [arXiv:2006.04768](https://arxiv.org/abs/2006.04768) |
| 2020.09 | **Performer (FAVOR+)** | Rethinking Attention with Performers | Choromanski, Likhosherstov, Dohan, Song ほか (Google) | [arXiv:2009.14794](https://arxiv.org/abs/2009.14794) |
| 2021.02 | **Nyströmformer** | Nyströmformer: A Nyström-based Algorithm for Approximating Self-Attention | Xiong, Zeng, Chakraborty, Tan, Fung, Li, Singh | [arXiv:2102.03902](https://arxiv.org/abs/2102.03902) |
| 2021.03 | **Random Feature Attention** | Random Feature Attention | Peng, Pappas, Yogatama, Schwartz, Smith, Kong | [arXiv:2103.02143](https://arxiv.org/abs/2103.02143) |
| 2021.06 | **Luna** | Luna: Linear Unified Nested Attention | Ma, Kong, Wang, Zhou, May, Ma, Zettlemoyer | [arXiv:2106.01540](https://arxiv.org/abs/2106.01540) |
| 2021.10 | **Scatterbrain** | Scatterbrain: Unifying Sparse and Low-rank Attention Approximation | Chen, Dao, Winsor, Song, Rudra, Ré | [arXiv:2110.15343](https://arxiv.org/abs/2110.15343) |
| 2022.02 | **cosFormer** | cosFormer: Rethinking Softmax in Attention | Qin, Sun, Deng, Li, Wei, Lv, Yan, Kong, Zhong (OpenNLPLab / SenseTime) | [arXiv:2202.08791](https://arxiv.org/abs/2202.08791) |
| 2022.10 | **The Devil in Linear Transformer (TransNormer)** | The Devil in Linear Transformer | Qin, Han, Sun, Li, Kong, Barnes, Zhong (SenseTime / ANU / Shanghai AI Lab) | [arXiv:2210.10340](https://arxiv.org/abs/2210.10340) |

## 再帰・外部メモリ — 定数状態（4 件）

| 年月 | 名称 | 論文名（原題） | 著者 | 一次ソース |
|---|---|---|---|---|
| 2019.01 | **Transformer-XL** | Transformer-XL: Attentive Language Models Beyond a Fixed-Length Context | Dai, Yang, Yang, Carbonell, Le, Salakhutdinov | [arXiv:1901.02860](https://arxiv.org/abs/1901.02860) |
| 2019.11 | **Compressive Transformer** | Compressive Transformers for Long-Range Sequence Modelling | Rae, Potapenko, Jayakumar, Hillier, Lillicrap (DeepMind) | [arXiv:1911.05507](https://arxiv.org/abs/1911.05507) |
| 2021.09 | **∞-former** | ∞-former: Infinite Memory Transformer | Martins, Marinho, Martins | [arXiv:2109.00301](https://arxiv.org/abs/2109.00301) |
| 2022.03 | **Memorizing Transformers** | Memorizing Transformers | Wu, Rabe, Hutchins, Szegedy (Google) | [arXiv:2203.08913](https://arxiv.org/abs/2203.08913) |

## SSM・線形RNN — 定数状態（22 件）

| 年月 | 名称 | 論文名（原題） | 著者 | 一次ソース |
|---|---|---|---|---|
| 2020.08 | **HiPPO** | HiPPO: Recurrent Memory with Optimal Polynomial Projections | Gu, Dao, Ermon, Rudra, Ré | [arXiv:2008.07669](https://arxiv.org/abs/2008.07669) |
| 2021.10 | **LSSL** | Combining Recurrent, Convolutional, and Continuous-time Models with Linear State-Space Layers | Gu, Johnson, Goel, Saab, Dao, Rudra, Ré | [arXiv:2110.13985](https://arxiv.org/abs/2110.13985) |
| 2021.11 | **S4** | Efficiently Modeling Long Sequences with Structured State Spaces | Gu, Goel, Ré | [arXiv:2111.00396](https://arxiv.org/abs/2111.00396) |
| 2022.03 | **DSS** | Diagonal State Spaces are as Effective as Structured State Spaces | Gupta, Gu, Berant | [arXiv:2203.14343](https://arxiv.org/abs/2203.14343) |
| 2022.08 | **S5** | Simplified State Space Layers for Sequence Modeling | Smith, Warrington, Linderman | [arXiv:2208.04933](https://arxiv.org/abs/2208.04933) |
| 2022.12 | **H3** | Hungry Hungry Hippos: Towards Language Modeling with State Space Models | Fu, Dao, Saab, Thomas, Rudra, Ré | [arXiv:2212.14052](https://arxiv.org/abs/2212.14052) |
| 2023.02 | **Hyena** | Hyena Hierarchy: Towards Larger Convolutional Language Models | Poli, Massaroli, Nguyen, Fu, Dao, Baccus, Bengio, Ermon, Ré | [arXiv:2302.10866](https://arxiv.org/abs/2302.10866) |
| 2023.05 | **RWKV-4** | RWKV: Reinventing RNNs for the Transformer Era | Peng, Alcaide, Anthony ほか | [arXiv:2305.13048](https://arxiv.org/abs/2305.13048) |
| 2023.07 | **RetNet** | Retentive Network: A Successor to Transformer for Large Language Models | Sun, Dong, Huang, Ma ほか (Microsoft Research Asia) | [arXiv:2307.08621](https://arxiv.org/abs/2307.08621) |
| 2023.12 | **GLA (Gated Linear Attention)** | Gated Linear Attention Transformers with Hardware-Efficient Training | Yang, Wang, Shen, Panda, Kim | [arXiv:2312.06635](https://arxiv.org/abs/2312.06635) |
| 2023.12 | **Mamba** | Mamba: Linear-Time Sequence Modeling with Selective State Spaces | Gu, Dao | [arXiv:2312.00752](https://arxiv.org/abs/2312.00752) |
| 2024.04 | **RWKV-5/6 (Eagle/Finch)** | Eagle and Finch: RWKV with Matrix-Valued States and Dynamic Recurrence | Peng ほか (RWKV Foundation) | [arXiv:2404.05892](https://arxiv.org/abs/2404.05892) |
| 2024.05 | **Mamba-2 / SSD** | Transformers are SSMs: Generalized Models and Efficient Algorithms Through Structured State Space Duality | Dao, Gu | [arXiv:2405.21060](https://arxiv.org/abs/2405.21060) |
| 2024.05 | **xLSTM** | xLSTM: Extended Long Short-Term Memory | Beck, Pöppel, Spanring, Auer, Prudnikova, Kopp, Klambauer, Brandstetter, Hochreiter | [arXiv:2405.04517](https://arxiv.org/abs/2405.04517) |
| 2024.06 | **DeltaNet (parallelizing)** | Parallelizing Linear Transformers with the Delta Rule over Sequence Length | Yang, Wang, Zhang, Kim | [arXiv:2406.06484](https://arxiv.org/abs/2406.06484) |
| 2024.07 | **TTT layers** | Learning to (Learn at Test Time): RNNs with Expressive Hidden States | Sun, Li, Dalal ほか (Stanford / UCSD / Berkeley) | [arXiv:2407.04620](https://arxiv.org/abs/2407.04620) |
| 2024.12 | **Gated DeltaNet** | Gated Delta Networks: Improving Mamba2 with Delta Rule | Yang, Kautz, Hatamizadeh (NVIDIA) | [arXiv:2412.06464](https://arxiv.org/abs/2412.06464) |
| 2025.01 | **Lightning Attention / MiniMax-01** | MiniMax-01: Scaling Foundation Models with Lightning Attention | MiniMax | [arXiv:2501.08313](https://arxiv.org/abs/2501.08313) |
| 2025.01 | **Titans** | Titans: Learning to Memorize at Test Time | Behrouz, Zhong, Mirrokni (Google Research) | [arXiv:2501.00663](https://arxiv.org/abs/2501.00663) |
| 2025.03 | **RWKV-7 (Goose)** | RWKV-7 "Goose" with Expressive Dynamic State Evolution | Peng ほか (RWKV Foundation) | [arXiv:2503.14456](https://arxiv.org/abs/2503.14456) |
| 2025.10 | **Kimi Linear (KDA)** | Kimi Linear: An Expressive, Efficient Attention Architecture | Moonshot AI (Kimi Team) | [arXiv:2510.26692](https://arxiv.org/abs/2510.26692) |
| 2026.03 | **Mamba-3** ⚠ | Mamba-3 | Lahoti, Li, Chen, Wang, Bick, Kolter, Dao, Gu | [arXiv:2603.15569](https://arxiv.org/abs/2603.15569) |

## 厳密カーネル — 厳密（14 件）

| 年月 | 名称 | 論文名（原題） | 著者 | 一次ソース |
|---|---|---|---|---|
| 2018.05 | **Online Softmax** | Online normalizer calculation for softmax | Milakov, Gimelshein (NVIDIA) | [arXiv:1805.02867](https://arxiv.org/abs/1805.02867) |
| 2021.12 | **Self-attention Does Not Need O(n²) Memory** | Self-attention Does Not Need O(n²) Memory | Rabe, Staats (Google) | [arXiv:2112.05682](https://arxiv.org/abs/2112.05682) |
| 2022.05 | **FlashAttention** | FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness | Dao, Fu, Ermon, Rudra, Ré | [arXiv:2205.14135](https://arxiv.org/abs/2205.14135) |
| 2023.07 | **FlashAttention-2** | FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning | Tri Dao | [arXiv:2307.08691](https://arxiv.org/abs/2307.08691) |
| 2023.10 | **Flash-Decoding** | Flash-Decoding for long-context inference | Dao, Haziza, Massa, Sizov | PyTorch / CRFM blog |
| 2023.11 | **FlashDecoding++** | FlashDecoding++: Faster Large Language Model Inference on GPUs | Hong, Dai, Xu ほか (Tsinghua / Infinigence-AI) | [arXiv:2311.01282](https://arxiv.org/abs/2311.01282) |
| 2024.07 | **FlashAttention-3** | FlashAttention-3: Fast and Accurate Attention with Asynchrony and Low-precision | Shah, Bikshandi, Zhang, Thakkar, Ramani, Dao | [arXiv:2407.08608](https://arxiv.org/abs/2407.08608) |
| 2024.10 | **SageAttention** | SageAttention: Accurate 8-Bit Attention for Plug-and-play Inference Acceleration | Zhang, Huang, Zhang, Wei, Zhu, Chen (Tsinghua) | [arXiv:2410.02367](https://arxiv.org/abs/2410.02367) |
| 2024.11 | **SageAttention2** | SageAttention2: Efficient Attention with Thorough Outlier Smoothing and Per-thread INT4 Quantization | Zhang, Huang ほか (Tsinghua) | [arXiv:2411.10958](https://arxiv.org/abs/2411.10958) |
| 2024.12 | **FlexAttention** | FlexAttention: A Programming Model for Generating Optimized Attention Kernels | Dong, Feng, Guessous, Liang, He (Meta / PyTorch) | [arXiv:2412.05496](https://arxiv.org/abs/2412.05496) |
| 2025.01 | **FlashInfer** | FlashInfer: Efficient and Customizable Attention Engine for LLM Inference Serving | Ye, Lai, Zhou ほか | [arXiv:2501.01005](https://arxiv.org/abs/2501.01005) |
| 2025.05 | **SageAttention3** | SageAttention3: Microscaling FP4 Attention for Inference and an Exploration of 8-Bit Training | Zhang ほか (Tsinghua) | [arXiv:2505.11594](https://arxiv.org/abs/2505.11594) |
| 2025.09 | **FlashMLA** | FlashMLA (GitHub) | DeepSeek-AI | GitHub (DeepSeek) |
| 2026.03 | **FlashAttention-4** | FlashAttention-4 | Zadouri, Hoehnerbach, Shah, Liu, Thakkar, Dao | [arXiv:2603.05451](https://arxiv.org/abs/2603.05451) |

## 分散・文脈並列 — 厳密（6 件）

| 年月 | 名称 | 論文名（原題） | 著者 | 一次ソース |
|---|---|---|---|---|
| 2022.05 | **Reducing Activation Recomputation** | Reducing Activation Recomputation in Large Transformer Models | Korthikanti, Casper, Lym, McAfee, Andersch, Shoeybi, Catanzaro (NVIDIA) | [arXiv:2205.05198](https://arxiv.org/abs/2205.05198) |
| 2023.05 | **Blockwise Parallel Transformer** | Blockwise Parallel Transformer for Large Context Models | Liu, Abbeel (Berkeley) | [arXiv:2305.19370](https://arxiv.org/abs/2305.19370) |
| 2023.09 | **DeepSpeed-Ulysses** | DeepSpeed Ulysses: System Optimizations for Enabling Training of Extreme Long Sequence Transformer Models | Jacobs, Tanaka ほか (Microsoft) | [arXiv:2309.14509](https://arxiv.org/abs/2309.14509) |
| 2023.10 | **Ring Attention** | Ring Attention with Blockwise Transformers for Near-Infinite Context | Liu, Zaharia, Abbeel (Berkeley) | [arXiv:2310.01889](https://arxiv.org/abs/2310.01889) |
| 2023.11 | **Striped Attention** | Striped Attention: Faster Ring Attention for Causal Transformers | Brandon, Nrusimha, Qian, Ankner, Jin, Song, Ragan-Kelley (MIT) | [arXiv:2311.09431](https://arxiv.org/abs/2311.09431) |
| 2024.05 | **USP** | USP: A Unified Sequence Parallelism Approach for Long Context Generative AI | Fang, Zhao | [arXiv:2405.07719](https://arxiv.org/abs/2405.07719) |

## KV アーキテクチャ — KV 圧縮（12 件）

| 年月 | 名称 | 論文名（原題） | 著者 | 一次ソース |
|---|---|---|---|---|
| 2019.11 | **MQA (Multi-Query Attention)** | Fast Transformer Decoding: One Write-Head is All You Need | Noam Shazeer | [arXiv:1911.02150](https://arxiv.org/abs/1911.02150) |
| 2023.05 | **GQA** | GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints | Ainslie, Lee-Thorp, de Jong, Zemlyanskiy, Lebrón, Sanghai | [arXiv:2305.13245](https://arxiv.org/abs/2305.13245) |
| 2024.05 | **CLA (Cross-Layer Attention)** | Reducing Transformer Key-Value Cache Size with Cross-Layer Attention | Brandon, Mishra, Nrusimha, Panda, Kelly (MIT) | [arXiv:2405.12981](https://arxiv.org/abs/2405.12981) |
| 2024.05 | **Layer-Condensed KV Cache** | Layer-Condensed KV Cache for Efficient Inference of Large Language Models | Wu, Tu ほか | [arXiv:2405.10637](https://arxiv.org/abs/2405.10637) |
| 2024.05 | **MLA (DeepSeek-V2)** | DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model | DeepSeek-AI | [arXiv:2405.04434](https://arxiv.org/abs/2405.04434) |
| 2024.05 | **YOCO** | You Only Cache Once: Decoder-Decoder Architectures for Language Models | Sun, Dong ほか (Microsoft) | [arXiv:2405.05254](https://arxiv.org/abs/2405.05254) |
| 2024.06 | **MLKV** | MLKV: Multi-Layer Key-Value Heads for Memory Efficient Transformer Decoding | Zuhri ほか | [arXiv:2406.09297](https://arxiv.org/abs/2406.09297) |
| 2024.12 | **MFA (Multi-Matrix Factorization Attn)** | Multi-matrix Factorization Attention | StepFun | [arXiv:2412.19255](https://arxiv.org/abs/2412.19255) |
| 2025.01 | **TPA (Tensor Product Attention)** | Tensor Product Attention Is All You Need | Zhang, Liu, Yuan, Qin, Yuan, Gu, Yao | [arXiv:2501.06425](https://arxiv.org/abs/2501.06425) |
| 2025.02 | **TransMLA** | TransMLA: Multi-Head Latent Attention Is All You Need | Meng, Tang, Zhang ほか (Peking University) | [arXiv:2502.07864](https://arxiv.org/abs/2502.07864) |
| 2025.05 | **GTA / GLA (hardware-efficient)** | Hardware-Efficient Attention for Fast Decoding | Zadouri, Strauss, Dao | [arXiv:2505.21487](https://arxiv.org/abs/2505.21487) |
| 2026.06 | **Keyless Attention** | Keyless Attention: Value-Space Routing and Value-Only Caching for Efficient Transformers | Gao (York University), Xu (UC Davis) | [arXiv:2606.21848](https://arxiv.org/abs/2606.21848) |

## KV 事後圧縮 — KV 圧縮（36 件）

| 年月 | 名称 | 論文名（原題） | 著者 | 一次ソース |
|---|---|---|---|---|
| 2023.04 | **Gist tokens** | Learning to Compress Prompts with Gist Tokens | Mu, Li, Goodman (Stanford) | [arXiv:2304.08467](https://arxiv.org/abs/2304.08467) |
| 2023.05 | **Scissorhands** | Scissorhands: Exploiting the Persistence of Importance Hypothesis for LLM KV Cache Compression at Test Time | Liu, Desai, Liao, Wang, Xie, Xu, Kyrillidis, Shrivastava | [arXiv:2305.17118](https://arxiv.org/abs/2305.17118) |
| 2023.06 | **H2O (Heavy-Hitter Oracle)** | H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models | Zhang, Sheng, Zhou, Chen ほか | [arXiv:2306.14048](https://arxiv.org/abs/2306.14048) |
| 2023.06 | **LLMLingua** | LLMLingua: Compressing Prompts for Accelerated Inference of Large Language Models | Jiang, Wu, Lin, Yang, Qiu (Microsoft) | EMNLP 2023 |
| 2023.07 | **ICAE** | In-context Autoencoder for Context Compression in a Large Language Model | Ge, Hu, Wang, Chen, Wei | [arXiv:2307.06945](https://arxiv.org/abs/2307.06945) |
| 2023.09 | **StreamingLLM** | Efficient Streaming Language Models with Attention Sinks | Xiao, Tian, Chen, Han, Lewis | [arXiv:2309.17453](https://arxiv.org/abs/2309.17453) |
| 2023.10 | **Atom** | Atom: Low-bit Quantization for Efficient and Accurate LLM Serving | Zhao, Lin, Zhu ほか | [arXiv:2310.19102](https://arxiv.org/abs/2310.19102) |
| 2023.10 | **FastGen** | Model Tells You What to Discard: Adaptive KV Cache Compression for LLMs | Ge, Zhang, Liu ほか | [arXiv:2310.01801](https://arxiv.org/abs/2310.01801) |
| 2023.10 | **LongLLMLingua** | LongLLMLingua: Accelerating and Enhancing LLMs in Long Context Scenarios via Prompt Compression | Jiang, Wu, Luo ほか (Microsoft) | [arXiv:2310.06839](https://arxiv.org/abs/2310.06839) |
| 2024.01 | **KVQuant** | KVQuant: Towards 10 Million Context Length LLM Inference with KV Cache Quantization | Hooper, Kim, Mohammadzadeh ほか (Berkeley) | [arXiv:2401.18079](https://arxiv.org/abs/2401.18079) |
| 2024.01 | **TOVA** | Transformers are Multi-State RNNs | Oren, Hassid, Adi, Schwartz | [arXiv:2401.06104](https://arxiv.org/abs/2401.06104) |
| 2024.02 | **KIVI** | KIVI: A Tuning-Free Asymmetric 2bit Quantization for KV Cache | Liu, Yuan, Jin, Zhong, Xu, Braverman, Chen, Hu | [arXiv:2402.02750](https://arxiv.org/abs/2402.02750) |
| 2024.03 | **Keyformer** | Keyformer: KV Cache Reduction through Key Tokens Selection for Efficient Generative Inference | Adnan, Arunkumar, Jain ほか | [arXiv:2403.09054](https://arxiv.org/abs/2403.09054) |
| 2024.04 | **Infini-attention** | Leave No Context Behind: Efficient Infinite Context Transformers with Infini-attention | Munkhdalai, Faruqui, Gopal (Google) | [arXiv:2404.07143](https://arxiv.org/abs/2404.07143) |
| 2024.04 | **SnapKV** | SnapKV: LLM Knows What You are Looking for Before Generation | Li, Huang, Yang ほか | [arXiv:2404.14469](https://arxiv.org/abs/2404.14469) |
| 2024.05 | **Coupled Quantization** | KV Cache is 1 Bit Per Channel: Efficient Large Language Model Inference with Coupled Quantization | Zhang, Yi, Xu, Shrivastava | [arXiv:2405.03917](https://arxiv.org/abs/2405.03917) |
| 2024.05 | **MiniCache** | MiniCache: KV Cache Compression in Depth Dimension for Large Language Models | Liu, Yan, Zhang ほか | [arXiv:2405.14366](https://arxiv.org/abs/2405.14366) |
| 2024.05 | **PyramidInfer** | PyramidInfer: Pyramid KV Cache Compression for High-throughput LLM Inference | Yang, Han, Xu ほか | [arXiv:2405.12532](https://arxiv.org/abs/2405.12532) |
| 2024.05 | **QServe (W4A8KV4)** | QServe: W4A8KV4 Quantization and System Co-design for Efficient LLM Serving | Lin, Tang, Yang, Zhang, Xiao, Gan, Han (MIT / NVIDIA) | [arXiv:2405.04532](https://arxiv.org/abs/2405.04532) |
| 2024.06 | **PyramidKV** | PyramidKV: Dynamic KV Cache Compression based on Pyramidal Information Funneling | Cai, Zhang, Chen ほか | [arXiv:2406.02069](https://arxiv.org/abs/2406.02069) |
| 2024.06 | **Quest** | Quest: Query-Aware Sparsity for Efficient Long-Context LLM Inference | Tang, Zhao, Zhu ほか (MIT HAN Lab) | [arXiv:2406.10774](https://arxiv.org/abs/2406.10774) |
| 2024.07 | **Ada-KV** | Ada-KV: Optimizing KV Cache Eviction by Adaptive Budget Allocation for Efficient LLM Inference | Feng, Fu, Cai ほか | [arXiv:2407.11550](https://arxiv.org/abs/2407.11550) |
| 2024.07 | **MInference 1.0** | MInference 1.0: Accelerating Pre-filling for Long-Context LLMs via Dynamic Sparse Attention | Jiang, Li, Zhang ほか (Microsoft) | [arXiv:2407.02490](https://arxiv.org/abs/2407.02490) |
| 2024.07 | **Palu** | Palu: KV-Cache Compression with Low-Rank Projection | Chang, Lin ほか | [arXiv:2407.21118](https://arxiv.org/abs/2407.21118) |
| 2024.08 | **Eigen Attention** | Eigen Attention: Attention in Low-Rank Space for KV Cache Compression | Saxena, Sharify, Roy, Wang | [arXiv:2408.05646](https://arxiv.org/abs/2408.05646) |
| 2024.09 | **RetrievalAttention** | RetrievalAttention: Accelerating Long-Context LLM Inference via Vector Retrieval | Liu, Li, Cheng ほか (Microsoft) | [arXiv:2409.10516](https://arxiv.org/abs/2409.10516) |
| 2024.10 | **DuoAttention** | DuoAttention: Efficient Long-Context LLM Inference with Retrieval and Streaming Heads | Xiao, Tang, Zuo, Guo, Yang, Tang, Fu, Han (MIT HAN Lab) | [arXiv:2410.10819](https://arxiv.org/abs/2410.10819) |
| 2024.10 | **LoRC** | LoRC: Low-Rank Compression for LLMs KV Cache with a Progressive Compression Strategy | Zhang ほか | [arXiv:2410.03111](https://arxiv.org/abs/2410.03111) |
| 2024.10 | **ShadowKV** | ShadowKV: KV Cache in Shadows for High-Throughput Long-Context LLM Inference | Sun, Chang, Bao, Zheng, Zheng, Liu, Dong, Chi, Chen | [arXiv:2410.21465](https://arxiv.org/abs/2410.21465) |
| 2025.02 | **MoBA (Mixture of Block Attention)** | MoBA: Mixture of Block Attention for Long-Context LLMs | Moonshot AI (Kimi) | [arXiv:2502.13189](https://arxiv.org/abs/2502.13189) |
| 2025.02 | **NSA (Native Sparse Attention)** | Native Sparse Attention: Hardware-Aligned and Natively Trainable Sparse Attention | DeepSeek-AI | [arXiv:2502.11089](https://arxiv.org/abs/2502.11089) |
| 2025.06 | **Cartridges** | Cartridges: Lightweight and general-purpose long context representations via self-study | Eyuboglu, Ehrlich, Arora ほか (Stanford ほか) | [arXiv:2506.06266](https://arxiv.org/abs/2506.06266) |
| 2025.09 | **DSA (DeepSeek-V3.2)** | DeepSeek-V3.2: Boosting Long-Context Efficiency with DeepSeek Sparse Attention | DeepSeek-AI | [arXiv:2512.02556](https://arxiv.org/abs/2512.02556) |
| 2026.04 | **KSA (Kwai Summary Attention)** | Kwai Summary Attention (KSA) | Kuaishou (Kwai) | [arXiv:2604.24432](https://arxiv.org/abs/2604.24432) |
| 2026.06 | **MiniMax-M3 (MSA)** | MiniMax Sparse Attention | Lai ほか (MiniMax) | [arXiv:2606.13392](https://arxiv.org/abs/2606.13392) |
| 2026.08 | **LongCat Sparse Attention** | LongCat Sparse Attention | Meituan LongCat Team | [arXiv:2608.01662](https://arxiv.org/abs/2608.01662) |

## サービングシステム — システム（20 件）

| 年月 | 名称 | 論文名（原題） | 著者 | 一次ソース |
|---|---|---|---|---|
| 2022.08 | **Orca** | Orca: A Distributed Serving System for Transformer-Based Generative Models | Yu, Jeong, Kim, Kim, Chun | OSDI 2022 |
| 2022.11 | **Speculative Decoding (Leviathan)** | Fast Inference from Transformers via Speculative Decoding | Leviathan, Kalman, Matias (Google) | [arXiv:2211.17192](https://arxiv.org/abs/2211.17192) |
| 2023.02 | **Speculative Sampling (DeepMind)** | Accelerating Large Language Model Decoding with Speculative Sampling | Chen, Borgeaud, Irving, Lespiau, Sifre, Jumper (DeepMind) | [arXiv:2302.01318](https://arxiv.org/abs/2302.01318) |
| 2023.03 | **FlexGen** | FlexGen: High-Throughput Generative Inference of Large Language Models with a Single GPU | Sheng, Zheng, Yuan, Li ほか | [arXiv:2303.06865](https://arxiv.org/abs/2303.06865) |
| 2023.08 | **Sarathi** | SARATHI: Efficient LLM Inference by Piggybacking Decodes with Chunked Prefills | Agrawal, Panwar, Mohan ほか (MSR India) | [arXiv:2308.16369](https://arxiv.org/abs/2308.16369) |
| 2023.09 | **PagedAttention / vLLM** | Efficient Memory Management for Large Language Model Serving with PagedAttention | Kwon, Li, Zhuang, Sheng, Zheng, Yu, Gonzalez, Zhang, Stoica | [arXiv:2309.06180](https://arxiv.org/abs/2309.06180) |
| 2023.11 | **Splitwise** | Splitwise: Efficient Generative LLM Inference Using Phase Splitting | Patel, Choukse, Zhang ほか (Microsoft Azure) | [arXiv:2311.18677](https://arxiv.org/abs/2311.18677) |
| 2023.12 | **LLM in a Flash** | LLM in a flash: Efficient Large Language Model Inference with Limited Memory | Alizadeh, Mirzadeh, Belenko ほか (Apple) | [arXiv:2312.11514](https://arxiv.org/abs/2312.11514) |
| 2024.01 | **DistServe** | DistServe: Disaggregating Prefill and Decoding for Goodput-optimized Large Language Model Serving | Zhong, Liu, Chen, Hu, Zhu, Liu, Jin, Zhang | [arXiv:2401.09670](https://arxiv.org/abs/2401.09670) |
| 2024.01 | **EAGLE** | EAGLE: Speculative Sampling Requires Rethinking Feature Uncertainty | Li, Wei, Zhang, Zhang (Peking University) | [arXiv:2401.15077](https://arxiv.org/abs/2401.15077) |
| 2024.01 | **Medusa** | Medusa: Simple LLM Inference Acceleration Framework with Multiple Decoding Heads | Cai, Li, Geng ほか | [arXiv:2401.10774](https://arxiv.org/abs/2401.10774) |
| 2024.01 | **RadixAttention / SGLang** | SGLang: Efficient Execution of Structured Language Model Programs | Zheng, Yin, Xie ほか | [arXiv:2312.07104](https://arxiv.org/abs/2312.07104) |
| 2024.03 | **Sarathi-Serve** | Taming Throughput-Latency Tradeoff in LLM Inference with Sarathi-Serve | Agrawal, Kedia, Panwar ほか (MSR India) | [arXiv:2403.02310](https://arxiv.org/abs/2403.02310) |
| 2024.06 | **EAGLE-2** | EAGLE-2: Faster Inference of Language Models with Dynamic Draft Trees | Li, Wei, Zhang, Zhang | [arXiv:2406.16858](https://arxiv.org/abs/2406.16858) |
| 2024.06 | **InfiniGen** | InfiniGen: Efficient Generative Inference of Large Language Models with Dynamic KV Cache Management | Lee, Park ほか | [arXiv:2406.19707](https://arxiv.org/abs/2406.19707) |
| 2024.07 | **Mooncake** | Mooncake: A KVCache-centric Disaggregated Architecture for LLM Serving | Qin, Wang, Zhang ほか (Moonshot AI) | [arXiv:2407.00079](https://arxiv.org/abs/2407.00079) |
| 2025.03 | **EAGLE-3** | EAGLE-3: Scaling up Inference Acceleration of Large Language Models via Training-Time Test | Li, Wei, Zhang, Zhang | [arXiv:2503.01840](https://arxiv.org/abs/2503.01840) |
| 2025.10 | **LMCache** | LMCache: A KV Cache Layer for Efficient LLM Serving | — | [arXiv:2510.09665](https://arxiv.org/abs/2510.09665) |
| 2026.06 | **Multi-Segment Attention (AsymCache)** | Multi-Segment Attention: Enabling Efficient KV-Cache Management for Faster Large Language Model Serving | Shi, Chen, Chen, Miao, Cui (Peking University) | [arXiv:2606.02964](https://arxiv.org/abs/2606.02964) |
| 2026.08 | **HiSparse** | HiSparse: Scaling Sparse-Attention Decoding with Hierarchical KV Cache Management | Xie, Huang, Huang, Xu, Ma, Kozyrakis (Stanford / Alibaba / Ant / SJTU / PKU / NVIDIA) | [arXiv:2608.07009](https://arxiv.org/abs/2608.07009) |

## 実運用モデル — 実運用モデル（34 件）

| 年月 | 名称 | 論文名（原題） | 著者 | 一次ソース |
|---|---|---|---|---|
| 2023.10 | **Mistral 7B (SWA)** | Mistral 7B | Jiang, Sablayrolles, Mensch ほか (Mistral AI) | [arXiv:2310.06825](https://arxiv.org/abs/2310.06825) |
| 2024.02 | **Griffin / Hawk** | Griffin: Mixing Gated Linear Recurrences with Local Attention for Efficient Language Models | De, Smith, Fernando ほか (DeepMind) | [arXiv:2402.19427](https://arxiv.org/abs/2402.19427) |
| 2024.03 | **Jamba** | Jamba: A Hybrid Transformer-Mamba Language Model | AI21 Labs | [arXiv:2403.19887](https://arxiv.org/abs/2403.19887) |
| 2024.04 | **RecurrentGemma** | RecurrentGemma: Moving Past Transformers for Efficient Open Language Models | Google DeepMind | [arXiv:2404.07839](https://arxiv.org/abs/2404.07839) |
| 2024.05 | **Zamba / Zamba2** | Zamba: A Compact 7B SSM Hybrid Model | Glorioso, Anthony ほか (Zyphra) | [arXiv:2405.16712](https://arxiv.org/abs/2405.16712) |
| 2024.06 | **Character.AI 推論スタック** | Optimizing AI Inference at Character.AI (エンジニアリングブログ) | Character.AI | エンジニアリングブログ |
| 2024.06 | **Samba** | Samba: Simple Hybrid State Space Models for Efficient Unlimited Context Language Modeling | Ren, Liu, Gao ほか (Microsoft) | [arXiv:2406.07522](https://arxiv.org/abs/2406.07522) |
| 2024.08 | **Gemma 2** | Gemma 2: Improving Open Language Models at a Practical Size | Google DeepMind | [arXiv:2408.00118](https://arxiv.org/abs/2408.00118) |
| 2024.08 | **Jamba-1.5** | Jamba-1.5: Hybrid Transformer-Mamba Models at Scale | AI21 Labs | [arXiv:2408.12570](https://arxiv.org/abs/2408.12570) |
| 2024.08 | **The Mamba in the Llama** | The Mamba in the Llama: Distilling and Accelerating Hybrid Models | Wang, Paliotta, May, Rush, Dao | [arXiv:2408.15237](https://arxiv.org/abs/2408.15237) |
| 2024.08 | **MOHAWK** | Transformers to SSMs: Distilling Quadratic Knowledge to Subquadratic Models | Bick, Li, Xing, Kolter, Gu | [arXiv:2408.10189](https://arxiv.org/abs/2408.10189) |
| 2024.10 | **LoLCATs** | LoLCATs: On Low-Rank Linearizing of Large Language Models | Zhang, Arora, Chalamala, Wu, Spector, Singhal, Ramesh, Ré (HazyResearch) | [arXiv:2410.10254](https://arxiv.org/abs/2410.10254) |
| 2025.02 | **Llamba** | Llamba: Scaling Distilled Recurrent Models for Efficient Language Processing | Bick, Katsch, Sohoni, Desai, Gu (Cartesia AI) | [arXiv:2502.14458](https://arxiv.org/abs/2502.14458) |
| 2025.03 | **Gemma 3** | Gemma 3 Technical Report | Google DeepMind | [arXiv:2503.19786](https://arxiv.org/abs/2503.19786) |
| 2025.04 | **Llama 4 (iRoPE)** ⚠ | Llama 4 (公式ブログ) | Meta AI | Meta blog（要確認） |
| 2025.04 | **Nemotron-H** | Nemotron-H: A Family of Accurate and Efficient Hybrid Mamba-Transformer Models | NVIDIA | [arXiv:2504.03624](https://arxiv.org/abs/2504.03624) |
| 2025.05 | **Hunyuan-TurboS** | Hunyuan-TurboS: Advancing Large Language Models through Mamba-Transformer Synergy | Tencent Hunyuan | [arXiv:2505.15431](https://arxiv.org/abs/2505.15431) |
| 2025.06 | **MiniMax-M1** | MiniMax-M1: Scaling Test-Time Compute Efficiently with Lightning Attention | MiniMax | [arXiv:2506.13585](https://arxiv.org/abs/2506.13585) |
| 2025.07 | **Falcon-H1** | Falcon-H1: A Family of Hybrid-Head Language Models | TII | [arXiv:2507.22448](https://arxiv.org/abs/2507.22448) |
| 2025.07 | **Step-3 (MFA + AFD)** | Step-3 is Large yet Affordable: Model-system Co-design for Cost-effective Decoding | StepFun | [arXiv:2507.19427](https://arxiv.org/abs/2507.19427) |
| 2025.08 | **GLM-4.5** | GLM-4.5: Agentic, Reasoning, and Coding (ARC) Foundation Models | Zhipu AI / Z.ai | [arXiv:2508.06471](https://arxiv.org/abs/2508.06471) |
| 2025.09 | **Qwen3-Next** ⚠ | Qwen3-Next (モデルカード / 公式ブログ) | Qwen Team, Alibaba | モデルカード（要確認） |
| 2025.10 | **IBM Granite 4.0** ⚠ | IBM Granite 4.0 (公式発表) | IBM | IBM 発表（要確認） |
| 2025.10 | **Every Attention Matters (Ling 2.0)** | Every Attention Matters: An Efficient Hybrid Architecture for Long-Context Reasoning | Ant Group / InclusionAI | [arXiv:2510.19338](https://arxiv.org/abs/2510.19338) |
| 2025.11 | **MiniMax-M2（フル Attention 回帰）** | MiniMax-M2 (技術報告) | MiniMax | [arXiv:2605.26494](https://arxiv.org/abs/2605.26494) |
| 2026.02 | **ERNIE 5.0** | ERNIE 5.0 (技術報告) | Baidu | [arXiv:2602.04705](https://arxiv.org/abs/2602.04705) |
| 2026.02 | **GLM-5** | GLM-5: from Vibe Coding to Agentic Engineering | Zhipu AI / Z.ai | [arXiv:2602.15763](https://arxiv.org/abs/2602.15763) |
| 2026.02 | **Qwen3.5** ⚠ | Qwen3.5 (モデルカード / 公式ブログ) | Qwen Team, Alibaba | モデルカード（要確認） |
| 2026.02 | **Step 3.5 Flash** | Step 3.5 Flash (技術報告) | StepFun | [arXiv:2602.10604](https://arxiv.org/abs/2602.10604) |
| 2026.06 | **DeepSeek-V4 (CSA + HCA)** | DeepSeek-V4 (技術報告) | DeepSeek-AI | [arXiv:2606.19348](https://arxiv.org/abs/2606.19348) |
| 2026.06 | **Ring / Ling 2.6** | Ring / Ling 2.6 (技術報告) | Ant Group / InclusionAI | [arXiv:2606.15079](https://arxiv.org/abs/2606.15079) |
| 2026.07 | **Kimi K3** | Kimi K3 (技術報告) | Moonshot AI (Kimi Team) | [arXiv:2607.24653](https://arxiv.org/abs/2607.24653) |
| 2026.08 | **Qwen3.8-Flash-Next (QSA + Gated Residual)** | On the Design of Qwen3.8-Next Architecture: Evaluation, Efficiency, and Training Stability | Qiu, Wang, Li, Li, Xu ほか (Qwen Team) | [arXiv:2608.30320](https://arxiv.org/abs/2608.30320) |
| 2026.08 | **Qwen3.8-Max** ⚠ | 専用の技術報告は存在しない（config.json / GitHub README に基づく） | Qwen Team, Alibaba | config.json / GitHub（技術報告なし） |

## 理論・評価・批判 — 理論・評価（23 件）

| 年月 | 名称 | 論文名（原題） | 著者 | 一次ソース |
|---|---|---|---|---|
| 2020.09 | **Efficient Transformers: A Survey** | Efficient Transformers: A Survey | Tay, Dehghani, Bahri, Metzler | [arXiv:2009.06732](https://arxiv.org/abs/2009.06732) |
| 2020.11 | **Long Range Arena** | Long Range Arena: A Benchmark for Efficient Transformers | Tay, Dehghani, Abnar, Shen, Bahri ほか | [arXiv:2011.04006](https://arxiv.org/abs/2011.04006) |
| 2021.09 | **Do Long-Range LMs Use Long-Range Context?** | Do Long-Range Language Models Actually Use Long-Range Context? | Sun, Krishna, Mattarella-Micke, Iyyer | [arXiv:2109.09115](https://arxiv.org/abs/2109.09115) |
| 2022.07 | **Scaling Laws vs Model Architectures** | Scaling Laws vs Model Architectures: How does Inductive Bias Influence Scaling? | Tay, Dehghani ほか (Google) | [arXiv:2207.10551](https://arxiv.org/abs/2207.10551) |
| 2022.10 | **CAB benchmark** | CAB: Comprehensive Attention Benchmarking on Long Sequence Modeling | Zhang ほか | [arXiv:2210.07661](https://arxiv.org/abs/2210.07661) |
| 2023.10 | **Why Softmax Outperforms Linear Attention** | — | — | [arXiv:2310.11685](https://arxiv.org/abs/2310.11685) |
| 2023.12 | **Zoology** | Zoology: Measuring and Improving Recall in Efficient Language Models | Arora, Eyuboglu ほか (HazyResearch) | [arXiv:2312.04927](https://arxiv.org/abs/2312.04927) |
| 2024.02 | **Based** | Simple linear attention language models balance the recall-throughput tradeoff | Arora, Eyuboglu, Zhang ほか (HazyResearch) | [arXiv:2402.18668](https://arxiv.org/abs/2402.18668) |
| 2024.04 | **The Illusion of State in SSMs** | The Illusion of State in State-Space Models | Merrill, Petty, Sabharwal | [arXiv:2404.08819](https://arxiv.org/abs/2404.08819) |
| 2024.04 | **Retrieval Head** | Retrieval Head Mechanistically Explains Long-Context Factuality | Wu, Wang, Xiao, Peng, Fu | [arXiv:2404.15574](https://arxiv.org/abs/2404.15574) |
| 2024.05 | **Expressive Capacity of SSMs** | The Expressive Capacity of State Space Models: A Formal Language Perspective | Sarrof, Veitsman, Hahn | [arXiv:2405.17394](https://arxiv.org/abs/2405.17394) |
| 2024.07 | **KV圧縮の代償ベンチマーク** | KV Cache Compression, But What Must We Give in Return? A Comprehensive Benchmark of Long Context Capable Approaches | Yuan, Liu, Feng ほか | [arXiv:2407.01527](https://arxiv.org/abs/2407.01527) |
| 2024.11 | **Negative Eigenvalues で状態追跡を解放** | Unlocking State-Tracking in Linear RNNs Through Negative Eigenvalues | Grazzi, Siems, Franke, Zela, Hutter, Pontil | [arXiv:2411.12537](https://arxiv.org/abs/2411.12537) |
| 2024.12 | **KV Cache Management サーベイ** | A Survey on Large Language Model Acceleration based on KV Cache Management | Li, Li, Tian, Tang, Xu, Chen, Hu, Dong, Li, Chen | [arXiv:2412.19442](https://arxiv.org/abs/2412.19442) |
| 2024.12 | **SCBench** | SCBench: A KV Cache-Centric Analysis of Long-Context Methods | Li, Jiang, Zhang ほか (Microsoft) | [arXiv:2412.10319](https://arxiv.org/abs/2412.10319) |
| 2024.12 | **SSM/Mamba の計算限界** | The Computational Limits of State-Space Models and Mamba via the Lens of Circuit Complexity | — | [arXiv:2412.06148](https://arxiv.org/abs/2412.06148) |
| 2025.02 | **Compression Barriers** | Compression Barriers for Autoregressive Transformers | Haris, Onak (Boston University) | [arXiv:2502.15955](https://arxiv.org/abs/2502.15955) |
| 2025.02 | **Semantic Integrity Matters (KVFundaBench)** | Semantic Integrity Matters: Benchmarking and Preserving High-Density Reasoning in KV Cache Compression | Liu, Tang, Chen, Dong, Li, Zhou, Li, Hu, Chu (HKUST) | [arXiv:2502.01941](https://arxiv.org/abs/2502.01941) |
| 2025.10 | **The Pitfalls of KV Cache Compression** | The Pitfalls of KV Cache Compression | Chen, Geh, Grover, Van den Broeck, Israel (UCLA) | [arXiv:2510.00231](https://arxiv.org/abs/2510.00231) |
| 2025.11 | **Nemotron-Flash** | Nemotron-Flash | NVIDIA | [arXiv:2511.18890](https://arxiv.org/abs/2511.18890) |
| 2026.02 | **Neural Attention Search Linear** | Neural Attention Search Linear | — | [arXiv:2602.03681](https://arxiv.org/abs/2602.03681) |
| 2026.06 | **NLL-Guided Full-Attention Layer Selection** | NLL-Guided Full-Attention Layer Selection | — | [arXiv:2606.27791](https://arxiv.org/abs/2606.27791) |
| 2026.06 | **Rethinking Efficient Attention in Hybrids** | Rethinking the Role of Efficient Attention in Hybrid Architectures | Tsinghua / OpenBMB | [arXiv:2606.15378](https://arxiv.org/abs/2606.15378) |

---

⚠ は一次情報に到達できず、二次情報または組織発表に依拠している項目。
レビュー論文の第 10 章「出典と検証状況」に理由を列挙している。
