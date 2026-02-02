FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Instalar dependencias del sistema necesarias para psycopg2
RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential libpq-dev gcc dos2unix \
    && rm -rf /var/lib/apt/lists/*

# Copiar e instalar dependencias de Python
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r /app/requirements.txt \
    && pip install --no-cache-dir gunicorn

# Copiar el código de la aplicación
COPY . /app

# Convertir finales de línea a LF y dar permiso
RUN dos2unix /app/start.sh || true
RUN chmod +x /app/start.sh

EXPOSE 5000

CMD ["/app/start.sh"]