from PIL import Image, ImageDraw, ImageFont
import os

def create_app_icon():
    # Create a 256x256 image with transparent background
    size = 256
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Background circle
    margin = 20
    draw.ellipse([margin, margin, size-margin, size-margin], 
                fill=(52, 152, 219, 255), outline=(41, 128, 185, 255), width=4)
    
    # Document icon (rectangle)
    doc_x, doc_y = 60, 50
    doc_w, doc_h = 80, 100
    draw.rectangle([doc_x, doc_y, doc_x+doc_w, doc_y+doc_h], 
                  fill=(255, 255, 255, 255), outline=(149, 165, 166, 255), width=2)
    
    # Folded corner
    corner_size = 15
    draw.polygon([(doc_x+doc_w-corner_size, doc_y), 
                  (doc_x+doc_w, doc_y+corner_size),
                  (doc_x+doc_w-corner_size, doc_y+corner_size)], 
                 fill=(236, 240, 241, 255))
    
    # Text lines on document
    line_y = doc_y + 20
    for i in range(4):
        draw.rectangle([doc_x+10, line_y, doc_x+doc_w-15, line_y+3], 
                      fill=(52, 73, 94, 255))
        line_y += 12
    
    # Camera/eye icon for OCR
    eye_x, eye_y = 150, 160
    eye_w, eye_h = 60, 35
    draw.ellipse([eye_x, eye_y, eye_x+eye_w, eye_y+eye_h], 
                fill=(231, 76, 60, 255), outline=(192, 57, 43, 255), width=2)
    
    # Eye pupil
    pupil_x = eye_x + eye_w//2 - 8
    pupil_y = eye_y + eye_h//2 - 8
    draw.ellipse([pupil_x, pupil_y, pupil_x+16, pupil_y+16], 
                fill=(255, 255, 255, 255))
    
    # Arrow from document to eye
    arrow_start_x = doc_x + doc_w + 5
    arrow_start_y = doc_y + doc_h//2
    arrow_end_x = eye_x - 5
    arrow_end_y = eye_y + eye_h//2
    
    draw.line([(arrow_start_x, arrow_start_y), (arrow_end_x, arrow_end_y)], 
              fill=(46, 204, 113, 255), width=4)
    
    # Arrow head
    draw.polygon([(arrow_end_x, arrow_end_y-5), 
                  (arrow_end_x-10, arrow_end_y),
                  (arrow_end_x, arrow_end_y+5)], 
                 fill=(46, 204, 113, 255))
    
    return img

# Create icon in multiple sizes
icon_img = create_app_icon()

# Save as ICO file with multiple sizes
sizes = [16, 32, 48, 64, 128, 256]
icon_images = []

for size in sizes:
    resized = icon_img.resize((size, size), Image.Resampling.LANCZOS)
    icon_images.append(resized)

# Save as .ico file
icon_images[0].save('app_icon.ico', format='ICO', sizes=[(img.width, img.height) for img in icon_images])

# Also save as PNG for preview
icon_img.save('app_icon.png', format='PNG')

print("Icon created: app_icon.ico and app_icon.png")