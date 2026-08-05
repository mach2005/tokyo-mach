---
name: website_build_and_deploy
description: 東京真隼ウェブサイトの全ページ生成（HP・応援歌）とGitHub Pagesへのデプロイを一括自動実行するスキル。
---

# 東京真隼ウェブサイト ビルド＆デプロイ

このスキルは、東京真隼プロジェクトの全ウェブページ生成からGitHub Pagesへのデプロイまでを一括で実行します。

## プロジェクト構造

```
C:\Users\user\Antigravity\東京真隼\
├── index.html              ← ルートリダイレクト（portal/index.htmlへ）
├── portal/index.html       ← ポータルサイト（全コンテンツへのハブ）
├── HP/                     ← 公式サイト（index, schedule, songs, faq, gallery）
│   ├── index.html
│   ├── schedule.html
│   ├── songs.html
│   ├── faq.html
│   └── gallery.html
├── FightSong/              ← 応援歌サイト（モバイル・デジタル・印刷版）
│   ├── cheer-guide.html
│   ├── digital-sheet.html
│   ├── print-sheet.html
│   ├── print_ouenka_2026.html
│   ├── ouenka_2026.pdf
│   └── print_ouenka_2026.pdf
├── public/                 ← 共有アセット（CSS、音声、favicon）
│   ├── style.css
│   ├── favicon.svg
│   └── audio/
├── develop/                ← ビルドスクリプト・データファイル
│   ├── build_pages.py      ← HP配下の schedule/songs/faq/gallery を生成
│   ├── gen_songs.py        ← HP/songs.html を応援歌データから再生成
│   ├── data.txt            ← 試合日程データ（TSV形式）
│   ├── server.py           ← ローカル開発用サーバー (port 3000)
│   └── ...
└── history/                ← 過去バージョンのアーカイブ
```

## GitHub 情報

- **リポジトリ**: `git@github.com:mach2005/tokyo-mach.git`
- **ブランチ**: `main`
- **Git ユーザー名**: `Tokyo Mach Admin`
- **Git メール**: `tokyo.mach@example.com`
- **GitHub Pages URL**: `https://mach2005.github.io/tokyo-mach/`

## 公開URL一覧

| ページ | URL |
|--------|-----|
| ポータル | https://mach2005.github.io/tokyo-mach/portal/index.html |
| 公式サイト | https://mach2005.github.io/tokyo-mach/HP/index.html |
| 試合日程 | https://mach2005.github.io/tokyo-mach/HP/schedule.html |
| 応援歌 (HP版) | https://mach2005.github.io/tokyo-mach/HP/songs.html |
| Q&A | https://mach2005.github.io/tokyo-mach/HP/faq.html |
| ギャラリー | https://mach2005.github.io/tokyo-mach/HP/gallery.html |
| モバイル応援ガイド | https://mach2005.github.io/tokyo-mach/FightSong/cheer-guide.html |
| デジタルシート | https://mach2005.github.io/tokyo-mach/FightSong/digital-sheet.html |
| 応援歌PDF | https://mach2005.github.io/tokyo-mach/FightSong/ouenka_2026.pdf |
| 印刷用PDF | https://mach2005.github.io/tokyo-mach/FightSong/print_ouenka_2026.pdf |

## 実行手順（完全自動化：ゼロタッチ運用）

> [!TIP]
> 文中のすべてのステップは自動実行（SafeToAutoRun: true）を前提としています。
> AIが自律的に作業を完遂するため、ユーザーの「Run」や「Accept」ボタンの待機を排除します。

### Step 1: HPページの生成（schedule, songs, faq, gallery）

```powershell
python develop/build_pages.py
```

### Step 2: 応援歌ページの生成（HP/songs.html）

```powershell
python develop/gen_songs.py
```

### Step 3: Git ステージング・コミット・デプロイ

```powershell
git add .
git status
git commit -m "Update: Automatic Rebuild and Deploy"
git push origin main
```

### Step 4: ローカル検証（npx serve + Browser Subagent）

プッシュ前、またはプッシュ後に表示を確認するために、ローカルHTTPサーバーを立ち上げてブラウザ検証を実施します。

```powershell
# ローカルサーバー起動（ポート 3000）
npx serve .
```

**AIへの指示:**
1. `browser_subagent` を使用し、`http://localhost:3000/HP/index.html` および `schedule.html` を開く。
2. SNSセクションのレイアウト（Twitterが右側に正しく表示されているか）を確認。
3. スケジュールのナビゲーション矢印が「黒いカプセル型」であることを視認。

## GitHub Pagesの復旧（公開設定変更時）

リポジトリを一時的に「Private」にすると、GitHub Pagesの設定が解除されます。サイトが404になった場合は、以下の手順で復旧してください。

1. GitHub リポジトリ（`mach2005/tokyo-mach`）の **Settings > Pages** を開く。
2. **Build and deployment > Branch** で `main` を選択し、**Save** をクリック。
3. 数分待つとデプロイ（再構築）が完了し、サイトがオンラインに戻ります。

## 文字コードに関する注意事項
... (以降、既存の文字コードセクション)


> [!CAUTION]
> **絶対に PowerShell の `Set-Content`, `Get-Content`, `>`, `Out-File` でHTMLファイルを直接編集しないでください。**
> Windows PowerShell はデフォルトで UTF-16LE を使用するため、UTF-8 のHTMLファイルが文字化け（Mojibake）します。

### ✅ 安全なファイル編集方法（優先順位順）

1. **AIのファイル編集ツール**（最優先）: `replace_file_content`, `multi_replace_file_content`
2. **Python**（使える場合）: `open(path, 'w', encoding='utf-8')`
3. **PowerShell System.IO**（Pythonが使えない場合）:
```powershell
$enc = [System.Text.Encoding]::UTF8
$c = [System.IO.File]::ReadAllText($path, $enc)
$c = $c.Replace("旧テキスト", "新テキスト")
[System.IO.File]::WriteAllText($path, $c, $enc)
```

> [!NOTE]
> 微修正（テキスト置換レベル）は **`/quick-fix-deploy`ワークフロー** を使うと最速。Pythonビルドは不要。

## トラブルシューティング

### 文字化けが発生した場合

Git の履歴から正常なファイルを復元します。正常だったコミットは `d84f3e9` です。

```powershell
# 特定コミットからファイルを復元
git show d84f3e9:HP/index.html > HP/index.html
git show d84f3e9:HP/schedule.html > HP/schedule.html
```

> [!WARNING]
> 上記の `>` リダイレクトも PowerShell では文字化けするため、Python で復元してください:
> ```powershell
> python -c "import subprocess,os; data=subprocess.run(['git','show','d84f3e9:HP/index.html'],capture_output=True).stdout; open('HP/index.html','wb').write(data)"
> ```

### リンクが壊れている場合

ポータル (`portal/index.html`) のリンクパスを確認:
- HP配下: `../HP/index.html` (相対パス)
- FightSong配下: `../FightSong/xxx` (相対パス)
- モバイル応援ガイド: 絶対URL `https://mach2005.github.io/tokyo-mach/FightSong/cheer-guide.html`

HP配下のサブページの共通CSS:
- パス: `../public/style.css` (HPフォルダからの相対パス)
