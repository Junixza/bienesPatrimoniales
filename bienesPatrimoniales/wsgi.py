"""
WSGI config for bienesPatrimoniales project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

# -----------------------------------------------------------------------------
# Nota de documentación (modo ejemplo)
# Este archivo WSGI es funcional y puede usarse en servidores como gunicorn o
# mod_wsgi. Se entrega como base/plantilla y puede requerir ajustes por entorno
# (variables de entorno, settings de producción, middleware de seguridad, etc.).
# -----------------------------------------------------------------------------

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bienesPatrimoniales.settings')

application = get_wsgi_application()
