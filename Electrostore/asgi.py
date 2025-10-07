"""
ASGI config for web1 project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application  # Punto de entrada servidor

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Electrostore.settings')  # Configuración entorno Django

application = get_asgi_application()  # Punto de entrada servidor
