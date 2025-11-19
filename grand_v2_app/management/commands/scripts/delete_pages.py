import os
import sys
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mtb_v4_settings.settings')  # Replace 'mtb_v4_settings' with your project name
PROJECT_ROOT = os.path.dirname( os.path.abspath( '../../manage.py' ) )
sys.path.append(PROJECT_ROOT)

django.setup()

from mtb_v4_app.models import Page, Media

def delete_pages_except_phase_0():
    try:
        # Get the Page record with phase 0
        phase_0_page = Page.objects.get(phase=0)

        # Delete all other Page records except phase 0 and their related Media
        Page.objects.exclude(id=phase_0_page.id).delete()

        print("Successfully deleted Page records and related Media, except for phase 0.")
    except Page.DoesNotExist:
        print("No Page record found with phase 0.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    delete_pages_except_phase_0()
