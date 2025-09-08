@echo off
echo Starting Image to Text Reader...
python image_to_text_reader.py
if %errorlevel% neq 0 (
    echo.
    echo Error occurred. Press any key to exit...
    pause >nul
)