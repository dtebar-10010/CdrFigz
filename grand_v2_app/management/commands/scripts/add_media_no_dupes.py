from grand_v2_app.models import Media, Page
import os
from django.conf import settings

def run():
    # Define the base path to the folders
    base_folder_path = os.path.join(settings.BASE_DIR, 'media')

    # Ensure the 'celeste' page exists
    try:
        celeste_page = Page.objects.get(id=3, name='celeste')
    except Page.DoesNotExist:
        print("The page 'celeste' does not exist.")
        return

    # Loop over folders 01, 02, 03, etc.
    for folder_num in range(1, 7):  # Assuming there are 6 folders (01 to 06)
        folder_name = f'{folder_num:02d}/celeste'  # Folder format '01/celeste', '02/celeste', etc.
        folder_path = os.path.join(base_folder_path, folder_name)

        # Check if the folder exists
        if not os.path.exists(folder_path):
            print(f"Folder {folder_path} does not exist. Skipping...")
            continue

        # Get all .mp4 files in the folder
        for filename in os.listdir(folder_path):
            if filename.endswith('.mp4'):
                # Extract the file name without the extension
                file_name_without_ext = os.path.splitext(filename)[0]

                # Check if the media record already exists
                if not Media.objects.filter(path=file_name_without_ext, page=celeste_page).exists():
                    # Create new media record
                    new_media = Media(
                        title=file_name_without_ext,
                        path=file_name_without_ext,
                        phase=folder_num,  # Phase is the folder number
                        page=celeste_page,
                        type='video'  # Media type is video
                    )
                    new_media.save()
                    print(f"Added: {file_name_without_ext} to the database.")
                else:
                    print(f"File {file_name_without_ext} already exists in the database.")
