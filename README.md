# MiniCommerce — Monorepo (Flask + Angular + PostgreSQL)

MiniCommerce es un MVP de tienda online pensado para demostraciones y pruebas técnicas. La aplicación permite listar productos, ver detalle, realizar un checkout de un solo producto y enviar una confirmación por correo electrónico.

Características (MVP)
- Listado de productos y vista detalle.
- Formulario de compra y creación de orden.
- Envío de correo de confirmación (configurable para MailHog en desarrollo).
- Seed idempotente de productos al arrancar la aplicación (solo si la tabla está vacía).

Tecnologías
- Backend: Flask
- Base de datos: PostgreSQL
- Frontend: Angular
- Dev mail capture: MailHog (incluido en docker-compose)

Estructura del repositorio (resumen)

- backend/
  - app/                # Código Flask (models, services, routes)
  - Dockerfile          # Imagen del backend
  - requirements.txt
- frontend/             # App Angular y Dockerfile para build + Nginx
- docker-compose.yml
- README.md

Comportamiento importante
- Al arrancar (create_app) llama a `init_db()` para crear tablas si no existen y a `ProductService.seed_products()` que inserta 3 productos por defecto solo si la tabla `products` está vacía. Esto evita duplicados en reinicios.

Variables de entorno (ejemplo y valores por defecto usados en docker-compose)

```
DATABASE_URL=postgresql://postgres:postgres@db:5432/minicommerce
FLASK_DEBUG=1
SECRET_KEY=supersecretkey
MAIL_SERVER=mailhog            # en desarrollo usamos MailHog
MAIL_PORT=1025
MAIL_USE_TLS=0
MAIL_USERNAME=
MAIL_PASSWORD=
MAIL_DEFAULT_SENDER=no-reply@minicommerce.local
MAIL_SUPPRESS_SEND=0
```

Ejecución (con Docker)

1) Construir y levantar todo (desde la raíz del repo):

   docker compose up --build -d

2) Ver logs (ej. backend):

   docker compose logs -f backend

3) Parar y eliminar contenedores y volúmenes (útil para forzar re-seed):

   docker compose down -v

4) Usar un archivo `.env` personalizado:

   docker compose --env-file .env up --build -d


Endpoints principales
- Frontend: http://localhost:4200
- API base: http://localhost:5000/api
- GET /api/products — lista de productos
- GET /api/products/<uuid> — detalle de producto
- MailHog UI: http://localhost:8025 (mensajes capturados en dev)

Errores comunes y soluciones rápidas
- SMTPNotSupportedError: "SMTP AUTH extension not supported by server" — sucede cuando se intenta autenticarse contra un servidor que no soporta AUTH o cuando se usa el puerto/TLS incorrecto. Soluciones: en desarrollo usar MailHog (MAIL_SERVER=mailhog, MAIL_PORT=1025). Para SMTP real, habilitar MAIL_USE_TLS=1, configurar MAIL_USERNAME y MAIL_PASSWORD (Gmail requiere app password).

- AssertionError: "The message does not specify a sender" — Flask-Mail requiere un remitente; asegurarse de setear `MAIL_DEFAULT_SENDER` en el `.env` o pasar `sender` al crear el Message (ya soportado en el código).

- Advertencia docker compose "version is obsolete" — se eliminó la clave `version` en docker-compose.yml; usar el plugin moderno `docker compose` (con espacio) o instala la versión compatible si prefieres `docker-compose`.

Consejos para producción
- No usar MailHog; configurar un SMTP real con TLS y credenciales seguras (gestionar secretos fuera del repo). 
- Usar variables de entorno/secret manager y backups del volumen de Postgres.






