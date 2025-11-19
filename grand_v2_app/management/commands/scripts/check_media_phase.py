from grand_v2_app.models import Page, Media

def run():
    # Retrieve the 'stills' page with phase 0
    page_phase_0 = Page.objects.get(name='stills', phase=0)

    # Get media items of type 'image'
    media_items_image = Media.objects.filter(page=page_phase_0, type='image')

    print(f"Total 'image' media items: {media_items_image.count()}")

    # Print the first few media items
    for media in media_items_image[:5]:
        print(f"Path: {media.path}, Title: {media.title}, Type: {media.type}, Phase: {media.phase}")
