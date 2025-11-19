# /scripts/populate_stills_media.py

import os
from django.conf import settings
from grand_v2_app.models import Page, Media

def run( *args ):
  # Ensure the 'stills' page exists
  try:
    stills_page = Page.objects.get( name = 'stills', phase = 0 )
  except Page.DoesNotExist:
    print( "Stills page not found." )
    return

  # Directory where still images are stored
  media_directory = 'd:\current\code\grand_v2_project/media/t/stills/'

  # Check if the directory exists
  if not os.path.exists( media_directory ):
    print( f"Directory {media_directory} does not exist." )
    return

  # Iterate through all files in the directory
  for filename in os.listdir( media_directory ):
    if filename.endswith( '.jpg' ):
      # Extract the name without extension
      name_without_extension = os.path.splitext( filename )[ 0 ]

      # Check if the media already exists to avoid duplicates
      if not Media.objects.filter( path = name_without_extension, page = stills_page ).exists( ):
        # Create a new Media record
        media = Media.objects.create(
          title = name_without_extension,
          phase = 0,  # Set phase as 0
          path = name_without_extension,  # Save the name without the extension
          page = stills_page,
          type = 'Still'  # Type set to 'Still'
        )
        print( f"Added media: {media.title}" )
      else:
        print( f"Media {name_without_extension} already exists." )

  print( "Media population completed." )
