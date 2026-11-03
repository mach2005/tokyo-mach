# Antigravity / Gemini プロジェクト自動実行絶対設定

## 1. コマンド全自動実行＆デプロイルール
- **ユーザーへのコマンド実行依頼の禁止**: コマンドの実行（`git add .`, `git commit`, `git push origin main`, ビルドコマンド等）をユーザーに案内・依頼してはならない。
- **全自動Git Push**: コードやデザイン修正後は、自律的にコマンドまたはスクリプトを呼び出して GitHub Pages へのコミット＆デプロイまで完全自動で完遂すること。
- **エラー時の自律対応**: `run_command` 等の標準ツールでエラー（NULアクセス権限等）が発生した場合も、ユーザーに手動操作を求めず、Python `subprocess` スクリプト等を作成・バックグラウンド実行させて代替手段で全自動完遂すること。

## 2. 文字コード（UTF-8厳守）
- PowerShell の `>`, `>>`, `Set-Content` 等によるファイル操作は禁止（UTF-16LE化防止）。
- ファイル編集は必ず AI編集ツール (`replace_file_content` 等) または Python (`open(..., encoding='utf-8')`) で行うこと。

## 3. 会話ログ・事前バックアップ
- 作業前には必ず `python develop/backup_manager.py` で事前バックアップを取ること。
- 会話ログは `archive/chat_history/` に自動テキスト抽出保存すること。

## 4. Instagram自動更新＆画像ダウンロード・除外ルール
- Instagram更新時は `develop/download_and_update_ig.py` を使用し、外部広告等の無関係画像を除外して各投稿の純粋な写真のみを `public/images/` にダウンロード保存・更新すること。
- 正確な投稿日付（`2026.08.03` 等）を正確に反映し、カルーセル（画像送り機能 `moveIgCarousel`）のHTML構造を維持すること。

