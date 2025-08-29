# Sistema de Gestión de Bienes Patrimoniales — Estado Actual del Proyecto

Este documento resume de forma clara, concisa y práctica el estado actual del proyecto, su arquitectura, endpoints, modelos, vistas, formularios, templates, configuración y mejoras sugeridas.

## 1. Visión General
- Proyecto Django para gestión de bienes patrimoniales.
- Apps principales: `bienes` (negocio) y `usuarios` (placeholder).
- Autenticación vía Django `auth` con vistas genéricas de login/logout.
- Base de datos: MySQL.

## 2. Stack y Dependencias
Archivo: `requirements.txt`
- Django 5.2.5
- mysqlclient 2.2.7
- asgiref, sqlparse, typing_extensions, tzdata
Frontend: Bootstrap 5 por CDN.

## 3. Estructura Relevante
- Proyecto: `bienesPatrimoniales/`
  - Configuración: `bienesPatrimoniales/settings.py`, `bienesPatrimoniales/urls.py`
- App negocio: `bienes/`
  - Modelos: `bienes/models.py`
  - Formularios: `bienes/forms.py`
  - Vistas: `bienes/views.py`
  - URLs: `bienes/urls.py`
  - Admin: `bienes/admin.py`
  - Migraciones: `bienes/migrations/`
- App usuarios: `usuarios/` (modelos y vistas vacíos)
- Templates: `templates/` (auth, bienes, operadores, includes, base)
- Estáticos: `static/panel/css`, `static/panel/js`
- Docs: `.docs/` y `README.md`

## 4. Configuración (settings)
Archivo: `bienesPatrimoniales/settings.py`
- INSTALLED_APPS: `usuarios`, `bienes.apps.BienesConfig`, Django core.
- Base de datos (MySQL): NAME `bienes_patrimoniales_db`, HOST `127.0.0.1`, PORT `3306`, credenciales en texto plano.
- Templates: directorio raíz `templates/`.
- Estáticos: `STATICFILES_DIRS = ['static']`.
- Media: `MEDIA_URL = '/media/'`, `MEDIA_ROOT = 'media'`.
- Autenticación: `LOGIN_URL='login'`, `LOGIN_REDIRECT_URL='dashboard'`, `LOGOUT_REDIRECT_URL='login'`.
- Localización: `LANGUAGE_CODE='es'`, `TIME_ZONE='America/Argentina/Buenos_Aires'`.
- Estado: `DEBUG=True`, `ALLOWED_HOSTS=[]`.

## 5. Modelos (bienes/models.py)
- `Bien`
  - Campos: `nombre`, `descripcion`, `codigo_patrimonial` (único), `fecha_adquisicion`, `valor`, `cuenta_codigo`, `tipo_origen` (choices), `estado` (choices), `fecha_baja`, `motivo_baja`, `ubicacion`, timestamps.
  - Choices `tipo_origen`: DONACION, OMISION, TRANSFERENCIA, COMPRA.
  - Choices `estado`: ACTIVO, BAJA, TRANSFERIDO, MANTENIMIENTO.
  - Orden: `-fecha_creacion`.
- `Perfil`
  - OneToOne con `User`. Campos: `tipo_usuario` (administrador/operador), `telefono`, `fecha_nacimiento`, `direccion`, timestamp.
  - Propiedades: `es_administrador`, `es_operador`.
  - Señales `post_save`: crea/actualiza perfil al crear/guardar `User`.
- `Operador`
  - OneToOne con `User` (`usuario`). ManyToMany `bienes_asignados` con `Bien`.
  - `activo` (bool), `fecha_creacion`. Orden `-fecha_creacion`.

## 6. Formularios (bienes/forms.py)
- `BienForm`: ModelForm completo con widgets Bootstrap.
- `OperadorForm`: campos `usuario`, `bienes_asignados` (SelectMultiple), `activo`.
- `BajaBienForm`: campos `fecha_baja`, `motivo_baja`.

## 7. Vistas (bienes/views.py)
Todas con `@login_required`.

Panel:
- `dashboard(request)`: renderiza `panel/dashboard.html` con `stats` de ejemplo (plantilla aún no creada).

Bienes (CRUD):
- `bienes_lista`: lista de bienes → `templates/bienes/lista.html`.
- `bien_crear`: alta con `BienForm` → `templates/bienes/form.html`.
- `bien_editar`: edición por `pk` → `templates/bienes/form.html`.
- `bien_eliminar`: confirmación y borrado → `templates/bienes/confirm_delete.html`.
- `bien_baja`: setea `estado='BAJA'`, define `fecha_baja` si falta, usa `BajaBienForm` → `templates/bienes/baja.html`.

Operadores:
- `operadores_lista`: tabla de operadores → `templates/operadores/lista.html`.
- `operador_crear` / `operador_editar`: `OperadorForm` → `templates/operadores/form.html`.
- `operador_detalle`: muestra datos y bienes asignados → `templates/operadores/detalle.html`.
- `operador_baja`: marca `activo=False` con confirmación → `templates/operadores/confirm_baja.html`.
- `operador_activar`: marca `activo=True` (redirect a lista).

