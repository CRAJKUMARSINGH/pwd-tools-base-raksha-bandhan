@echo off
title PWD Tools Genspark - Launcher
echo ========================================
echo    PWD Tools Genspark - Launcher
echo ========================================
echo.
echo This will start the PWD Tools Genspark application
echo Please wait while we set up the environment...
echo.

cd /d "%~dp0"

echo Installing required packages...
pip install -r requirements.txt

echo.
echo Starting PWD Tools Genspark application...
echo The app will open in your default web browser
echo.
echo To stop the app, press Ctrl+C in this window
echo.
pause

streamlit run app.py

pause