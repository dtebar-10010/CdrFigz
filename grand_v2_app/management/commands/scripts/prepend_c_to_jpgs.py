import os
from django.conf import settings

def run( ):
  # Define the directory where the .jpg files are located
  media_dir = r"d:/current/code/grand_v2_project/media/01/celeste/t/"

  # List all files in the directory
  for filename in os.listdir( media_dir ):
    # if filename.endswith( ".mp4" ):
      old_path = os.path.join( media_dir, filename )
      new_filename = "c-" + filename
      new_path = os.path.join( media_dir, new_filename )

      # Rename the file
      os.rename( old_path, new_path )
      print( f"Renamed: {old_path} -> {new_path}" )

  print( "All files have been renamed successfully." )
