import os
from PIL import Image
from django.conf import settings

# Set the maximum allowed file size (600 KB)
MAX_FILE_SIZE_KB = 500
MEDIA_ROOT = settings.MEDIA_ROOT

def resize_image(image_path):
    """Resize an image to ensure it's under the 500KB size limit."""
    with Image.open(image_path) as img:
        img_format = img.format

        # Reduce quality incrementally until the file is under the limit
        quality = 95  # Start with high quality
        while os.path.getsize(image_path) / 1024 > MAX_FILE_SIZE_KB and quality > 10:
            img.save(image_path, format=img_format, quality=quality)
            quality -= 5

        print(f"Resized {image_path} to {os.path.getsize(image_path) / 1024:.2f} KB (Quality: {quality})")

def run():
    # Define the path to the stills directory
    stills_dir = 'd:/current/code/grand_v2_project/media/t/stills/'

    if not os.path.exists(stills_dir):
        print(f"Directory {stills_dir} does not exist.")
        return

    # Iterate through all .jpg files in the directory
    for filename in os.listdir(stills_dir):
        if filename.endswith('.jpg'):
            file_path = os.path.join(stills_dir, filename)

            # Check the file size
            file_size_kb = os.path.getsize(file_path) / 1024
            if file_size_kb > MAX_FILE_SIZE_KB:
                print(f"Resizing {filename} (Size: {file_size_kb:.2f} KB)")
                resize_image(file_path)
            else:
                print(f"{filename} is already under the 500KB limit ({file_size_kb:.2f} KB)")
