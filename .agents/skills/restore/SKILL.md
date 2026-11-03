---
name: restore
description: >-
  直前の変更を破棄し、直前の自動バックアップファイルからすべてのHTMLファイルを即座に復元（ロールバック）して
  GitHub Pages へ再デプロイするスキル。
  ユーザーが「元に戻して」「ロールバックして」「直前の状態に復元して」と指示した際に緊急使用する。
---

# 即時ロールバック（復元） スキル

直前の変更で不具合が生じた場合や、ユーザーからの「元に戻して」の指示にノータイムで対応するため、直前のバックアップ（`archive/backup/`）からHTMLファイルを一括復元し、GitHub Pages へ即座に反映します。

## 実行手順（完全自動化）

1. **直前バックアップからの復元実行**:
   ```powershell
   python develop/backup_manager.py restore
   ```

2. **Git ステージング・コミット・即時デプロイ**:
   ```powershell
   git add .
   git status
   git commit -m "Rollback: Restore all HTML files to previous backup state"
   git push origin main
   ```

3. **復元完了報告**:
   - 復元が完了し、GitHub Pages への送信が完了したことをユーザーに報告します。

