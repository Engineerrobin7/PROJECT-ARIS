@echo off
echo ========================================
echo    ARIS Ultimate - Installation
echo ========================================
echo.
echo Installing all dependencies...
echo.

pip install -r requirements.txt

echo.
echo ========================================
echo Installation complete!
echo ========================================
echo.
echo You can now run ARIS Ultimate:
echo   1. start_ultimate.bat
echo   2. python gui_ultimate.py
echo   3. python aris_enhanced.py
echo.
echo To test everything:
echo   python test_all_ultimate_features.py
echo.
pause
