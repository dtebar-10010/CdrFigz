from django.db import models

class Page( models.Model ):
  name = models.CharField( max_length = 255 )
  phase = models.IntegerField( )

  class Meta:
    verbose_name_plural = "Page"
    app_label = 'grand_v2_app'

  def __str__( self ):
    return f"Page: {self.name} (Phase: {self.phase})"

class Media( models.Model ):
  title = models.CharField( max_length = 255 )
  phase = models.IntegerField( )
  path = models.CharField( max_length = 255 )
  page = models.ForeignKey( Page, on_delete = models.CASCADE )

  type = models.CharField( max_length = 255, choices = [
    ('image', 'Cover'),
    ('image', 'Poster'),
    ('video', 'Video'),
    ('image', 'Still'),
  ] )

  class Meta:
    verbose_name_plural = "Media"
    app_label = 'grand_v2_app'

  def __str__( self ):
    return f"Media: {self.title}"

  def poster_path( self ):
    if self.type == 'video':
      return self.path.replace( '.mp4', '.jpg' )
    return None

# class History( models.Model ):
#   content = models.TextField( )
#   phase = models.IntegerField( )
#   page = models.ForeignKey( Page, on_delete = models.CASCADE )
#
#   class Meta:
#     verbose_name_plural = "History"
#
#   def __str__( self ):
#     return f"History: (Page {self.page.name})"
