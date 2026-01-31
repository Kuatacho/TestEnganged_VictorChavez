from flask import Blueprint, request, jsonify
from app.services.order_service import OrderService

# Crear un Blueprint para la ruta de creación de órdenes.
order_bp = Blueprint('order_bp', __name__)

@order_bp.route('/orders', methods=['POST'])
def create_order():
    """
    Endpoint para crear una nueva orden.
    Valida la entrada, llama al servicio de órdenes y devuelve una respuesta.
    """
    # Obtener los datos JSON de la solicitud.
    data = request.get_json()

    # Validación de los datos de entrada.
    if not data or not all(k in data for k in ('name', 'last_name', 'email', 'product_id')):
        return jsonify({'message': 'Faltan datos requeridos en el JSON'}), 400

    try:
        # Llama al servicio para procesar la creación de la orden.
        order = OrderService.create_order(data)
        
        # Formatea la respuesta con los datos de la orden recién creada.
        response_data = {
            'id': str(order.id),
            'name': order.name,
            'last_name': order.last_name,
            'email': order.email,
            'product_id': str(order.product_id),
            'created_at': order.created_at.isoformat()
        }
        return jsonify({'message': 'Orden creada exitosamente', 'order': response_data}), 201
    
    except ValueError as e:
        # Captura errores de validación del servicio (ej. producto no existente).
        return jsonify({'message': str(e)}), 404
    
    except Exception as e:
        # Captura cualquier otro error inesperado.
        return jsonify({'message': f'Ocurrió un error en el servidor: {e}'}), 500