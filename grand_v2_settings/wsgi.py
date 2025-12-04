"""
WSGI config for grand_v3 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import sys
import os

# Add your project directory to the sys.path (for PythonAnywhere)
production_path = "/home/dtebar/grand"
if os.path.exists(production_path):
    sys.path.append(production_path)

# Set environment variables for production
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "grand_v2_settings.settings")
os.environ.setdefault("DJANGO_DEBUG", "False")
os.environ.setdefault(
    "DJANGO_ALLOWED_HOSTS",
    "commander-figz.com,www.commander-figz.com,dtebar.pythonanywhere.com",
)
os.environ.setdefault(
    "DJANGO_CSRF_TRUSTED_ORIGINS",
    "https://commander-figz.com,https://www.commander-figz.com",
)

# Import the Django WSGI application
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
