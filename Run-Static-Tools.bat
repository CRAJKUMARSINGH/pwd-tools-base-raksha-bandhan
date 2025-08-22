@echo off
setlocal
cd /d %~dp0
where python >nul 2>nul
if errorlevel 1 (
  echo Python not found. Please install Python 3.9+ and add to PATH.
  pause
  exit /b 1
)
python -m http.server 5500 -d public
endlocal

