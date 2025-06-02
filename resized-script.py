from PIL import Image
import os

# === Settings ===
input_folder = '...'       # Folder with original images
output_folder = '...'           # Folder to save resized images
target_size = (850, 567)                    # (width, height)

os.makedirs(output_folder, exist_ok=True)

# === Process images ===
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.webp')):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        with Image.open(input_path) as img:
            resized_img = img.resize(target_size, Image.LANCZOS)
            resized_img.save(output_path)

        print(f"Resized: {filename} → {target_size}")

print("✅ All images resized.")