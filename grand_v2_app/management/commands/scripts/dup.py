import os
import sys
import logging
import django

# Set up Django environment
os.environ['DJANGO_SETTINGS_MODULE'] = 'mtb_v4_settings.settings'  # Replace 'mtb_v4_settings' with your project name
PROJECT_ROOT = os.path.dirname( os.path.abspath( '../../manage.py' ) )
sys.path.append(PROJECT_ROOT)

# Initialize Django
django.setup()

# Import your models
from mtb_v4_app.models import Media  # Import only the Media model


# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def duplicate_records(num_duplicates=4):
    model = Media  # Only duplicate Media records

    try:
        original_records = list(model.objects.all())
        for phase_offset in range(1, num_duplicates + 1):
            new_records = []
            for record in original_records:
                # Create a copy of the record data and EXCLUDE the 'id' and '_state' fields
                new_record_data = {k: v for k, v in record.__dict__.items() if k != 'id' and k != '_state'}
                new_record_data['phase'] += phase_offset  # Increment the 'phase'

                # Create and add the new record
                new_record = model(**new_record_data)
                new_records.append(new_record)

            model.objects.bulk_create(new_records)
        logger.info(f"Successfully duplicated records for model: {model.__name__}")
    except Exception as e:
        logger.error(f"Error duplicating records for model {model.__name__}: {e}")


if __name__ == '__main__':
    duplicate_records()
