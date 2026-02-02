# Dockerización del Monorepo (MiniCommerce)

Se añadieron Dockerfiles para backend (Flask) y frontend (Angular), un `docker-compose.yml` y archivos `.dockerignore` para facilitar el despliegue local.

Resumen de lo creado:
- backend/Dockerfile: Imagen basada en python:3.12-slim, instala dependencias y ejecuta la aplicación con gunicorn en el puerto 5000.
- frontend/Dockerfile: Build con node:20-alpine y sirve la app estática con nginx en el puerto 80 (mapeado al host 4200).
- docker-compose.yml: Orquestra tres servicios: `db` (Postgres), `backend` (Flask) y `frontend` (Nginx). La base de datos persiste en un volumen `db_data`.

Variables importantes:
- La conexión a la DB usada por la app es: `DATABASE_URL=postgresql://postgres:postgres@db:5432/minicommerce` (configurada en docker-compose).
- Para enviar correos, agregar un archivo `.env` en la raíz con: `MAIL_SERVER`, `MAIL_PORT`, `MAIL_USERNAME`, `MAIL_PASSWORD`, `MAIL_DEFAULT_SENDER`, y ejecutar `docker compose --env-file .env up -d`.

Comandos rápidos:
1) Construir imágenes y levantar contenedores:

   docker compose build
   docker compose up -d

2) Ver logs:

   docker compose logs -f

3) Detener y eliminar contenedores y volúmenes de datos:

   docker compose down -v

Accesos:
- Frontend: http://localhost:4200
- Backend (API): http://localhost:5000/api
- PostgreSQL: localhost:5432 (user: postgres, password: postgres, db: minicommerce)

Notas:
- El backend crea las tablas automáticamente al iniciar (init_db en la fábrica de la app).
- Si se requieren cambios en la configuración (por ejemplo credenciales de correo), usar un `.env` y pasar con `--env-file` o configurar variables del sistema antes de ejecutar `docker compose`.
- Si el recruiter necesita ver la app rápidamente en su máquina, indicarle ejecutar los comandos de "Comandos rápidos".

Si quieres, puedo: agregar un `Makefile` con atajos, añadir un `healthcheck` para los servicios o preparar una imagen optimizada para producción (multi-stage para Python).