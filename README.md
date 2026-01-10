# 表情差分デモギャラリー（ComfyUI / Stable Diffusion）
# Expression Demo Gallery (ComfyUI / Stable Diffusion)

このリポジトリは、**表情差分がどの程度うまく出るか**をモデル別に確認できる **デモ用HTMLギャラリー（summary.html + 画像）** を公開しています。  
This repository provides **preview HTML galleries (summary.html + images)** to check how well facial expression variations appear across different models.

- 各モデルフォルダに `summary.html` を用意し、複数の表情差分を一覧で確認できます。  
  Each model folder contains a `summary.html` to browse multiple expression variations at a glance.
- 本リポジトリは **購入前の確認用途（デモ）** を目的としています。  
  This repository is intended **for preview/evaluation before purchase**.

---

## 近日公開予定（note有料記事） / Planned release (Note)

表情プリセット（プロンプト）および推奨パラメータは、**近日中にnoteの有料記事として販売予定**です。  
The expression presets (prompts) and recommended parameters will be released soon as a **paid Note article**.

その他モデルについても現在確認中。数モデルのデモを追加予定です。
More models are currently being evaluated, and we plan to add demo galleries for several additional models.

含める予定の内容 / Planned contents:
- 表情ごとのプロンプトプリセット / Prompt presets per expression
- 推奨パラメータ・チューニング方針 / Recommended parameters & tuning notes

（準備中） / (Coming soon)

---

## デモギャラリー（summary.html） / Demo galleries (summary.html)

各モデルのギャラリーはこちら / Open the gallery for each model:

- [**MeinaMix**](docs/MeinaMix_demo/summary.html)
- [**Counterfeit**](docs/Counterfeit_demo/summary.html)

> GitHub Pagesで閲覧している場合は、公開されたPagesのURLから上記パスにアクセスしてください。  
> If you are viewing via GitHub Pages, open these paths from the published Pages URL.

---

## ギャラリーの内容 / What you’ll find
- 8枚のサンプル画像 × 15表情 / 8 sample images × 15 expressions
- 同じワークフロー思想で、モデル（checkpoint）を切り替えて比較 / Same workflow concept, compared across models
- 「表情の出やすさ」「安定性」を視覚的に確認 / Visual comparison of expression strength and consistency

---

## ライセンス / License & Terms

- **コード / HTML / 設定ファイル**: `LICENSE` を参照  
  **Code / HTML / config files**: See `LICENSE`
- **デモ画像**: 閲覧用途のみ（再利用・再配布禁止）。`docs/DEMO_IMAGES_LICENSE.txt` を参照  
  **Demo images**: Preview only. No reuse / redistribution. See `docs/DEMO_IMAGES_LICENSE.txt`
- **モデル本体（重み）は同梱していません**。各モデルの配布元ページ・ライセンスを参照してください（`THIRD_PARTY_NOTICES.md`）  
  **Model weights are NOT included**. Refer to each model’s distribution page and license (see `THIRD_PARTY_NOTICES.md`).



