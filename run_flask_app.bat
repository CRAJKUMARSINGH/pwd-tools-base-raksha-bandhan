@echo off
title PWD Tools - Flask App Launcher
echo ========================================
echo    PWD Tools - Flask App Launcher
echo ========================================
echo.
echo This will start the PWD Tools Flask application
echo Please wait while we set up the environment...
echo.

cd /d "%~dp0Excel_se_EMD"

echo Installing required packages...
pip install -r requirements.txt

echo.
echo Starting PWD Tools Flask application...
echo The app will be available at: http://localhost:5000
echo.
echo To stop the app, press Ctrl+C in this window
echo.
pause

python app.py

pause
