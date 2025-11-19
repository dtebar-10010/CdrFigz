from grand_v2_app.models import Media, Page

def run( ):
  try:
    # Retrieve the 'stills' page
    page_stills = Page.objects.get( name = 'stills' )

    # Get all media items associated with the 'stills' page
    media_items_to_delete = Media.objects.filter( page = page_stills )

    # Delete all media records for the 'stills' page
    count, _ = media_items_to_delete.delete( )

    print( f"Deleted {count} media items associated with the 'stills' page." )

  except Page.DoesNotExist:
    print( "No page with name 'stills' found." )
  except Exception as e:
    print( f"An error occurred: {e}" )
