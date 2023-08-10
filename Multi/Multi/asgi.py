import os

from django.core.wsgi import get_wsgi_application

# application의 settings.py의 경로를 찾아간다! 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Multi.settings')

application = get_wsgi_application()