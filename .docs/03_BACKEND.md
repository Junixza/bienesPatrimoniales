# Estructura del Backend

## Estructura de Directorios
```
bienesPatrimoniales/
├── bienes/                  # App de negocio
│   ├── migrations/          # Migraciones de la base
│   ├── models.py            # Modelos: Bien, Perfil, Operador
│   ├── forms.py             # Formularios: BienForm, OperadorForm, BajaBienForm
│   ├── views.py             # Vistas: CRUD bienes, operadores, dashboard
│   ├── admin.py             # Admin Django personalizado
│   └── urls.py              # Rutas de la app
│
├── usuarios/                # App placeholder (sin modelos/vistas)
│   ├── models.py
│   └── views.py
│
├── bienesPatrimoniales/     # Configuración del proyecto
│   ├── settings.py          # Settings (MySQL, static, templates)
│   └── urls.py              # Rutas principales (login, dashboard, include bienes)
│
├── templates/               # Plantillas
└── manage.py                # CLI de Django
```

## Tecnologías Principales
- **Python 3.x**: Lenguaje principal
- **Django 5.2**: Framework web
- **MySQL**: Base de datos

## Modelos Principales
1. **Bien**
   - Información de bienes patrimoniales
   - Estado, ubicación, fechas

2. **Usuario/Perfil**
   - Autenticación y autorización
   - Roles: Administrador/Operador

3. **Operador**
   - Relación con usuarios
   - Bienes asignados

## Endpoints Web (actuales)
Ruta raíz en `bienesPatrimoniales/urls.py` + `bienes/urls.py`:
```
# Autenticación
GET /login/              # Login (Django auth)
POST /logout/            # Logout

# Panel
GET /dashboard/          # Dashboard (plantilla pendiente)

# Bienes
GET    /bienes/                      # Listado
GET|POST /bienes/nuevo/              # Alta
GET|POST /bienes/<pk>/editar/        # Edición
GET|POST /bienes/<pk>/eliminar/      # Confirmación + eliminación
GET|POST /bienes/<pk>/baja/          # Formulario de baja

# Operadores
GET       /bienes/operadores/                 # Listado
GET|POST  /bienes/operadores/nuevo/           # Alta
GET       /bienes/operadores/<pk>/            # Detalle
GET|POST  /bienes/operadores/<pk>/editar/     # Edición
GET|POST  /bienes/operadores/<pk>/baja/       # Confirmar baja (activo=False)
POST      /bienes/operadores/<pk>/activar/    # Activar (activo=True)
```

## Seguridad
- Autenticación por sesión
- CSRF Protection
- Validación de datos
- Permisos y grupos

## Notas
- No se expone API REST actualmente.
- No hay tareas asíncronas configuradas.
