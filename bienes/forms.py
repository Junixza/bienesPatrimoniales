from django import forms
from .models import Bien, Operador

# -----------------------------------------------------------------------------
# Nota de documentación (modo ejemplo)
# Formularios funcionales para operar Bienes y Operadores. Se entregan como
# base/plantilla para personalizar validaciones, etiquetas, help_text y widgets
# según necesidades institucionales.
# -----------------------------------------------------------------------------
class BienForm(forms.ModelForm):
    class Meta:
        model = Bien
        fields = [
            'nombre',
            'descripcion',
            'codigo_patrimonial',
            'fecha_adquisicion',
            'valor',
            'cuenta_codigo',
            'tipo_origen',
            'estado',
            'fecha_baja',
            'motivo_baja',
            'ubicacion',
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'codigo_patrimonial': forms.TextInput(attrs={'class': 'form-control'}),
            'valor': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'fecha_adquisicion': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'cuenta_codigo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 6.1.0'}),
            'tipo_origen': forms.Select(attrs={'class': 'form-select'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
            'fecha_baja': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'motivo_baja': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'ubicacion': forms.TextInput(attrs={'class': 'form-control'}),
        }


class OperadorForm(forms.ModelForm):
    class Meta:
        model = Operador
        fields = ['usuario', 'bienes_asignados', 'activo']
        widgets = {
            'usuario': forms.Select(attrs={'class': 'form-select'}),
            'bienes_asignados': forms.SelectMultiple(attrs={'class': 'form-select', 'size': 8}),
            'activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class BajaBienForm(forms.ModelForm):
    class Meta:
        model = Bien
        fields = ['fecha_baja', 'motivo_baja']
        widgets = {
            'fecha_baja': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'motivo_baja': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
        }
