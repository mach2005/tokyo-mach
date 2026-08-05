---
name: data_update
description: 応援歌データや試合日程データを更新し、ウェブサイトに反映するための手順。データソースの場所と更新方法を定義。
---

# データ更新スキル

応援歌の歌詞・選手データ、試合日程データを更新し、ウェブサイトに反映するための手順です。

## データソースの場所

### 1. 応援歌データ（gen_songs.py 内）

**ファイル**: `C:\Users\user\Antigravity\東京真隼\develop\gen_songs.py`

このスクリプト内に以下のデータが直接定義されています:

| 変数名 | 内容 |
|--------|------|
| `PITCHERS` | 投手の背番号・名前・歌詞 |
| `PITCHERS_GEN` | 投手汎用応援歌 |
| `CATCHERS` | 捕手の背番号・名前・歌詞 |
| `INFIELDERS` | 内野手の背番号・名前・歌詞 |
| `OUTFIELDERS` | 外野手の背番号・名前・歌詞 |
| `FIELDERS_GEN` | 野手汎用応援歌 |
| `CHANCE` | チャンステーマ |
| `MULTI` | マルチテーマ |

#### データフォーマット
```
背番号 名前;歌詞（改行は半角スペースまたは全角スペースで区切り）
```

新選手の場合は先頭に `NEW!` を付けます:
```
NEW!49 松本 晴;鍛えたその腕を 自信持って振り抜き 揺るがぬ覚悟胸に 松本晴輝け
```

#### 音声ファイルのマッピング
`gen_songs.py` 内の `audio_map` で定義されています:
```python
audio_map = {
    "45": "../public/audio/45_tanigawara.aac",
    "49": "../public/audio/49_matsumoto_hare.m4a",
    "53": "../public/audio/53_oyama.m4a",
    "57": "../public/audio/57_ogata.m4a"
}
```
新しい音声ファイルを追加する場合:
1. 音声ファイルを `public/audio/` に配置
2. `audio_map` にエントリ追加

### 2. 試合日程データ

**ファイル**: `C:\Users\user\Antigravity\東京真隼\develop\data.txt`

#### TSV フォーマット
```
日付\t曜日\t対戦相手\t球場\t開始時刻
```

例:
```
3月7日	金	日本ハム	みずほPayPay	18:30
4月4日	土	ロッテ	ZOZOマリン	14:00
```

> [!IMPORTANT]
> `data.txt` を更新した後は、`build_pages.py` 内の `schedule_content` セクションを対応するよう手動で更新する必要があります。
> `build_pages.py` のカレンダーデータはハードコードされているため、`data.txt` と自動同期はされません。

### 3. FightSong（応援歌シート）データ

**ファイル**: 
- `C:\Users\user\Antigravity\東京真隼\FightSong\cheer-guide.html` — モバイル版
- `C:\Users\user\Antigravity\東京真隼\FightSong\digital-sheet.html` — デジタルシート
- `C:\Users\user\Antigravity\東京真隼\FightSong\print_ouenka_2026.html` — 印刷用HTML

これらは独立したHTMLファイルです。応援歌データを更新する場合は、各ファイルを直接編集してください。

## 更新手順

### 選手の追加・変更（自動化手順）

1. `develop/gen_songs.py` の対応するセクションでデータを追加・変更します。
2. 以下の「一括ビルド＆デプロイ」コマンドを実行して、関連するすべてのページを更新・公開します。

```powershell
# Songs ページを再生成
python develop/gen_songs.py
# 全ページをビルドし直し
python develop/build_pages.py
# Gitへプッシュ
git add .
git commit -m "Update: 選手名簿の更新とサイト再ビルド"
git push origin main
```

> [!TIP]
> 選手データが複数のファイル（FightSong 配下など）に跨る場合、AIは Python スクリプトを使用してそれらを一括で置換することを推奨します。

### 試合日程の更新（自動化手順）

1. `develop/data.txt` を更新
2. `develop/build_pages.py` の `schedule_content` セクションを更新
3. ページを再生成:
   ```powershell
   python develop/build_pages.py
   ```
4. コミット＆デプロイ

### PDF の更新

PDF はブラウザで HTML を開き、印刷機能で生成する方法が最も確実です:

1. `FightSong/digital-sheet.html` または `FightSong/print_ouenka_2026.html` を更新
2. ブラウザで開く
3. `Ctrl+P` > PDF として保存
4. 保存先: `FightSong/ouenka_2026.pdf` または `FightSong/print_ouenka_2026.pdf`

## 文字コードの注意

> [!CAUTION]
> すべてのファイル操作はPython (`encoding='utf-8'`) で行ってください。
> PowerShell の `Set-Content` / `Get-Content` は UTF-16LE になるため、文字化けの原因となります。
