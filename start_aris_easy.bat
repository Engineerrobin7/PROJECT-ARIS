@echo off
REM Easy ARIS Launcher - Choose your mode

:menu
cls
echo.
echo ============================================================
echo   ARIS - Your AI Assistant
echo ============================================================
echo.
echo Choose how to run ARIS:
echo.
echo   1. JARVIS Interface (Advanced - RECOMMENDED)
echo   2. JARVIS Classic (Futuristic design)
echo   3. Text Mode (Simple, type commands)
echo   4. Standard GUI (Original interface)
echo   5. Voice Mode (Always listening)
echo   6. Test Voice Recognition
echo   7. Exit
echo.
set /p choice="Enter your choice (1-7): "

if "%choice%"=="1" goto jarvisadvanced
if "%choice%"=="2" goto jarvisclassic
if "%choice%"=="3" goto textmode
if "%choice%"=="4" goto guimode
if "%choice%"=="5" goto voicemode
if "%choice%"=="6" goto testvoice
if "%choice%"=="7" goto end
goto menu

:jarvisadvanced
cls
echo.
echo Starting JARVIS Advanced Interface...
echo Full JARVIS experience with animations and effects!
echo.
python jarvis_advanced.py
pause
goto menu

:jarvisclassic
cls
echo.
echo Starting JARVIS Classic Interface...
echo Futuristic design with glowing effects!
echo.
python jarvis_gui.py
pause
goto menu

:textmode
cls
echo.
echo Starting ARIS in Text Mode...
echo Type your commands and press Enter.
echo.
python gui_text_mode.py
pause
goto menu

:guimode
cls
echo.
echo Starting ARIS GUI...
echo A window will open. You can type or use the voice button.
echo.
python gui_enhanced.py
pause
goto menu

:voicemode
cls
echo.
echo Starting ARIS Voice Mode...
echo Say "wake up aris" to activate, then speak your command.
echo Press Ctrl+C to exit.
echo.
python main.py
pause
goto menu

:testvoice
cls
echo.
echo Testing Voice Recognition...
echo Speak when prompted to test if your microphone works.
echo.
python test_voice_simple.py
pause
goto menu

:end
echo.
echo Goodbye!
echo.
