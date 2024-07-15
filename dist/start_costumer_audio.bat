@echo off
echo Starting MP3 Player... >> mp3_player_log.txt
echo %date% %time% >> mp3_player_log.txt
"%~dp0mp3_player.exe" "%~dp0Customer.mp3" >> mp3_player_log.txt 2>&1
if %errorlevel% neq 0 (
    echo Error occurred. Error level: %errorlevel% >> mp3_player_log.txt
) else (
    echo MP3 Player started successfully >> mp3_player_log.txt
)