## 8. URLs
Archivo: `bienesPatrimoniales/urls.py`
- `admin/` → Admin Django
- `login/` (GET/POST) → `auth.LoginView` (`templates/auth/login.html`)
- `logout/` (POST) → `auth.LogoutView`
- `/` → login (redirige a dashboard si autenticado)
- `dashboard/` → `bienes.views.dashboard`
- `bienes/` → incluye `bienes/urls.py`

Archivo: `bienes/urls.py`
- `''` → `bienes_lista`
- `'nuevo/'` → `bien_crear`
- `'<int:pk>/editar/'` → `bien_editar`
- `'<int:pk>/eliminar/'` → `bien_eliminar`
- `'<int:pk>/baja/'` → `bien_baja`
- `'operadores/'` → `operadores_lista`
- `'operadores/nuevo/'` → `operador_crear`
- `'operadores/<int:pk>/'` → `operador_detalle`
- `'operadores/<int:pk>/editar/'` → `operador_editar`
- `'operadores/<int:pk>/baja/'` → `operador_baja`
- `'operadores/<int:pk>/activar/'` → `operador_activar`

## 9. Templates Clave
Layout:
- `templates/base.html`: base Bootstrap, incluye `templates/includes/navbar.html`.
- `templates/includes/navbar.html`: enlaces a `dashboard`, `bienes`, `operadores`, login/logout.

Auth:
- `templates/auth/login.html`: formulario de ingreso con mensajes de error.

Bienes:
- `templates/bienes/lista.html`: tabla de bienes (código, nombre, cuenta, origen, estado, valor, fecha) y acciones.
- `templates/bienes/form.html`: formulario de alta/edición.
- `templates/bienes/confirm_delete.html`: confirmación de eliminación.
- `templates/bienes/baja.html`: formulario de baja (fecha/motivo).

Operadores:
- `templates/operadores/lista.html`: tabla de operadores.
- `templates/operadores/form.html`: crear/editar operador.
- `templates/operadores/detalle.html`: datos + bienes asignados.
- `templates/operadores/confirm_baja.html`: confirmación de baja.

Faltante:
- `templates/panel/dashboard.html` (referido por `dashboard()`).

## 10. Admin (bienes/admin.py)
- Sustituye el registro de `User` por `UsuarioPersonalizadoAdmin` con inlines:
  - `PerfilInline` (StackedInline, no borrable).
  - `OperadorInline` (StackedInline, no borrable, `filter_horizontal` en bienes asignados).
- `BienAdmin`: listados, filtros, búsqueda, `fieldsets`, timestamps readonly.
- `OperadorAdmin`: listados, filtros, búsqueda, `filter_horizontal`, jerarquía por fecha.

## 11. Autenticación y Seguridad
- `@login_required` en vistas de negocio.
- Riesgos actuales:
  - `SECRET_KEY` hardcodeado en `settings.py`.
  - Credenciales MySQL en texto plano en `settings.py`.
  - `DEBUG=True` y `ALLOWED_HOSTS=[]`.

## 12. Datos y Migraciones
- Migraciones en `bienes/migrations/` (inicial y posteriores).
- `usuarios/` sin modelos propios por ahora.

## 13. Ejecución y Desarrollo
Archivo: `README.md` — contiene guía detallada para:
- Crear y activar `venv`.
- Instalar dependencias.
- Configurar MySQL y credenciales en `settings.py`.
- Ejecutar `migrate`, `createsuperuser`, `runserver`.
- Accesos: `/admin/`, `/login` → `/dashboard`.

## 14. Endpoints (Referencia Rápida)
Autenticación:
- `GET /login/`, `POST /login/`
- `POST /logout/`

Panel:
- `GET /dashboard/`

Bienes:
- `GET /bienes/`
- `GET|POST /bienes/nuevo/`
- `GET|POST /bienes/<pk>/editar/`
- `GET|POST /bienes/<pk>/eliminar/`
- `GET|POST /bienes/<pk>/baja/`

Operadores:
- `GET /bienes/operadores/`
- `GET|POST /bienes/operadores/nuevo/`
- `GET /bienes/operadores/<pk>/`
- `GET|POST /bienes/operadores/<pk>/editar/`
- `GET|POST /bienes/operadores/<pk>/baja/`
- `POST /bienes/operadores/<pk>/activar/` (GET redirige)

## 15. Pendientes y Mejoras Sugeridas
- Crear `templates/panel/dashboard.html` (mínimo viable) o ajustar `dashboard()` a una plantilla existente.
- Seguridad y configuración:
  - Mover `SECRET_KEY`, `DEBUG`, `DB USER` y `DB PASSWORD` a variables de entorno.
  - Definir `ALLOWED_HOSTS` correctos.
- Dashboard: reemplazar métricas dummy por consultas reales (totales, por estado, por origen, etc.).
- Validaciones de dominio: asegurar `valor >= 0`; mantener `codigo_patrimonial` único (ya está).
- UX: considerar confirmación previa al `bien_baja` similar a operadores; mensajes de éxito.
- Tests: unit tests de modelos (choices/constraints), vistas (CRUD), permisos.
- Organización: decidir si mover `Perfil`/`Operador` a la app `usuarios` para coherencia.

---
Documento generado automáticamente para facilitar mantenimiento, on-boarding y revisión.
