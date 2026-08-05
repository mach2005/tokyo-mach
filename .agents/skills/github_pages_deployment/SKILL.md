---
name: github_pages_deployment
description: index.html などの静的ファイルを GitHub Pages で公開するための手順。SSH 接続による push と GitHub 設定を含みます。
---

# GitHub Pages 公開手順（SSH push 版）

このスキルは、ローカルの HTML ファイルを GitHub Pages で公開するための標準的な手順を提供します。

## 事前準備
- GitHub アカウント（例: `mach2005`）
- 公開用のリポジトリ名（例: `tokyo-mach`）
- SSH 鍵の設定が完了していること

## 手順

### 1. Git リポジトリの初期化
公開したいディレクトリで以下のコマンドを実行します。
```powershell
git init
```

### 2. ユーザー情報の構成 (未設定の場合のみ)
```powershell
git config --local user.name "Your Name"
git config --local user.email "your-email@example.com"
```

### 3. ファイルの追加とコミット
```powershell
git add .
git commit -m "Initial commit"
```

### 4. リモートリポジトリの設定
ブランチ名を `main` に変更し、SSH 形式の URL をリモートに追加します。
```powershell
git branch -M main
git remote add origin git@github.com:USERNAME/REPOSITORY.git
```
※ `USERNAME` と `REPOSITORY` は実際のものに置き換えてください。

### 5. GitHub への push
```powershell
git push -u origin main
```

### 6. GitHub Pages の有効化
push 完了後、GitHub のウェブサイトで以下の設定を行います：
1. リポジトリの **Settings** > **Pages** に移動。
2. **Build and deployment** > **Branch** で `main` を選択し、`/ (root)` を指定して **Save**。

## トラブルシューティング
- **"Repository not found" エラー**: GitHub 上にリポジトリが作成されているか確認してください。
- **SSH 認証エラー**: `ssh -T git@github.com` で接続が成功するか確認してください。
