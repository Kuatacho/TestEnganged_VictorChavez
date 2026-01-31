from app.models.product import Product
from app.models.base import db_session

class ProductService:
    """
    Capa de servicio para la lógica de negocio relacionada con los productos.
    Separa la lógica de la base de datos de los controladores.
    """

    @staticmethod
    def get_all_products():
        """
        Obtiene todos los productos de la base de datos.
        
        Returns:
            Una lista de objetos Product.
        """
        # Realiza una consulta para obtener todos los registros de la tabla de productos.
        products = db_session.query(Product).all()
        return products

    @staticmethod
    def get_product_by_id(product_id):
        """
        Obtiene un producto específico por su UUID.
        
        Args:
            product_id: El UUID del producto a buscar.
            
        Returns:
            El objeto Product si se encuentra, de lo contrario None.
        """
        # Realiza una consulta para encontrar un producto por su clave primaria.
        product = db_session.query(Product).get(product_id)
        return product
