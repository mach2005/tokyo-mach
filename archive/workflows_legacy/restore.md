---
description: 修正前の状態に即座にロールバック（復元）してデプロイする
---

# 即時ロールバック（復元） ワークフロー

直前の変更を破棄し、修正直前に自動保存されたバックアップファイルからすべてのHTMLを即座に復元・再デプロイします。

## 手順

### 1. 直前バックアップからの復元実行

```powershell
python develop/backup_manager.py restore
```

### 2. リモートへ即時デプロイ

```powershell
git add .
git status
git commit -m "Rollback: Restore all HTML files to previous backup state"
git push origin main
Write-Host "✅ ロールバック（復元）とデプロイが完了しました。"
```
