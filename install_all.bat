@echo off
REM ============================================
REM ARIS Complete Installation Script
REM ============================================

echo.
echo ============================================
echo   ARIS Installation Wizard
echo ============================================
echo.

REM Check Python installation
echo [1/5] Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.11+ from https://www.python.org/
    pause
    exit /b 1
)
echo Python found!
echo.

REM Create virtual environment (optional)
echo [2/5] Would you like to create a virtual environment? (Recommended)
set /p CREATE_VENV="Create venv? (y/n): "
if /i "%CREATE_VENV%"=="y" (
    echo Creating virtual environment...
    python -m venv venv
    call venv\Scripts\activate.bat
    echo Virtual environment created and activated!
) else (
    echo Skipping virtual environment...
)
echo.

REM Install dependencies
echo [3/5] Installing dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)
echo Dependencies installed successfully!
echo.

REM Create directories
echo [4/5] Creating required directories...
if not exist "logs" mkdir logs
if not exist "data" mkdir data
if not exist "config" mkdir config
echo Directories created!
echo.

REM Setup configuration
echo [5/5] Setting up configuration...
if not exist "config\config.env" (
    echo Creating default configuration file...
    copy .env.example config\config.env
    echo Configuration file created at config\config.env
    echo.
    echo IMPORTANT: Please edit config\config.env with your API keys
) else (
    echo Configuration file already exists.
)
echo.

REM Installation complete
echo ============================================
echo   Installation Complete!
echo ============================================
echo.
echo Next steps:
echo 1. Edit config\config.env with your API keys
echo 2. See API_SETUP_GUIDE.md for API setup instructions
echo 3. Run: python quick_start.py
echo 4. Or run: python gui_enhanced.py
echo.
echo Documentation:
echo - README.md - Main documentation
echo - FEATURES.md - Complete feature list
echo - USAGE_GUIDE.md - Usage instructions
echo - API_SETUP_GUIDE.md - API setup guide
echo.
pause
