from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Bien(models.Model):
    """
    Modelo para representar un bien patrimonial en el sistema.
    """
    # Choices alineados al instructivo
    TIPO_ORIGEN_CHOICES = [
        ('DONACION', 'Donación'),
        ('OMISION', 'Omisión'),
        ('TRANSFERENCIA', 'Transferencia/Traslado'),
        ('COMPRA', 'Compra'),
    ]

    ESTADO_CHOICES = [
        ('ACTIVO', 'Activo'),
        ('BAJA', 'Dado de baja'),
        ('TRANSFERIDO', 'Transferido'),
        ('MANTENIMIENTO', 'En mantenimiento'),
    ]

    nombre = models.CharField(max_length=200, verbose_name='Nombre del Bien')
    descripcion = models.TextField(verbose_name='Descripción', blank=True, null=True)
    codigo_patrimonial = models.CharField(max_length=50, unique=True, verbose_name='Código Patrimonial')
    fecha_adquisicion = models.DateField(verbose_name='Fecha de Adquisición', null=True, blank=True)
    valor = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Valor')
    # Patrimonial mínimo
    cuenta_codigo = models.CharField(max_length=20, verbose_name='Cuenta / Código', blank=True)
    tipo_origen = models.CharField(max_length=20, choices=TIPO_ORIGEN_CHOICES, verbose_name='Tipo de Origen', blank=True)
    estado = models.CharField(
        max_length=20,
        choices=ESTADO_CHOICES,
        default='ACTIVO',
        verbose_name='Estado del Bien',
    )
    fecha_baja = models.DateField(null=True, blank=True, verbose_name='Fecha de Baja')
    motivo_baja = models.TextField(null=True, blank=True, verbose_name='Motivo de Baja')
    ubicacion = models.CharField(max_length=200, verbose_name='Ubicación')
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name='Última Actualización')

    class Meta:
        verbose_name = 'Bien Patrimonial'
        verbose_name_plural = 'Bienes Patrimoniales'
        ordering = ['-fecha_creacion']

    def __str__(self):
        return f"{self.nombre} - {self.codigo_patrimonial}"

class Perfil(models.Model):
    """
    Modelo para extender el modelo de Usuario con información adicional.
    """
    TIPO_USUARIO = [
        ('administrador', 'Administrador'),
        ('operador', 'Operador'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    tipo_usuario = models.CharField(
        max_length=20, 
        choices=TIPO_USUARIO, 
        default='operador',
        verbose_name='Tipo de Usuario'
    )
    telefono = models.CharField(max_length=20, blank=True, null=True, verbose_name='Teléfono')
    fecha_nacimiento = models.DateField(null=True, blank=True, verbose_name='Fecha de Nacimiento')
    direccion = models.TextField(blank=True, null=True, verbose_name='Dirección')
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')

    class Meta:
        verbose_name = 'Perfil de Usuario'
        verbose_name_plural = 'Perfiles de Usuarios'
        ordering = ['user__last_name', 'user__first_name']

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.get_tipo_usuario_display()}"

    @property
    def es_administrador(self):
        return self.tipo_usuario == 'administrador'

    @property
    def es_operador(self):
        return self.tipo_usuario == 'operador'

class Operador(models.Model):
    """
    Modelo para gestionar la relación entre usuarios operadores y bienes.
    """
    usuario = models.OneToOneField(
        User, 
        on_delete=models.CASCADE, 
        related_name='operador',
        verbose_name='Usuario Operador'
    )
    bienes_asignados = models.ManyToManyField(
        Bien, 
        related_name='operadores',
        blank=True,
        verbose_name='Bienes Asignados'
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    activo = models.BooleanField(default=True, verbose_name='¿Activo?')

    class Meta:
        verbose_name = 'Operador'
        verbose_name_plural = 'Operadores'
        ordering = ['-fecha_creacion']

    def __str__(self):
        return f"Operador: {self.usuario.get_full_name()}"

# Señales para crear/actualizar perfiles automáticamente
@receiver(post_save, sender=User)
def crear_actualizar_perfil_usuario(sender, instance, created, **kwargs):
    """
    Crea o actualiza el perfil cuando se crea o actualiza un usuario.
    """
    if created:
        Perfil.objects.create(user=instance)
    else:
        # Si el usuario ya existe, solo guarda el perfil si existe
        if hasattr(instance, 'perfil'):
            instance.perfil.save()

@receiver(post_save, sender=User)
def guardar_perfil_usuario(sender, instance, **kwargs):
    """
    Guarda el perfil del usuario cuando se guarda el usuario.
    """
    if hasattr(instance, 'perfil'):
        instance.perfil.save()
