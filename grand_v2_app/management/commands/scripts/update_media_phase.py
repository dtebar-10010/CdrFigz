from django.core.exceptions import ObjectDoesNotExist
from grand_v2_app.models import Page, Media  # Make sure to replace 'grand_v2_app' with your actual app name if needed

# Set up Django settings (this is optional, Django should already be configured by manage.py when using runscript)
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yourproject.settings')
# django.setup()

def run( ):
  try:
    # Get the page with name 'stills' and phase 2
    page = Page.objects.get( name = 'stills', phase = 0 )

    # Update all media associated with the page to phase 0
    Media.objects.filter( page = page ).update( phase = 0 )

    print( f"Successfully updated media records associated with page 'stills' (Phase: 2) to Phase: 0." )

  except ObjectDoesNotExist:
    print( "Page 'stills' with Phase: 2 does not exist." )
