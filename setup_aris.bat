@echo off

:: Check for admin privileges
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo This setup requires administrator privileges.
    echo Please right-click on setup_aris.bat and select "Run as administrator".
    echo.
    pause
    exit
)

echo ===================================
echo ARIS Voice Assistant Setup
echo ===================================
echo.

echo Installing required Python packages...
pip install -r requirements.txt

echo.
echo Creating desktop shortcut...
powershell -ExecutionPolicy Bypass -File create_shortcut.ps1

echo.
echo Setup complete!
echo You can now start ARIS by:
echo 1. Double-clicking the desktop shortcut
echo 2. Double-clicking start_aris.bat in the project folder
echo.
echo When ARIS is running, say "wake up aris" to activate the assistant.
echo.
pause