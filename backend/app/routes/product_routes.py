from flask import Blueprint, jsonify
from app.services.product_service import ProductService
import uuid

# Crear un Blueprint para agrupar las rutas de productos.
product_bp = Blueprint('product_bp', __name__)

@product_bp.route('/products', methods=['GET'])
def get_all_products():
    """
    Endpoint para obtener todos los productos.
    Llama directamente al servicio de productos y serializa la respuesta.
    """
    try:
        # Llama al servicio para obtener todos los productos de la base de datos.
        products = ProductService.get_all_products()
        
        # Convierte la lista de objetos SQLAlchemy a un formato JSON serializable.
        product_list = [
            {
                'id': str(p.id),
                'name': p.name,
                'description': p.description,
                'price': p.price,
                'image_url': p.image_url
            } for p in products
        ]
        
        return jsonify(product_list), 200
    except Exception as e:
        # Manejo de errores en caso de que falle la consulta a la base de datos.
        return jsonify({'message': f'Ocurrió un error: {e}'}), 500


@product_bp.route('/products/<uuid:product_id>', methods=['GET'])
def get_product_by_id(product_id):
    """
    Endpoint para obtener un producto específico por su ID.
    """
    try:
        # Llama al servicio para buscar el producto por su ID.
        product = ProductService.get_product_by_id(product_id)
        
        if product:
            # Si se encuentra el producto, lo serializa y lo devuelve.
            product_data = {
                'id': str(product.id),
                'name': product.name,
                'description': product.description,
                'price': product.price,
                'image_url': product.image_url
            }
            return jsonify(product_data), 200
        else:
            # Si no se encuentra, devuelve un error 404.
            return jsonify({'message': 'Producto no encontrado'}), 404
    except Exception as e:
        return jsonify({'message': f'Ocurrió un error: {e}'}), 500