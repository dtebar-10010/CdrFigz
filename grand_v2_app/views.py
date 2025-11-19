from django.shortcuts import render
from django.conf import settings
from .models import Media, Page
import random

def harrison( request ):
  # Get the page with the name 'harrison'
  page_harrison = Page.objects.get( name = 'harrison' )

  current_phase = request.GET.get( 'phase', None )
  if not current_phase:
    current_phase = 1
  else:
    current_phase = int( current_phase )

  # Format the current_phase as a two-digit string
  current_phase = f"{current_phase:02d}"

  # Filter media by phase and page
  media_list = Media.objects.filter( phase = current_phase, page = page_harrison )

  # Filter media to only include videos, and select a random sample
  media_videos = media_list.filter( type = 'video' )
  media_list = random.sample( list( media_videos ), min( 9, len( media_videos ) ) )

  # Define phases
  phases = [ (i, str( i )) for i in range( 1, 8 ) ]  # 7 phases
  context = {
    'current_phase': current_phase,
    'media_list'   : media_list,
    'phases'       : phases,
    'MEDIA_URL'    : settings.MEDIA_URL,
    'page'         : page_harrison,
    'page_name'    : 'harrison',
  }
  return render( request, 'home.html', context )

def celeste( request ):
  # Get the page with the name 'celeste'
  page_celeste = Page.objects.get( name = 'celeste' )

  current_phase = request.GET.get( 'phase', None )
  if not current_phase:
    current_phase = 1
  else:
    current_phase = int( current_phase )

  # Format the current_phase as a two-digit string
  current_phase = f"{current_phase:02d}"

  # Filter media by phase and page
  media_list = Media.objects.filter( phase = current_phase, page = page_celeste )

  # Filter media to only include videos, and select a random sample
  media_videos = media_list.filter( type = 'video' )
  media_list = random.sample( list( media_videos ), min( 9, len( media_videos ) ) )

  # Define phases
  phases = [ (i, str( i )) for i in range( 1, 6 ) ]  # 5 phases
  context = {
    'current_phase': current_phase,
    'media_list'   : media_list,
    'phases'       : phases,
    'MEDIA_URL'    : settings.MEDIA_URL,
    'page'         : page_celeste,
    'page_name'    : 'celeste',
  }

  return render( request, 'home.html', context )

def stills_view( request ):
  # Retrieve the 'stills' page
  page_stills = Page.objects.get( name = 'stills' )

  # Get all media items associated with the 'stills' page and randomize the order
  # images = Media.objects.filter(page=page_stills).order_by('?')
  images = Media.objects.filter( page = page_stills )

  context = { 'images': images }
  return render( request, 'stills.html', context )
