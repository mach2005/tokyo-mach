@echo off
REM === 東京真隼 試合結果0時自動更新 セットアップ ===
REM このバッチを管理者権限で1回実行すると、毎日0:00にタスクが登録されます

set SCRIPT_DIR=%~dp0
set PYTHON_PATH=python
set SCRIPT_PATH=%SCRIPT_DIR%update_game_result.py

REM タスクスケジューラに登録（既存があれば上書き）
schtasks /create /tn "TokyoMach_GameResultUpdate" /tr "\"%PYTHON_PATH%\" \"%SCRIPT_PATH%\"" /sc daily /st 00:00 /f

if %ERRORLEVEL% == 0 (
    echo [OK] タスク "TokyoMach_GameResultUpdate" を毎日0:00に登録しました
) else (
    echo [ERROR] タスク登録に失敗しました。管理者権限で再実行してください。
)

pause
