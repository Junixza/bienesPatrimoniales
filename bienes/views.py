from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Bien, Operador
from .forms import BienForm, BajaBienForm, OperadorForm

# Vistas del módulo Bienes / Panel

@login_required
def dashboard(request):
    """Panel principal con métricas básicas.

    Nota: Por ahora se muestran valores por defecto. Luego conectaremos con
    los modelos para obtener estadísticas reales.
    """
    stats = {
        "bienes_total": 0,
        "bienes_activos": 0,
        "bienes_baja": 0,
    }
    return render(request, "panel/dashboard.html", {"stats": stats})


# ---------- CRUD de Bienes ----------

@login_required
def bienes_lista(request):
    bienes = Bien.objects.all().order_by('nombre')
    return render(request, 'bienes/lista.html', {'bienes': bienes})


@login_required
def bien_crear(request):
    if request.method == 'POST':
        form = BienForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bienes_lista')
    else:
        form = BienForm()
    return render(request, 'bienes/form.html', {'form': form, 'titulo': 'Alta de Bien'})


@login_required
def bien_editar(request, pk):
    bien = get_object_or_404(Bien, pk=pk)
    if request.method == 'POST':
        form = BienForm(request.POST, instance=bien)
        if form.is_valid():
            form.save()
            return redirect('bienes_lista')
    else:
        form = BienForm(instance=bien)
    return render(request, 'bienes/form.html', {'form': form, 'titulo': 'Editar Bien'})


@login_required
def bien_eliminar(request, pk):
    bien = get_object_or_404(Bien, pk=pk)
    if request.method == 'POST':
        bien.delete()
        return redirect('bienes_lista')
    return render(request, 'bienes/confirm_delete.html', {'bien': bien})


@login_required
def bien_baja(request, pk):
    bien = get_object_or_404(Bien, pk=pk)
    if request.method == 'POST':
        form = BajaBienForm(request.POST, instance=bien)
        if form.is_valid():
            bien = form.save(commit=False)
            bien.estado = 'BAJA'
            if not bien.fecha_baja:
                # Si no se indicó, poner hoy
                from django.utils.timezone import now
                bien.fecha_baja = now().date()
            bien.save()
            return redirect('bienes_lista')
    else:
        form = BajaBienForm(instance=bien)
    return render(request, 'bienes/baja.html', {'form': form, 'bien': bien})


# ---------- Operadores ----------

@login_required
def operadores_lista(request):
    operadores = Operador.objects.select_related('usuario').prefetch_related('bienes_asignados').order_by('-fecha_creacion')
    return render(request, 'operadores/lista.html', {'operadores': operadores})


@login_required
def operador_crear(request):
    if request.method == 'POST':
        form = OperadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('operadores_lista')
    else:
        form = OperadorForm()
    return render(request, 'operadores/form.html', {'form': form, 'titulo': 'Nuevo operador'})


@login_required
def operador_editar(request, pk):
    operador = get_object_or_404(Operador, pk=pk)
    if request.method == 'POST':
        form = OperadorForm(request.POST, instance=operador)
        if form.is_valid():
            form.save()
            return redirect('operadores_lista')
    else:
        form = OperadorForm(instance=operador)
    return render(request, 'operadores/form.html', {'form': form, 'titulo': 'Editar operador'})


@login_required
def operador_detalle(request, pk):
    operador = get_object_or_404(Operador.objects.select_related('usuario'), pk=pk)
    return render(request, 'operadores/detalle.html', {'operador': operador})


@login_required
def operador_baja(request, pk):
    operador = get_object_or_404(Operador, pk=pk)
    if request.method == 'POST':
        operador.activo = False
        operador.save(update_fields=['activo'])
        return redirect('operadores_lista')
    # fallback sencillo: confirmar
    return render(request, 'operadores/confirm_baja.html', {'operador': operador})


@login_required
def operador_activar(request, pk):
    operador = get_object_or_404(Operador, pk=pk)
    if request.method == 'POST':
        operador.activo = True
        operador.save(update_fields=['activo'])
        return redirect('operadores_lista')
    return redirect('operadores_lista')
