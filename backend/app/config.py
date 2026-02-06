import os
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Clave secreta para la aplicación
SECRET_KEY = os.environ.get('SECRET_KEY') or 'misecreto123'

# Configuración de la base de datos PostgreSQL
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://user:password@localhost/dbname'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Helper para parsear booleanos desde variables de entorno
def _env_bool(key, default=False):
    val = os.environ.get(key)
    if val is None:
        return default
    return str(val).lower() in ('1', 'true', 'yes', 'on')

# Configuración de Flask-Mail
MAIL_SERVER = os.environ.get('MAIL_SERVER') or None
MAIL_PORT = int(os.environ.get('MAIL_PORT') or 587)
MAIL_USE_TLS = _env_bool('MAIL_USE_TLS', False)
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER') or 'no-reply@minicommerce.local'
MAIL_SUPPRESS_SEND = _env_bool('MAIL_SUPPRESS_SEND', False)

# Configuración de modo debug
DEBUG = os.environ.get('FLASK_DEBUG') is not None
