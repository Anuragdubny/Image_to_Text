import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, ttk
import os
import sys

try:
    from PIL import Image, ImageTk
    import pytesseract
except ImportError as e:
    print(f"Missing required module: {e}")
    print("Please install: pip install pillow pytesseract")
    sys.exit(1)

# Configure Tesseract path for Windows
possible_paths = [
    r'C:\Program Files\Tesseract-OCR\tesseract.exe',
    r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
]

for path in possible_paths:
    if os.path.exists(path):
        pytesseract.pytesseract.tesseract_cmd = path
        break

def test_tesseract():
    try:
        pytesseract.get_tesseract_version()
        return True
    except:
        return False

class ImageToTextReader:
    def __init__(self, root):
        self.root = root
        self.root.title("📖 Image to Text Reader")
        self.root.geometry("1000x700")
        self.root.configure(bg='#f0f0f0')
        
        # Set window icon
        try:
            if getattr(sys, 'frozen', False):
                # Running as executable
                icon_path = os.path.join(sys._MEIPASS, 'app_icon.ico')
            else:
                # Running as script
                icon_path = 'app_icon.ico'
            self.root.iconbitmap(icon_path)
        except:
            pass  # Icon file not found, continue without icon
        
        if not test_tesseract():
            messagebox.showerror("Tesseract Not Found", 
                               "Tesseract OCR is not installed.\n\n"
                               "Download from: https://github.com/UB-Mannheim/tesseract/wiki")
        
        self.create_widgets()
        
    def create_widgets(self):
        # Header
        header = tk.Frame(self.root, bg='#2c3e50', height=60)
        header.pack(fill='x')
        header.pack_propagate(False)
        
        title = tk.Label(header, text="📖 Image to Text Reader", 
                        font=("Segoe UI", 18, "bold"), fg="white", bg='#2c3e50')
        title.pack(expand=True)
        
        # Main container
        main = tk.Frame(self.root, bg='#f0f0f0')
        main.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Left side - Image preview
        left = tk.Frame(main, bg='white', relief='solid', bd=1, width=400)
        left.pack(side='left', fill='both', padx=(0, 10))
        left.pack_propagate(False)
        
        img_header = tk.Label(left, text="🖼️ Image Preview", 
                             font=("Segoe UI", 12, "bold"), bg='#ecf0f1', pady=10)
        img_header.pack(fill='x')
        
        self.img_canvas = tk.Canvas(left, bg='#f8f9fa', highlightthickness=0)
        self.img_canvas.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Default message
        self.img_canvas.create_text(200, 250, text="No image selected\n\n📁 Click 'Select Image' to choose a file", 
                                   font=("Segoe UI", 11), fill="#6c757d", justify='center')
        
        # Right side - Controls and text
        right = tk.Frame(main, bg='#f0f0f0')
        right.pack(side='right', fill='both', expand=True)
        
        # Controls
        controls = tk.Frame(right, bg='white', relief='solid', bd=1)
        controls.pack(fill='x', pady=(0, 10))
        
        btn_frame = tk.Frame(controls, bg='white')
        btn_frame.pack(pady=15, padx=20)
        
        select_btn = tk.Button(btn_frame, text="📁 Select Image", command=self.select_image,
                              bg="#3498db", fg="white", font=("Segoe UI", 11, "bold"),
                              padx=20, pady=8, relief='flat', cursor='hand2')
        select_btn.pack(side='left')
        
        self.extract_btn = tk.Button(btn_frame, text="🔍 Extract Text", command=self.extract_text,
                                    bg="#27ae60", fg="white", font=("Segoe UI", 11, "bold"),
                                    padx=20, pady=8, relief='flat', cursor='hand2', state="disabled")
        self.extract_btn.pack(side='left', padx=(10, 0))
        
        self.file_label = tk.Label(controls, text="No file selected", 
                                  font=("Segoe UI", 10), fg="#6c757d", bg='white')
        self.file_label.pack(pady=(0, 15))
        
        # Progress bar
        self.progress = ttk.Progressbar(controls, mode='indeterminate')
        self.progress.pack(fill='x', padx=20, pady=(0, 15))
        
        # Text area
        text_frame = tk.Frame(right, bg='white', relief='solid', bd=1)
        text_frame.pack(fill='both', expand=True)
        
        text_header = tk.Frame(text_frame, bg='#ecf0f1')
        text_header.pack(fill='x')
        
        tk.Label(text_header, text="📄 Extracted Text", 
                font=("Segoe UI", 12, "bold"), bg='#ecf0f1', pady=10).pack(side='left', padx=20)
        
        btn_group = tk.Frame(text_header, bg='#ecf0f1')
        btn_group.pack(side='right', padx=20, pady=5)
        
        tk.Button(btn_group, text="📋 Copy", command=self.copy_text,
                 bg="#e67e22", fg="white", font=("Segoe UI", 9, "bold"),
                 padx=12, pady=4, relief='flat', cursor='hand2').pack(side='right', padx=(5, 0))
        
        tk.Button(btn_group, text="🗑️ Clear", command=self.clear_text,
                 bg="#e74c3c", fg="white", font=("Segoe UI", 9, "bold"),
                 padx=12, pady=4, relief='flat', cursor='hand2').pack(side='right')
        
        self.text_area = scrolledtext.ScrolledText(text_frame, wrap=tk.WORD, 
                                                  font=("Consolas", 10), bg='#fafafa')
        self.text_area.pack(fill='both', expand=True, padx=15, pady=(0, 15))
        
    def select_image(self):
        file_types = [
            ("Image files", "*.png *.jpg *.jpeg *.bmp *.tiff *.gif"),
            ("All files", "*.*")
        ]
        
        self.image_path = filedialog.askopenfilename(
            title="Select an image file",
            filetypes=file_types
        )
        
        if self.image_path:
            filename = os.path.basename(self.image_path)
            self.file_label.config(text=f"Selected: {filename}")
            self.extract_btn.config(state="normal")
            self.display_image()
    
    def display_image(self):
        try:
            # Clear canvas
            self.img_canvas.delete("all")
            
            # Open and resize image
            img = Image.open(self.image_path)
            canvas_width = self.img_canvas.winfo_width() or 380
            canvas_height = self.img_canvas.winfo_height() or 500
            
            # Calculate size to fit canvas
            img_width, img_height = img.size
            if img_width > canvas_width or img_height > canvas_height:
                ratio = min(canvas_width/img_width, canvas_height/img_height)
                new_width = int(img_width * ratio)
                new_height = int(img_height * ratio)
                img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
            
            # Convert to PhotoImage
            self.photo = ImageTk.PhotoImage(img)
            
            # Center image on canvas
            x = canvas_width // 2
            y = canvas_height // 2
            self.img_canvas.create_image(x, y, image=self.photo)
            
        except Exception as e:
            self.img_canvas.delete("all")
            self.img_canvas.create_text(200, 250, text=f"❌ Cannot preview image\n{str(e)[:50]}...", 
                                       font=("Segoe UI", 10), fill="#e74c3c", justify='center')
    
    def extract_text(self):
        if not hasattr(self, 'image_path') or not self.image_path:
            messagebox.showerror("Error", "Please select an image first")
            return
            
        try:
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, "🔄 Processing image...")
            self.progress.start(10)
            self.extract_btn.config(state="disabled")
            self.root.update()
            
            image = Image.open(self.image_path)
            extracted_text = pytesseract.image_to_string(image)
            
            self.progress.stop()
            self.extract_btn.config(state="normal")
            
            self.text_area.delete(1.0, tk.END)
            if extracted_text.strip():
                self.text_area.insert(tk.END, extracted_text)
                messagebox.showinfo("✅ Success", "Text extracted successfully!")
            else:
                self.text_area.insert(tk.END, "❌ No text found in the image.")
                
        except Exception as e:
            self.progress.stop()
            self.extract_btn.config(state="normal")
            error_msg = str(e)
            if "tesseract" in error_msg.lower():
                error_msg = "Tesseract OCR not found. Please install from:\nhttps://github.com/UB-Mannheim/tesseract/wiki"
            messagebox.showerror("❌ Error", f"Failed to extract text:\n{error_msg}")
            self.text_area.delete(1.0, tk.END)
            
    def copy_text(self):
        text = self.text_area.get(1.0, tk.END).strip()
        if text and text != "❌ No text found in the image.":
            self.root.clipboard_clear()
            self.root.clipboard_append(text)
            messagebox.showinfo("✅ Success", "Text copied to clipboard!")
        else:
            messagebox.showwarning("⚠️ Warning", "No text to copy")
    
    def clear_text(self):
        self.text_area.delete(1.0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageToTextReader(root)
    root.mainloop()