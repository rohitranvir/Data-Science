@echo off
echo Installing Job Monitoring Bot...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed!
    echo Download from: https://www.python.org/downloads/
    pause
    exit /b 1
)

REM Install required packages
pip install requests schedule

echo.
echo Setup complete!
echo.
echo IMPORTANT NEXT STEPS:
echo 1. Open job_bot.py in a text editor
echo 2. Change email settings at the top of the file
echo 3. Run: python job_bot.py
echo.
pause