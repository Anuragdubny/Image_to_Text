# 🚀 Deployment Guide - Image to Text Reader

## Quick Deploy (Recommended)

1. **Run the deployment script:**
   ```
   deploy.bat
   ```
   This will automatically build the executable.

2. **Find your app:**
   - Executable will be in `dist\ImageToTextReader.exe`
   - Double-click to run!

## Manual Deployment Options

### Option 1: PyInstaller (Recommended)
```bash
# Install PyInstaller
pip install pyinstaller

# Create executable
pyinstaller --onefile --windowed --name=ImageToTextReader image_to_text_reader.py

# Find executable in dist/ folder
```

### Option 2: cx_Freeze
```bash
# Install cx_Freeze
pip install cx-freeze

# Build executable
python build_exe.py build

# Find executable in build/ folder
```

## Distribution Package

### Create Installer (Advanced)
1. **Install NSIS (Nullsoft Scriptable Install System)**
   - Download from: https://nsis.sourceforge.io/

2. **Create installer script** (installer.nsi):
   ```nsis
   !define APP_NAME "Image to Text Reader"
   !define APP_VERSION "1.0"
   
   OutFile "ImageToTextReader_Setup.exe"
   InstallDir "$PROGRAMFILES\${APP_NAME}"
   
   Section "Install"
     SetOutPath $INSTDIR
     File "dist\ImageToTextReader.exe"
     CreateShortcut "$DESKTOP\${APP_NAME}.lnk" "$INSTDIR\ImageToTextReader.exe"
   SectionEnd
   ```

3. **Compile installer:**
   ```
   makensis installer.nsi
   ```

## Requirements for End Users

### Tesseract OCR Installation
Users need to install Tesseract OCR:
1. Download from: https://github.com/UB-Mannheim/tesseract/wiki
2. Install to default location
3. Add to system PATH (usually automatic)

### Alternative: Portable Version
Create a portable package with Tesseract included:
1. Download Tesseract portable
2. Include in app folder
3. Modify app to use local Tesseract path

## File Structure After Build
```
dist/
├── ImageToTextReader.exe    # Main executable
└── (dependencies included)

For distribution:
├── ImageToTextReader.exe
├── README.txt              # User instructions
└── tesseract-installer.exe # Optional bundled installer
```

## Testing Deployment
1. Test on clean Windows machine
2. Verify Tesseract detection works
3. Test with various image formats
4. Check all UI elements function properly

## Troubleshooting
- **"Module not found" errors**: Reinstall requirements
- **Tesseract not found**: Include installation instructions
- **Large file size**: Use `--exclude-module` for unused packages
- **Slow startup**: Consider using `--onedir` instead of `--onefile`