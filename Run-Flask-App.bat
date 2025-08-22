@echo off
setlocal
cd /d %~dp0
cd Excel_se_EMD
where python >nul 2>nul
if errorlevel 1 (
  echo Python not found. Please install Python 3.9+ and add to PATH.
  pause
  exit /b 1
)
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
set FLASK_APP=app.py
set FLASK_ENV=production
python app.py
endlocal

