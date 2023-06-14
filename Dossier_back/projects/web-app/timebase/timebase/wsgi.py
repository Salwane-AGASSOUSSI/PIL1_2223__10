import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('settings.py', 'settings.py')

application = get_wsgi_application()

