from app.models.order import Order
from app.models.product import Product
from app.models.base import db_session
from app.services.product_service import ProductService
from flask_mail import Message
from app.main import mail
import threading
from flask import current_app

class OrderService:
    """
    Capa de servicio para la lógica de negocio relacionada con las órdenes.
    """

    @staticmethod
    def create_order(data):
        """
        Crea una nueva orden, la guarda en la base de datos y envía un email de confirmación.
        
        Args:
            data: Un diccionario con los datos de la orden (name, last_name, email, product_id).
            
        Returns:
            El objeto Order creado.
        """
        # Extraer datos del diccionario de entrada.
        name = data.get('name')
        last_name = data.get('last_name')
        email = data.get('email')
        product_id = data.get('product_id')

        # Validar que el producto exista antes de crear la orden.
        product = ProductService.get_product_by_id(product_id)
        if not product:
            raise ValueError("El producto especificado no existe.")

        # Crear una nueva instancia del modelo Order.
        new_order = Order(
            name=name,
            last_name=last_name,
            email=email,
            product_id=product.id
        )

        # Añadir la nueva orden a la sesión de la base de datos y confirmar la transacción.
        db_session.add(new_order)
        db_session.commit()
        
        # Enviar el email de confirmación en un hilo separado para no bloquear la respuesta HTTP.
        # Se pasa `current_app._get_current_object()` para que el hilo tenga acceso al contexto de la app.
        thread = threading.Thread(target=OrderService.send_confirmation_email, args=(current_app._get_current_object(), new_order, product))
        thread.start()

        return new_order

    @staticmethod
    def send_confirmation_email(app, order, product):
        """
        Envía un email de confirmación de compra.
        Se ejecuta en un contexto de aplicación para poder usar Flask-Mail.
        
        Args:
            app: El objeto de la aplicación Flask.
            order: La orden que fue creada.
            product: El producto que fue comprado.
        """
        with app.app_context():
            # Asunto del correo.
            subject = "Confirmación de compra - MiniCommerce"
            
            # Contenido del correo.
            body = (
                f"Hola {order.name},\n\n"
                f"Tu compra fue confirmada correctamente.\n\n"
                f"Producto: {product.name}\n"
                f"Orden ID: {order.id}\n\n"
                f"Gracias por tu compra.\n"
                f"MiniCommerce Team"
            )
            
            # Crear el objeto Message.
            sender = app.config.get('MAIL_DEFAULT_SENDER') or 'no-reply@minicommerce.local'
            msg = Message(
                subject,
                sender=sender,
                recipients=[order.email],
                body=body
            )
            
            # Enviar el mensaje.
            mail.send(msg)
