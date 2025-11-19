from grand_v2_app.models import Page, Media

def run():
    try:
        # Retrieve the 'stills' page
        page_stills = Page.objects.get(name='stills')
        print(f"Page: {page_stills}")

        # Check if there are any media records associated with the 'stills' page
        media_items = Media.objects.filter(page=page_stills)
        print(f"Total media records associated with 'stills': {media_items.count()}")

        # Check if any media items have type='image' (which is stored for 'Still' records)
        media_stills = Media.objects.filter(page=page_stills, type='image')
        print(f"Total 'Still' media records: {media_stills.count()}")

        # Optionally, print out the first few media items
        for media in media_stills[:5]:
            print(f"Media: {media.title}, Path: {media.path}, Type: {media.type}")

    except Page.DoesNotExist:
        print("No page with name 'stills' found.")
    except Exception as e:
        print(f"An error occurred: {e}")
