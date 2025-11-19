import os
from PIL import Image
from django.conf import settings
from grand_v2_app.models import Media, Page

def get_image_height(image_path):
    """Returns the height of the image."""
    try:
        with Image.open(image_path) as img:
            return img.height
    except Exception as e:
        print(f"Error opening {image_path}: {e}")
        return None

def run():
    try:
        # Retrieve the 'stills' page
        page_stills = Page.objects.get(name='stills')

        # Get all media items associated with the 'stills' page
        media_items = Media.objects.filter(page=page_stills)

        # Define the correct path to the media directory (grand_v2_project/media/stills)
        MEDIA_DIR = os.path.join(settings.MEDIA_ROOT, 'stills')

        # Create a list of tuples (media_item, image_height, image_path)
        media_with_height = []
        for media_item in media_items:
            image_path = os.path.join(MEDIA_DIR, f"{media_item.path}.jpg")  # Ensure full path to image
            image_height = get_image_height(image_path)
            if image_height:
                media_with_height.append((media_item, image_height, image_path))

        # Sort the media items by image height (ascending)
        media_with_height.sort(key=lambda x: x[1])

        # Rename files and update the database
        for index, (media_item, height, old_image_path) in enumerate(media_with_height):
            # Create the new filename and path based on the sorted order
            new_filename = f"image_{index+1}.jpg"  # Rename files in order like image_1.jpg, image_2.jpg, etc.
            new_image_path = os.path.join(MEDIA_DIR, new_filename)

            # Rename the file physically
            os.rename(old_image_path, new_image_path)

            # Update the Media model with the new path
            media_item.path = f"stills/{new_filename}".replace(".jpg", "")  # Update path without .jpg extension
            media_item.save()

            print(f"Updated {media_item.title}: {old_image_path} -> {new_image_path}")

        print("Sorting complete, files renamed, and database updated.")

    except Page.DoesNotExist:
        print("No page with name 'stills' found.")
    except Exception as e:
        print(f"An error occurred: {e}")
