import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('settings.py', 'settings.py')

application = get_asgi_application()
