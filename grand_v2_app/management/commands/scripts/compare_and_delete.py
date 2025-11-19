import os
from grand_v2_app.models import Media

def run( ):
  # Define the correct absolute path for the local media directory
  local_media_dir = r'D:\current\code\grand_v2_project\media\stills'

  # Ensure the directory exists
  if not os.path.exists( local_media_dir ):
    print( f"Directory {local_media_dir} does not exist." )
    return

  # Get all Media records where phase is 0
  media_records = Media.objects.filter( phase = 0 )

  # Print out the media records to inspect their values
  print( f"Found {media_records.count( )} media records with phase 0:" )
  for media in media_records:
    print( f"Media record - Path: {media.path}, Title: {media.title}, Type: {media.type}" )

  # Get the filenames (without extensions) from the local directory
  local_filenames = [ os.path.splitext( f )[ 0 ] for f in os.listdir( local_media_dir ) if f.endswith( '.jpg' ) ]

  # Track how many records are deleted
  delete_count = 0

  # Compare the media paths with the local filenames
  for media in media_records:
    media_filename = os.path.splitext( os.path.basename( media.path ) )[ 0 ]  # Get the filename without extension
    if media_filename not in local_filenames:
      print( f"Deleting Media record with path: {media.path}" )
      media.delete( )
      delete_count += 1
      if delete_count >= 5:
        print( "Deleted 5 media records." )
        break

  if delete_count == 0:
    print( "No unmatched media records found." )
  else:
    print( f"Deleted {delete_count} unmatched media records." )
