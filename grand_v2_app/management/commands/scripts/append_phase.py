import os
import sys
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mtb_v4_settings.settings')
PROJECT_ROOT = os.path.dirname( os.path.abspath( '../../manage.py' ) )
sys.path.append(PROJECT_ROOT)

django.setup()

from mtb_v4_app.models import Media, Page  # Import both models

def add_media_phase_3(num_records=10):
    try:
        # Get the Page record with phase 0
        page = Page.objects.get(phase=0)
    except Page.DoesNotExist:
        print("Error: No Page record found with phase 0.")
        return  # Exit the script if the phase 0 page doesn't exist

    new_records = []
    for i in range(num_records):
        video_record = Media(
            title=f'New Video Phase 3 - {i+1}',
            phase=3,
            path=f'media/03/third_era-{i+1}.mp4',
            type='video',
            page=page
        )
        new_records.append(video_record)

        poster_record = Media(
            title=f'New Poster Phase 3 - {i+1}',
            phase=3,
            path=f'media/03/third_era-{i+1}.jpg',  # Poster path
            type='image',
            page=page
        )
        new_records.append(poster_record)

    Media.objects.bulk_create(new_records)
    print(f"Added {num_records * 2} Media records (video and poster) with phase 3, all associated with the phase 0 Page.")


if __name__ == '__main__':
    add_media_phase_3()
