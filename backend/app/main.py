import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_cors import CORS

# Importar la configuración y la función de inicialización de la BD
from app import config
from app.models.base import init_db, db_session

# Inicialización de extensiones de Flask
db = SQLAlchemy()
mail = Mail()

def create_app():
    """
    Factory para la creación y configuración de la aplicación Flask.
    """
    app = Flask(__name__)
    
    # Cargar configuración desde el archivo config.py
    app.config.from_object(config)

    # --- Inicialización de Extensiones ---
    # Inicializar SQLAlchemy para la gestión de la base de datos.
    db.init_app(app)
    # Inicializar Flask-Mail para el envío de correos.
    mail.init_app(app)
    # Inicializar Flask-CORS para permitir peticiones desde el frontend.
    CORS(app, resources={r"/api/*": {"origins": "*"}}) # Se permite cualquier origen para la API

    # --- Creación de la Base de Datos ---
    # `with app.app_context()` asegura que la aplicación esté activa
    # para operaciones como la creación de tablas.
    with app.app_context():
        # Llama a la función que crea las tablas de la base de datos
        # si estas no existen.
        init_db()
        # Inserta productos por defecto si la tabla está vacía (seed)
        try:
            from app.services.product_service import ProductService
            ProductService.seed_products()
        except Exception:
            # No detener el arranque si falla el seeding
            pass

    # --- Registro de Blueprints (Rutas) ---
    # Importar los blueprints que contienen las rutas de la aplicación.
    from app.routes.product_routes import product_bp
    from app.routes.order_routes import order_bp
    
    # Registrar los blueprints en la aplicación, añadiendo un prefijo a las URLs.
    app.register_blueprint(product_bp, url_prefix='/api')
    app.register_blueprint(order_bp, url_prefix='/api')

    # --- Manejo de Sesión de Base de Datos ---
    # Hook que se ejecuta al final de cada request para cerrar la sesión de SQLAlchemy.
    # Esto libera los recursos de la base de datos de manera segura.
    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()

    return app
