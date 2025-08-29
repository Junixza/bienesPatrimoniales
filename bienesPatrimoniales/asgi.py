"""
ASGI config for bienesPatrimoniales project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

# -----------------------------------------------------------------------------
# Nota de documentación (modo ejemplo)
# Este archivo ASGI es funcional y puede usarse en desarrollo/producción con un
# servidor ASGI (uvicorn/daphne). Se entrega como base/plantilla y puede
# requerir ajustes (settings por entorno, variables de entorno, middleware ASGI)
# según la infraestructura de despliegue.
# -----------------------------------------------------------------------------

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bienesPatrimoniales.settings')

application = get_asgi_application()
