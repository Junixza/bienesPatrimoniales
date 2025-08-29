from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Bien, Perfil, Operador

# -----------------------------------------------------------------------------
# Nota de documentación (modo ejemplo)
# Este módulo de administración funciona correctamente para un uso básico
# (inlines de Perfil y Operador, configuración de listas y filtros), pero está
# entregado a modo de ejemplo/plantilla. Se puede usar en desarrollo y sirve
# como base para producción mínima. Ajustar según políticas de tu institución,
# permisos finos, búsquedas avanzadas y auditorías.
# -----------------------------------------------------------------------------

# Clases personalizadas para el admin
class PerfilInline(admin.StackedInline):
    model = Perfil
    can_delete = False
    verbose_name_plural = 'Perfil'
    fk_name = 'user'

class OperadorInline(admin.StackedInline):
    model = Operador
    can_delete = False
    verbose_name_plural = 'Operador'
    fk_name = 'usuario'
    filter_horizontal = ('bienes_asignados',)

class UsuarioPersonalizadoAdmin(UserAdmin):
    inlines = (PerfilInline, OperadorInline)
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'get_tipo_usuario')
    list_select_related = ('perfil', 'operador')

    def get_tipo_usuario(self, instance):
        return instance.perfil.get_tipo_usuario_display()
    get_tipo_usuario.short_description = 'Tipo de Usuario'

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return []
        return super().get_inline_instances(request, obj)

# Desregistrar el modelo User original y registrar el personalizado
admin.site.unregister(User)
admin.site.register(User, UsuarioPersonalizadoAdmin)

@admin.register(Bien)
class BienAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'codigo_patrimonial', 'estado', 'ubicacion', 'fecha_creacion')
    list_filter = ('estado', 'fecha_creacion')
    search_fields = ('nombre', 'codigo_patrimonial', 'descripcion')
    date_hierarchy = 'fecha_creacion'
    ordering = ('-fecha_creacion',)
    fieldsets = (
        ('Información Básica', {
            'fields': ('nombre', 'descripcion', 'codigo_patrimonial')
        }),
        ('Detalles', {
            'fields': ('fecha_adquisicion', 'valor', 'estado', 'ubicacion')
        }),
        ('Fechas', {
            'fields': ('fecha_creacion', 'fecha_actualizacion'),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ('fecha_creacion', 'fecha_actualizacion')

@admin.register(Operador)
class OperadorAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'activo', 'fecha_creacion')
    list_filter = ('activo', 'fecha_creacion')
    search_fields = ('usuario__username', 'usuario__first_name', 'usuario__last_name')
    filter_horizontal = ('bienes_asignados',)
    date_hierarchy = 'fecha_creacion'
