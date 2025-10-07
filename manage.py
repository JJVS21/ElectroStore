#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():  # Vista backend
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Electrostore.settings')  # Configuración entorno Django
    try:
        from django.core.management import execute_from_command_line  # Ejecuta comandos del backend
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)  # Ejecuta comandos del backend


if __name__ == '__main__':
    main()
