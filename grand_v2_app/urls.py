from django.urls import path
from . import views

urlpatterns = [
  path( '', views.harrison, name = 'harrison' ),
  path( 'harrison/', views.harrison, name = 'harrison' ),
  path( 'celeste/', views.celeste, name = 'celeste' ),
  path( 'stills/', views.stills_view, name = 'stills' ),
]
