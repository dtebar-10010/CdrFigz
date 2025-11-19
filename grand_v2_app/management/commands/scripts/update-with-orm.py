import os
import django

# Set up Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'grand_v2_settings.settings')
django.setup()

from grand_v2_app.models import Page, Media  # Adjust to your actual model and app names

# Base directory where the numbered folders are located
base_dir = r'D:\current\code\inPHP\harrison\img\videos'

def get_video_files():
    video_files = []
    for folder in range(1, 7):  # Folders 1 through 6
        folder_path = os.path.join(base_dir, str(folder))
        if os.path.exists(folder_path):
            for filename in os.listdir(folder_path):
                if filename.lower().endswith('.mp4'):
                    video_files.append((filename, folder))
    return video_files

def insert_video_data(video_files, grand_page_id):
    if not video_files:
        print("No video files found.")
        return

    if grand_page_id is None:
        print("Error: grand_page_id is None")
        return

    print(f"Inserting video data with grand_page_id: {grand_page_id}")

    media_objects = [
        Media(
            title=filename.replace('.mp4', ''),
            phase=folder,
            path=os.path.join(base_dir, str(folder), filename),
            page_id=grand_page_id,
            type='video'
        )
        for filename, folder in video_files
    ]

    Media.objects.bulk_create(media_objects)
    print(f"Inserted {len(media_objects)} records into media table")

def main():
    video_files = get_video_files()
    print(f"Found {len(video_files)} video files")
    if len(video_files) > 0:
        print("Sample video files:")
        for vf in video_files[:5]:
            print(vf)

    # Use Django ORM to manage Page and Media
    grand_page, created = Page.objects.get_or_create(name='grand', defaults={'phase': 1})
    if created:
        print(f"Created new 'grand' page with id: {grand_page.id}")
    else:
        print(f"Existing 'grand' page found with id: {grand_page.id}")

    insert_video_data(video_files, grand_page.id)

if __name__ == "__main__":
    main()
