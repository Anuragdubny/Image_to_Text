# Image to Text Reader Setup Instructions

## Prerequisites

1. **Install Python 3.7+** from https://python.org
2. **Install Tesseract OCR**:
   - Download from: https://github.com/UB-Mannheim/tesseract/wiki
   - Install to default location (usually `C:\Program Files\Tesseract-OCR`)
   - Add Tesseract to your system PATH

## Installation Steps

1. Open Command Prompt in the project folder
2. Install required packages:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

```
python image_to_text_reader.py
```

## Usage

1. Click "Select Image" to choose an image file
2. Click "Extract Text" to process the image
3. View extracted text in the text area
4. Click "Copy Text" to copy results to clipboard

## Supported Formats

- PNG, JPG, JPEG, BMP, TIFF, GIF

## Troubleshooting

If you get a "tesseract not found" error:
- Ensure Tesseract is installed
- Add this line after imports in the Python file:
  ```python
  pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
  ```