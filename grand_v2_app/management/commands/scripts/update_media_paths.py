import os
import psycopg2
from psycopg2 import sql

import django

# Set up Django settings
os.environ.setdefault( 'DJANGO_SETTINGS_MODULE', 'grand_v2_settings.settings' )
django.setup( )

# Database connection parameters
# db_params = {
#   'dbname'  : 'grand_v2_pgdb',
#   'user'    : 'postgres',
#   'password': 'postgres',
#   'host'    : 'localhost',
#   'port'    : '5432'
# }

DATABASES = {
 'default': {
  'ENGINE': 'django.db.backends.sqlite3',
  'NAME'  : BASE_DIR / 'db.sqlite3',
 }
}

# Base directory where the numbered folders are located
base_dir = r'/media'

def get_video_files( ):
  video_files = [ ]
  for folder in range( 1, 7 ):  # Folders 1 through 6
    folder_path = os.path.join( base_dir, str( folder ) )
    if os.path.exists( folder_path ):
      for filename in os.listdir( folder_path ):
        if filename.lower( ).endswith( '.mp4' ):
          video_files.append( (filename, folder) )
  return video_files

def create_tables_if_not_exist( cursor ):
  # Create Page table if it doesn't exist
  cursor.execute( """
        CREATE TABLE IF NOT EXISTS page (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255),
            phase INTEGER
        )
    """ )

  # Create Media table if it doesn't exist
  cursor.execute( """
        CREATE TABLE IF NOT EXISTS media (
            id SERIAL PRIMARY KEY,
            title VARCHAR(255),
            phase INTEGER,
            path VARCHAR(255),
            page_id INTEGER REFERENCES page(id),
            type VARCHAR(255)
        )
    """ )

def ensure_grand_page_exists( cursor ):
  try:
    # Check if 'grand' page exists
    cursor.execute( "SELECT id FROM page WHERE name = 'grand'" )
    result = cursor.fetchone( )

    if result:
      print( f"Existing 'grand' page found with id: {result[ 0 ]}" )
      return result[ 0 ]
    else:
      # If 'grand' page doesn't exist, create it
      cursor.execute( """
                INSERT INTO page (name, phase) VALUES ('grand', 1) RETURNING id
            """ )
      new_id = cursor.fetchone( )[ 0 ]
      print( f"Created new 'grand' page with id: {new_id}" )
      return new_id
  except psycopg2.Error as e:
    print( f"Error in ensure_grand_page_exists: {e}" )
    return None

def insert_video_data( cursor, video_files, grand_page_id ):
  if not video_files:
    print( "No video files found." )
    return

  if grand_page_id is None:
    print( "Error: grand_page_id is None" )
    return

  print( f"Inserting video data with grand_page_id: {grand_page_id}" )

  try:
    # Insert data directly into media table
    insert_query = sql.SQL( """
            INSERT INTO media (title, phase, path, page_id, type)
            VALUES (%s, %s, %s, %s, %s)
        """ )

    # Prepare data for insertion
    data_to_insert = [
      (filename.replace( '.mp4', '' ), folder, os.path.join( base_dir, str( folder ), filename ), grand_page_id, 'video')
      for filename, folder in video_files
    ]

    # Insert data into media table
    cursor.executemany( insert_query, data_to_insert )

    print( f"Inserted {len( data_to_insert )} records into media table" )

  except psycopg2.Error as e:
    print( f"Error in insert_video_data: {e}" )
  except Exception as e:
    print( f"Unexpected error in insert_video_data: {e}" )
    import traceback
    traceback.print_exc( )

def main( ):
  video_files = get_video_files( )
  print( f"Found {len( video_files )} video files" )
  if len( video_files ) > 0:
    print( "Sample video files:" )
    for vf in video_files[ :5 ]:
      print( vf )

  conn = None
  try:
    conn = psycopg2.connect( **db_params )
    with conn.cursor( ) as cursor:
      create_tables_if_not_exist( cursor )
      grand_page_id = ensure_grand_page_exists( cursor )
      if grand_page_id is not None:
        insert_video_data( cursor, video_files, grand_page_id )
      else:
        print( "Failed to get or create 'grand' page" )
    conn.commit( )  # Commit after the INSERT
  except psycopg2.Error as e:
    print( f"Database error: {e}" )
  except Exception as e:
    print( f"Unexpected error: {e}" )
    import traceback
    traceback.print_exc( )
  finally:
    if conn:
      conn.close( )

if __name__ == "__main__":
  main( )
