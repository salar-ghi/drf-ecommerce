import os

from django.core.asgi import get_asgi_application
from core.settings import base

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

if base.DEBUG:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings.local')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings.production')

application = get_asgi_application()
