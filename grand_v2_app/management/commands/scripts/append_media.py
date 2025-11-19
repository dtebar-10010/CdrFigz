import os
import django
from django.conf import settings  # Import to access settings like BASE_DIR

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "grand_v2_settings")  # Make sure this points to your settings file
django.setup()

from grand_v2_app.models import Media, Page

# Use BASE_DIR from settings
folder_path = os.path.join(settings.BASE_DIR, 'media/t/stills')  # Accessing BASE_DIR from settings

# Ensure Page with id=1 exists
try:
    page = Page.objects.get(id=1)
except Page.DoesNotExist:
    print("Page with id=1 does not exist.")
    exit()

# Get a list of all .mp4 files in the folder
mp4_files = [f for f in os.listdir(folder_path) if f.endswith('.mp4')]

# Loop through the .mp4 files and create Media objects
for mp4_file in mp4_files:
    # Extract the file name without the .mp4 extension
    file_name = os.path.splitext(mp4_file)[0]

    # Create a new Media entry
    media = Media(
        title=file_name,  # Name without the extension
        phase=page.phase,  # Use the phase from the page
        path=f'{file_name}.mp4',  # Path with the .mp4 extension
        page=page,  # Foreign key to Page with id=1
        type='video'  # Mark type as 'video'
    )

    # Save the media entry to the database
    media.save()

    print(f'Added media: {file_name}.mp4')

print("Finished adding .mp4 files to the Media table.")
