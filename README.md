# Sistema de Gestión de Bienes Patrimoniales

Este proyecto es un sistema para gestionar los bienes patrimoniales de una institución, desarrollado con Django.

## Guía de Instalación Detallada

Esta guía cubre todos los pasos necesarios para configurar y ejecutar el proyecto en un entorno de desarrollo local.

### Paso 1: Requisitos Previos

Antes de empezar, verifica que tienes instalado el siguiente software:

- **Python**: Versión 3.10 o superior. Puedes verificar tu versión con `python --version`.
- **Git**: Para clonar el repositorio. Puedes verificarlo con `git --version`.
- **MySQL**: El servidor de base de datos. Asegúrate de que el servicio esté en ejecución.

### Paso 2: Clonar el Repositorio

Obtén una copia local del proyecto desde GitHub.

```bash
# Clona el repositorio desde la URL proporcionada
git clone https://github.com/Junixza/bienesPatrimoniales.git

# Navega al directorio del proyecto
cd bienesPatrimoniales
```

### Paso 3: Configurar el Entorno Virtual

Para mantener las dependencias del proyecto aisladas, crearemos un entorno virtual.

```bash
# Crea un directorio para el entorno virtual llamado 'venv'
python -m venv venv

# Activa el entorno virtual
# En Windows (PowerShell):
.\venv\Scripts\Activate.ps1
# En macOS/Linux:
source venv/bin/activate
```

> **Nota:** El archivo `.gitignore` del proyecto ya está configurado para ignorar el directorio `venv`, por lo que no se subirá al repositorio.

### Paso 4: Instalar las Dependencias

El archivo `requirements.txt` contiene la lista de todas las librerías de Python que el proyecto necesita. Instálalas con pip.

```bash
# Asegúrate de tener el entorno virtual activado
pip install -r requirements.txt
```

### Paso 5: Configuración de la Base de Datos MySQL

Este es un paso crucial. Necesitamos crear la base de datos y un usuario con los permisos adecuados.

1.  **Accede a MySQL** como usuario root para tener permisos de administrador.
    ```bash
    mysql -u root -p
    ```

2.  **Crea la base de datos** para el proyecto.
    ```sql
    CREATE DATABASE bienes_patrimoniales_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
    ```

3.  **Crea un usuario dedicado** para que la aplicación Django acceda a la base de datos (reemplaza `'password'` con una contraseña segura).
    ```sql
    CREATE USER 'bienes_user'@'localhost' IDENTIFIED BY 'password';
    ```

4.  **Otorga todos los permisos** necesarios al nuevo usuario sobre la base de datos que creaste.
    ```sql
    GRANT ALL PRIVILEGES ON bienes_patrimoniales_db.* TO 'bienes_user'@'localhost';
    ```

5.  **Refresca los privilegios** de MySQL para que los cambios surtan efecto y sal de la consola.
    ```sql
    FLUSH PRIVILEGES;
    EXIT;
    ```

6.  **Actualiza `settings.py`**: Abre el archivo `bienesPatrimoniales/settings.py` y modifica la sección `DATABASES` con los datos que acabas de crear.
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'bienes_patrimoniales_db', # El nombre de la BD que creaste
            'USER': 'bienes_user',            # El usuario que creaste
            'PASSWORD': 'password',         # La contraseña que asignaste
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }
    ```

### Paso 6: Inicializar la Aplicación

Ahora que todo está configurado, vamos a preparar la base de datos de Django y a crear tu cuenta de administrador.

```bash
# Ejecuta las migraciones para crear las tablas de Django en tu BD
python manage.py migrate

# Crea un superusuario para acceder al panel de administración
python manage.py createsuperuser
```

### Paso 7: Ejecutar el Proyecto

Finalmente, inicia el servidor de desarrollo de Django.

```bash
python manage.py runserver
```

La aplicación estará disponible en `http://127.0.0.1:8000/`.

-   **Panel de Administración**: `http://127.0.0.1:8000/admin/`

## Ejecutar el Proyecto para Desarrollo

Una vez que hayas completado la instalación inicial, sigue estos pasos cada vez que quieras trabajar en el proyecto:

1. **Navega al directorio del proyecto** (si no estás ya en él):
   ```bash
   cd ruta/al/proyecto/bienesPatrimoniales
   ```

2. **Activa el entorno virtual** (siempre es necesario antes de trabajar):
   ```bash
   # En Windows (PowerShell):
   .\venv\Scripts\Activate.ps1
   
   # En macOS/Linux:
   source venv/bin/activate
   ```

3. **Asegúrate de que el servidor MySQL esté en ejecución**
   - Verifica que el servicio de MySQL esté activo en tu sistema.
   - Si no está activo, inicia el servicio.
   - En Windows, puedes iniciar el servicio de MySQL desde el Panel de Control.
   - En Linux, puedes iniciar el servicio de MySQL desde el terminal con el siguiente comando:
   ```bash
   sudo service mysql start
   ```
    Revisa el puerto de MySQL en el archivo de configuración de la base de datos
    y que coincida el puerto en el que esta corriendo MySQL.
    podes verificarlo con el siguiente comando en windows:
    ```bash
    netstat -ano | findstr :3306 --> puerto por defecto de mysql
    ```
    en linux con el comando:
    ```bash
    sudo netstat -tulpn | grep mysql 
    ```
4. **Inicia el servidor de desarrollo de Django desde donde esta el archivo manage.py**:
   ```bash
   python manage.py runserver
   ```

5. **Accede a la aplicación** en tu navegador:
   - Página principal: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
   - Panel de administración: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

### Comandos útiles durante el desarrollo:

- **Detener el servidor**: Presiona `Ctrl+C` en la terminal donde se está ejecutando el servidor.
- **Desactivar el entorno virtual**: 
    Cuando termines de trabajar, puedes desactivar el entorno virtual en windows con:
    ```bash
    deactivate
    ```
    y en linux con:
    ```bash
    deactivate
    ```
- **Ver errores**: Revisa la salida en la terminal donde se ejecuta el servidor para ver mensajes de error o advertencias.
