import os

from django.core.wsgi import get_wsgi_application
from core.settings import base

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

if base.DEBUG:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings.local')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings.production')

application = get_wsgi_application()
