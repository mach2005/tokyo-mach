# restore (.agents/workflows/restore.md)

## 概要
東京真隼プロジェクトにおいて、HTMLやデータファイルの編集前状態（`archive/backup/`）からワンタッチで直前状態に復元・ロールバックする手順書です。
ユーザーから「戻して」「元に戻して」「ロールバック」と指示された際、またはチャット欄で `/restore` と入力された際に呼び出します。

## 実行手順
1. **復元スクリプトの実行**:
   ```powershell
   python develop/backup_manager.py restore
   ```
2. **復元状態の確認**:
   - `git status` およびローカルHTMLファイルが修正前の正常状態に戻ったことを確認する。
3. **安全な再デプロイ**:
   - 復元完了後、`/deploy` ワークフローを実行し、GitHub Pages 側も修正前の正常な状態に即座に同期・公開する。
4. **報告**:
   - 復元完了と公開URLをユーザーに報告する。

