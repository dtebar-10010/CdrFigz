from grand_v2_app.models import Page, Media  # Adjust this to your app name
import os

def run():
    base_dir = r'D:\current\code\grand_v2_project\media'

    def get_video_files():
        video_files = []
        for folder in range(1, 7):
            folder_name = os.path.join(f'{folder:02}', 'celeste')
            folder_path = os.path.join(base_dir, folder_name)

            # Debugging: print the folder path to verify correctness
            print(f"Checking folder: {folder_path}")

            if os.path.exists(folder_path):
                for filename in os.listdir(folder_path):
                    if filename.lower().endswith('.mp4'):
                        video_files.append((filename, folder_name))
                        # Debugging: print the file found
                        print(f"Found video file: {filename} in {folder_name}")
            else:
                # Debugging: notify if folder does not exist
                print(f"Folder does not exist: {folder_path}")

        return video_files

    def ensure_grand_page_exists():
        page, created = Page.objects.get_or_create(name='celeste', defaults={'phase': 2})
        if created:
            print(f"Created new 'celeste' page with id: {page.id}")
        else:
            print(f"Existing 'celeste' page found with id: {page.id}")
        return page.id

    def insert_video_data(video_files, grand_page_id):
        if not video_files:
            print("No video files found.")
            return

        if grand_page_id is None:
            print("Error: grand_page_id is None")
            return

        media_objects = [
            Media(
                title=filename.replace('.mp4', ''),
                phase=int(folder[:2]),  # Convert folder '01', '02', etc. to integer
                path=os.path.join(folder, filename),
                page_id=grand_page_id,
                type='video'
            )
            for filename, folder in video_files
        ]

        Media.objects.bulk_create(media_objects)
        print(f"Inserted {len(media_objects)} records into media table")

    # Execute the script
    video_files = get_video_files()
    print(f"Found {len(video_files)} video files")

    grand_page_id = ensure_grand_page_exists()
    if grand_page_id is not None:
        insert_video_data(video_files, grand_page_id)
    else:
        print("Failed to get or create 'celeste' page")
