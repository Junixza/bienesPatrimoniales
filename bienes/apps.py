from django.apps import AppConfig

# -----------------------------------------------------------------------------
# Nota de documentación (modo ejemplo)
# Configuración del app `bienes`. Es funcional y puede usarse tal cual,
# pero se entrega como base/plantilla para ajustes de nombres, verbose_name
# y señales según el proyecto.
# -----------------------------------------------------------------------------
class BienesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bienes'
    verbose_name = 'Gestión de Bienes Patrimoniales'
