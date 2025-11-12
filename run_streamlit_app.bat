@echo off
title PWD Tools - Streamlit App Launcher
echo ========================================
echo    PWD Tools - Streamlit App Launcher
echo ========================================
echo.
echo This will start the PWD Tools application
echo Please wait while we set up the environment...
echo.

echo Starting PWD Tools application...
echo The app will open in your default web browser
echo.
echo To stop the app, press Ctrl+C in this window
echo.

pwd_tools_env\Scripts\python.exe -m streamlit run streamlit_app.py

pause