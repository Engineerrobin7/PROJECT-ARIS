@echo off
echo ========================================
echo    ARIS Ultimate Launcher
echo ========================================
echo.
echo Choose your interface:
echo.
echo 1. Ultimate GUI (Recommended)
echo 2. Enhanced Voice Mode
echo 3. Web Dashboard
echo 4. Exit
echo.
set /p choice="Enter your choice (1-4): "

if "%choice%"=="1" (
    echo.
    echo Starting Ultimate GUI...
    python gui_ultimate.py
) else if "%choice%"=="2" (
    echo.
    echo Starting Enhanced Voice Mode...
    python aris_enhanced.py
) else if "%choice%"=="3" (
    echo.
    echo Starting Web Dashboard...
    echo Open your browser to http://localhost:5000
    python web_dashboard/app.py
) else if "%choice%"=="4" (
    echo.
    echo Goodbye!
    exit
) else (
    echo.
    echo Invalid choice. Please run again.
    pause
)
