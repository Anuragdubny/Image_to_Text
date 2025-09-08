@echo off
echo Creating distribution package...

mkdir "ImageToTextReader_v1.0" 2>nul
copy "dist\ImageToTextReader.exe" "ImageToTextReader_v1.0\"
copy "README_DEPLOYMENT.txt" "ImageToTextReader_v1.0\README.txt"

echo.
echo Creating user instructions...
echo # Image to Text Reader - User Guide > "ImageToTextReader_v1.0\USER_GUIDE.txt"
echo. >> "ImageToTextReader_v1.0\USER_GUIDE.txt"
echo ## Quick Start: >> "ImageToTextReader_v1.0\USER_GUIDE.txt"
echo 1. Install Tesseract OCR from: https://github.com/UB-Mannheim/tesseract/wiki >> "ImageToTextReader_v1.0\USER_GUIDE.txt"
echo 2. Double-click ImageToTextReader.exe >> "ImageToTextReader_v1.0\USER_GUIDE.txt"
echo 3. Click 'Select Image' to choose your image file >> "ImageToTextReader_v1.0\USER_GUIDE.txt"
echo 4. Click 'Extract Text' to convert image to text >> "ImageToTextReader_v1.0\USER_GUIDE.txt"
echo 5. Copy the extracted text to clipboard >> "ImageToTextReader_v1.0\USER_GUIDE.txt"
echo. >> "ImageToTextReader_v1.0\USER_GUIDE.txt"
echo ## Supported Formats: >> "ImageToTextReader_v1.0\USER_GUIDE.txt"
echo PNG, JPG, JPEG, BMP, TIFF, GIF >> "ImageToTextReader_v1.0\USER_GUIDE.txt"

echo.
echo ✅ Distribution package created: ImageToTextReader_v1.0\
echo.
echo Opening folder...
explorer "ImageToTextReader_v1.0"

echo.
echo 📦 Ready for distribution!
pause