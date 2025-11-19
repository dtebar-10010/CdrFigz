import os
import psycopg2
from psycopg2 import sql

# Database connection parameters
db_params = {
   'dbname'  : 'grand_v2_pgdb',
   'user'    : 'postgres',
   'password': 'postgres',
   'host'    : 'localhost',
   'port'    : '5432'
}

# Base directory where the numbered folders are located
base_dir = r'D:\current\code\inPHP\harrison\img\videos'

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
      # Create temporary table
      cursor.execute( """
           CREATE TEMPORARY TABLE temp_video_files (
               filename VARCHAR(255),
               folder_number INTEGER
           )
           """ )

      # Insert data into temporary table
      insert_query = sql.SQL( "INSERT INTO temp_video_files (filename, folder_number) VALUES (%s, %s)" )
      cursor.executemany( insert_query, video_files )

      # Print the first few rows of temp_video_files for debugging
      cursor.execute( "SELECT * FROM temp_video_files LIMIT 5" )
      print( "Sample data in temp_video_files:" )
      for row in cursor.fetchall( ):
         print( row )

      print( f"grand_page_id type: {type( grand_page_id )}" )
      print( f"grand_page_id value: {grand_page_id}" )

      # Simplified query for debugging
      query = "SELECT %s AS page_id"

      print( "SQL Query before mogrify:", query )
      print( "Parameters for mogrify:", [ grand_page_id ] )

      try:
         print( "SQL Query after mogrify:", cursor.mogrify( query, [ grand_page_id ] ) )
      except Exception as e:
         print( f"Error during mogrify: {e}" )

      # Commenting out the actual INSERT for now to focus on debugging mogrify
      # cursor.execute(query, [grand_page_id])
      # inserted_ids = cursor.fetchall()
      # if inserted_ids:
      #     print(f"Inserted {len(inserted_ids)} records into media table")
      # else:
      #     print("No records were inserted into media table")
      # Drop temporary table
      cursor.execute( "DROP TABLE temp_video_files" )

      conn.commit( )  # Commit after the INSERT (even though there's no INSERT currently)

   except Exception as e:
      print( f"Error in insert_video_data: {e}" )
      print( f"Error type: {type( e )}" )
      import traceback
      traceback.print_exc( )

def main( ):
   video_files = get_video_files( )
   print( f"Found {len( video_files )} video files" )
   if len( video_files ) > 0:
      print( "Sample video files:" )
      for vf in video_files[ :5 ]:
         print( vf )

   try:
      conn = psycopg2.connect( **db_params )
      with conn.cursor( ) as cursor:
         create_tables_if_not_exist( cursor )
         grand_page_id = ensure_grand_page_exists( cursor )
         if grand_page_id is not None:
            insert_video_data( cursor, video_files, grand_page_id )
         else:
            print( "Failed to get or create 'grand' page" )
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
