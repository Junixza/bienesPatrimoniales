# Configuración del Proyecto

## Requisitos
- Python 3.10+
- MySQL 8.0+
- (Opcional) Node.js 16+ si se gestionan assets adicionales

## Instalación
1. Clonar el repositorio
2. Crear entorno virtual:
   ```bash
   python -m venv venv
   # En Windows:
   .\venv\Scripts\activate
   # En Linux/Mac:
   source venv/bin/activate
   ```

3. Instalar dependencias
   ```bash
   pip install -r requirements.txt
   ```

4. Configurar variables de entorno (recomendado)
   Crear un archivo `.env` en la raíz del proyecto o exportar variables en tu ambiente:
   ```bash
   # Django
   DJANGO_SECRET_KEY="<una-clave-segura>"
   DJANGO_DEBUG=true
   DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost

   # Base de datos MySQL
   DB_NAME=bienes_patrimoniales_db
   DB_USER=<usuario>
   DB_PASSWORD=<password>
   DB_HOST=127.0.0.1
   DB_PORT=3306
   ```

   Nota: Ajustar `settings.py` para leer estas variables (por ejemplo, con `os.environ.get(...)`).

5. Inicializar base de datos y ejecutar el servidor
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py runserver
   ```