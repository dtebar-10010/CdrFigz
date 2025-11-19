# /scripts/update_stills_media_type.py

from grand_v2_app.models import Page, Media

def run(*args):
    # Ensure the 'stills' page exists
    try:
        stills_page = Page.objects.get(name='stills', phase=2)
    except Page.DoesNotExist:
        print("Stills page not found.")
        return

    # Get all media entries associated with the 'stills' page
    stills_media = Media.objects.filter(page=stills_page)

    # Update the 'type' field to 'image' for all media entries linked to the 'stills' page
    for media in stills_media:
        if media.type != 'image':
            media.type = 'image'  # 'image' is the actual value stored for 'Still'
            media.save()
            print(f"Updated media type to 'image' for: {media.title}")
        else:
            print(f"Media type already set to 'image' for: {media.title}")

    print("Type update for 'stills' media completed.")
