# Estructura del Frontend

## Directorios Principales
```
static/
└── panel/
    ├── css/            # Estilos propios (referenciados en base.html)
    └── js/             # Scripts propios (referenciados en base.html)

templates/
├── base.html           # Layout base con Bootstrap 5 (CDN)
├── includes/
│   └── navbar.html     # Barra de navegación
├── auth/
│   └── login.html      # Ingreso al sistema
├── bienes/
│   ├── lista.html
│   ├── form.html
│   ├── baja.html
│   └── confirm_delete.html
└── operadores/
    ├── lista.html
    ├── form.html
    ├── detalle.html
    └── confirm_baja.html

# Pendiente: templates/panel/dashboard.html (referido por la vista dashboard)
```

## Tecnologías Principales
- **HTML5**: Estructura de las páginas
- **CSS3**: Estilos y diseño responsivo
- **JavaScript**: Interactividad (scripts mínimos propios)
- **Bootstrap 5**: Framework CSS por CDN

## Flujo de Navegación
1. Página de Inicio de Sesión
2. Dashboard Principal
   - Resumen
   - Gestión de Bienes
   - Gestión de Usuarios
3. Perfil de Usuario

## Componentes Reutilizables
- Barra de navegación
- Tarjetas de resumen
- Formularios
- Tablas de datos
- Modales
- Alertas

## Responsive Design
- Diseño adaptable a móviles
- Menú colapsable
- Grillas flexibles

