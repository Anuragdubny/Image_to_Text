import sys
import os
from cx_Freeze import setup, Executable

# Dependencies
build_exe_options = {
    "packages": ["tkinter", "PIL", "pytesseract", "os", "sys"],
    "excludes": ["unittest"],
    "include_files": [
        ("app_icon.ico", "app_icon.ico"),  # Include icon file
    ],
    "zip_include_packages": ["encodings", "PySide6"],
}

# GUI applications require a different base on Windows
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="ImageToTextReader",
    version="1.0",
    description="Convert images to text using OCR",
    options={"build_exe": build_exe_options},
    executables=[Executable("image_to_text_reader.py", base=base, target_name="ImageToTextReader.exe", icon="app_icon.ico")]
)