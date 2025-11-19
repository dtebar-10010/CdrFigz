import os
from grand_v2_app.models import Media, Page

# Constants
MEDIA_STILLS_DIR = "D:/current/code/grand_v2_project/media/stills/"
DEFAULT_PAGE_NAME = 'stills'  # Set your default page name here

def run( ):
  try:
    # Get or create a default page for the media (you can customize this logic)
    default_page, _ = Page.objects.get_or_create( name = DEFAULT_PAGE_NAME, phase = 0 )

    # Get all media records where phase = 0 and type = 'Still'
    media_records = Media.objects.filter( phase = 0 )

    # Collect existing file names from the database (without the extension)
    existing_media = { os.path.splitext( os.path.basename( media.path ) )[ 0 ] for media in media_records }

    # Get all .jpg files in the /media/stills/ folder
    stills_files = [ f for f in os.listdir( MEDIA_STILLS_DIR ) if f.endswith( '.jpg' ) ]

    # Loop over each file and add it to the database if not present
    for file_name in stills_files:
      name_without_ext = os.path.splitext( file_name )[ 0 ]
      if name_without_ext not in existing_media:
        # Create a new Media object for the missing file
        new_media = Media(
          title = name_without_ext,
          phase = 0,
          path = name_without_ext,
          page = default_page,  # Assign the default page
          type = 'image',  # Set to 'Still'
        )
        new_media.save( )
        print( f"Added new media: {new_media.title}" )
      else:
        print( f"Media already exists: {name_without_ext}" )

    print( "Scan complete!" )

  except Exception as e:
    print( f"An error occurred: {e}" )
