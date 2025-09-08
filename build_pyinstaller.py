# PyInstaller build script
# Run: python build_pyinstaller.py

import PyInstaller.__main__
import os

# Get current directory
current_dir = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(current_dir, "icon.ico") if os.path.exists(os.path.join(current_dir, "icon.ico")) else None

# PyInstaller arguments
args = [
    'image_to_text_reader.py',
    '--onefile',
    '--windowed',
    '--name=ImageToTextReader',
    '--distpath=dist',
    '--workpath=build',
    '--specpath=.',
]

# Add icon if exists
if icon_path:
    args.append(f'--icon={icon_path}')

# Run PyInstaller
PyInstaller.__main__.run(args)