from PIL import Image
import os

# Define paths
source_image_path = r"h:\Electron_React_boilerplate\morse-translator\assets\icon.png"
output_dir = r"h:\Electron_React_boilerplate\morse-translator\assets\generated_icons"

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

# Define sizes for PNG icons
sizes = [16, 24, 32, 48, 64, 96, 128, 256, 512, 1024]

# Generate resized PNG icons
def generate_png_icons():
    with Image.open(source_image_path) as img:
        for size in sizes:
            resized_img = img.resize((size, size), Image.Resampling.LANCZOS)
            resized_img.save(os.path.join(output_dir, f"{size}x{size}.png"))

# Generate .ico file
def generate_ico():
    with Image.open(source_image_path) as img:
        img.save(os.path.join(output_dir, "icon.ico"), format="ICO", sizes=[(size, size) for size in sizes if size <= 256])

# Main function
if __name__ == "__main__":
    generate_png_icons()
    generate_ico()
    print(f"Icons generated in: {output_dir}")
