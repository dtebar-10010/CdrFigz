import os
from django.core.management.base import BaseCommand
from django.db import transaction
from grand_v2_app.models import Media

class Command( BaseCommand ):
  help = 'Replace the contents of media.path with the content of media.title'

  def handle( self, *args, **kwargs ):
    try:
      with transaction.atomic( ):
        medias = Media.objects.all( )
        for media in medias:
          media.path = media.title
          media.save( )

        self.stdout.write( self.style.SUCCESS( 'Successfully updated all media paths' ) )

    except Exception as e:
      self.stdout.write( self.style.ERROR( f'Error occurred: {e}' ) )
