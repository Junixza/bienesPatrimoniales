# Guía de Desarrollo

## Convenciones de Código
### Python
 - PEP 8 estándar
 - Docstrings estilo Google
 - Nombres descriptivos en español latinoamericano
 - Tamaño de indentación: 2 espacios

### JavaScript
- Uso de `const` y `let`
- Funciones flecha
- Nombres en camelCase

### Commits
- Formato convencional: `feat:`, `fix:`, `docs:`, `chore:`, `refactor:`, `test:`
- Mensajes breves y descriptivos en español

### Linteo y estilo
- Mantener código limpio, evitar duplicación
- Agregar comentarios solo cuando aporten claridad

### Pruebas (sugerido)
- Pruebas unitarias para vistas y modelos principales
- Casos: creación/edición/baja de Bien, activación/baja de Operador

## Flujo de Trabajo
1. GitHub Flow: crear rama a partir de `main`:
   ```bash
   git checkout -b feature/nombre-de-la-funcionalidad
   ```
2. Commits pequeños y frecuentes con mensajes claros
3. Abrir Pull Request hacia `main`
4. Revisión y merge tras aprobación y checks verdes