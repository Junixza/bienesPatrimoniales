from django.urls import path
from . import views

urlpatterns = [
    path('', views.bienes_lista, name='bienes_lista'),
    path('nuevo/', views.bien_crear, name='bien_crear'),
    path('<int:pk>/editar/', views.bien_editar, name='bien_editar'),
    path('<int:pk>/eliminar/', views.bien_eliminar, name='bien_eliminar'),
    path('<int:pk>/baja/', views.bien_baja, name='bien_baja'),

    # Operadores
    path('operadores/', views.operadores_lista, name='operadores_lista'),
    path('operadores/nuevo/', views.operador_crear, name='operador_crear'),
    path('operadores/<int:pk>/', views.operador_detalle, name='operador_detalle'),
    path('operadores/<int:pk>/editar/', views.operador_editar, name='operador_editar'),
    path('operadores/<int:pk>/baja/', views.operador_baja, name='operador_baja'),
    path('operadores/<int:pk>/activar/', views.operador_activar, name='operador_activar'),
]
