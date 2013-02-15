from mediamosa.api import MediaMosaAPI
from django.conf import settings


api = MediaMosaAPI(settings.MEDIAMOSA_URL)

if not (hasattr(settings, 'TESTING') and settings.TESTING):
    api.authenticate(
        settings.MEDIAMOSA_USERNAME,
        settings.MEDIAMOSA_PASSWORD)
