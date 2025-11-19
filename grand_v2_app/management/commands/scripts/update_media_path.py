from grand_v2_app.models import Media  # Adjust to your app name

def run():
    # Fetch all media records
    media_records = Media.objects.all()

    if not media_records:
        print("No media records found.")
        return

    # Update the 'path' field to be the same as 'title' for each record
    updated_count = 0
    for media in media_records:
        media.path = media.title
        media.save()
        updated_count += 1
        print(f"Updated Media ID {media.id}: path set to title '{media.title}'")

    print(f"Successfully updated {updated_count} media records.")
