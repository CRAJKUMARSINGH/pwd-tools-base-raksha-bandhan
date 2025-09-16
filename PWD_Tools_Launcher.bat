@echo off
title PWD Tools - Main Launcher
color 0A
cls

:menu
echo.
echo  ╔══════════════════════════════════════════════════════════════╗
echo  ║                    PWD TOOLS - RAKSHA BANDHAN               ║
echo  ║                                                              ║
echo  ║                    Choose your application:                  ║
echo  ║                                                              ║
echo  ║    1. Streamlit App (Recommended - Modern Interface)        ║
echo  ║    2. Flask App (Traditional Web Interface)                 ║
echo  ║    3. Open Tools Folder                                      ║
echo  ║    4. Exit                                                   ║
echo  ║                                                              ║
echo  ╚══════════════════════════════════════════════════════════════╝
echo.
set /p choice="Enter your choice (1-4): "

if "%choice%"=="1" goto streamlit
if "%choice%"=="2" goto flask
if "%choice%"=="3" goto tools
if "%choice%"=="4" goto exit
echo Invalid choice. Please try again.
goto menu

:streamlit
cls
echo Starting Streamlit App...
echo.
call "%~dp0run_streamlit_app.bat"
goto menu

:flask
cls
echo Starting Flask App...
echo.
call "%~dp0run_flask_app.bat"
goto menu

:tools
cls
echo Opening Tools Folder...
start "" "%~dp0public\tools"
goto menu

:exit
echo Thank you for using PWD Tools!
pause
exit
