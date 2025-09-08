@echo off
echo ========================================
echo   Image to Text Reader - Deployment
echo ========================================
echo.

echo Installing required packages...
pip install pyinstaller cx-freeze

echo.
echo Building executable with PyInstaller...
python -m PyInstaller --onefile --windowed --name=ImageToTextReader image_to_text_reader.py

if exist "dist\ImageToTextReader.exe" (
    echo.
    echo ✅ Build successful!
    echo Executable created: dist\ImageToTextReader.exe
    echo.
    echo Opening dist folder...
    explorer dist
) else (
    echo.
    echo ❌ Build failed. Check for errors above.
)

echo.
pause