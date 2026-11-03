---
name: backup-chat
description: >-
  ユーザーとの対話履歴・指示ログをプロジェクト内の archive/chat_history/ に抽出・永続バックアップし、
  Gitへコミット＆プッシュして安全に保存するスキル。
  ユーザーが「ログをバックアップして」「会話履歴を保存して」「チャット履歴を保存して」と指示した際に使用する。
---

# 対話・指示ログバックアップ スキル

ユーザーとの全発言・指示履歴およびセッション内容を抽出し、`archive/chat_history/` に保存してリモートリポジトリへ自動プッシュします。

## 実行手順

1. **ログ抽出スクリプトの実行**:
   ```powershell
   python develop/save_chat_history.py
   ```

2. **Git コミット＆自動プッシュ**:
   ```powershell
   git add archive/chat_history/
   git commit -m "Docs: Update chat transcript backup log"
   git push origin main
   ```

3. **完了確認**:
   - `archive/chat_history/chat_history_latest.md` が更新されていることを確認します。

