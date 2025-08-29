from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from bienes import views as bienes_views
from django.conf import settings
from django.conf.urls.static import static

# -----------------------------------------------------------------------------
# Nota de documentación (modo ejemplo)
# URLconf principal funcional. Se entrega como base/plantilla; ajustar rutas,
# names, middleware y patrones de autenticación/permiso según el proyecto.
# -----------------------------------------------------------------------------
urlpatterns = [
    path('admin/', admin.site.urls),

    # Autenticación
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Home = Login (redirige a dashboard si ya está autenticado)
    path('', auth_views.LoginView.as_view(template_name='auth/login.html', redirect_authenticated_user=True), name='home'),

    # Panel principal
    path('dashboard/', bienes_views.dashboard, name='dashboard'),

    # Bienes (CRUD)
    path('bienes/', include('bienes.urls')),
]

# Archivos de medios en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
