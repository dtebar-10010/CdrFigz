from django.conf.urls.i18n import i18n_patterns
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

# Adding i18n patterns for internationalization support
urlpatterns = i18n_patterns(
  path( 'admin/', admin.site.urls ),
  path( '', include( 'grand_v2_app.urls' ) ),  # Include your app's URLs here
)

# Serving static and media files
if settings.DEBUG:
  urlpatterns += static( settings.MEDIA_URL, document_root = settings.MEDIA_ROOT )
  urlpatterns += static( settings.STATIC_URL, document_root = settings.STATIC_ROOT )
