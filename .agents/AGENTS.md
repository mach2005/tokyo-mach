# 東京真隼（TOKYO MACH）プロジェクト開発ルール

## 1. 文字コードの絶対ルール (UTF-8 厳守)
- **PowerShellの操作禁止**: PowerShellの `Set-Content`, `Get-Content`, `>`, `>>` は UTF-16LE に変換され文字化けを引き起こすため、絶対に使用しないこと。
- **編集ツールの限定**: ファイルの書き換えは必ず AI専用編集ツール（`replace_file_content` 等）または Python (`open(..., encoding='utf-8')`) で行うこと。

## 2. データ更新とビルド同期
- 選手データ変更時は、`develop/gen_songs.py` の更新とともに `HP/songs.html` や FightSong 配下のHTMLも同期・置換すること。
- 試合日程データ変更時は、`develop/data.txt` の更新に加え、`develop/build_pages.py` の `schedule_content` も同期させること。

## 3. デザイン・表示検証
- モバイル表示最適化の際、既存の文字情報やロゴを無断で非表示（`display: none` 等）にしないこと。
- スケジュールナビゲーションの矢印は「黒カプセル型（ピル形状）」を維持すること。
- 変更後はローカル表示確認およびリンク整合性のチェックを実施すること。
