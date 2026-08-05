---
description: 現在の対話・指示ログをテキスト形式でプロジェクト内に保存する
---

# 対話・指示ログバックアップ ワークフロー

ユーザーとの全発言・指示履歴を `archive/chat_history/` に抽出・保存します。

## 手順

```powershell
python develop/save_chat_history.py
git add archive/chat_history/
git commit -m "Docs: Update chat transcript backup log"
git push origin main
Write-Host "✅ 対話・指示ログのバックアップとGit送信が完了しました。"
```
