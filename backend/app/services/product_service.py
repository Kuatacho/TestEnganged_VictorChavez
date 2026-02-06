from app.models.product import Product
from app.models.base import db_session
import uuid


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

    @staticmethod
    def seed_products():
        """
        Inserta productos por defecto si la tabla está vacía.
        """
        try:
            count = db_session.query(Product).count()
            if count > 0:
                return
            seeds = [
                {
                    'id': '1a2b3c4d-0001-4f5e-aaaa-111111111111',
                    'name': 'Laptop de Alto Rendimiento',
                    'description': 'Laptop potente para gaming y trabajo intensivo',
                    'price': 3200,
                    'image_url': 'https://images.pexels.com/photos/18105/pexels-photo.jpg'
                },
                {
                    'id': '1a2b3c4d-0002-4f5e-aaaa-222222222222',
                    'name': 'PC Gamer Completa',
                    'description': 'PC de escritorio con hardware gaming',
                    'price': 2800,
                    'image_url': 'https://volttierpc.com/7218-home_default/pc-gaming-completo-amd-ryzen-5-5500-rx-7600-32gb-ram-1tb-ssd-nvme.jpg'
                },
                {
                    'id': '1a2b3c4d-0003-4f5e-aaaa-333333333333',
                    'name': 'Monitor 27" UHD',
                    'description': 'Monitor de alta resolución para diseño y gaming',
                    'price': 750,
                    'image_url': 'https://i5.walmartimages.com/seo/Dell-Plus-S2725QS-27-Class-4K-UHD-LED-Monitor-16-9_08252b5a-b957-4ec4-9ef9-ade0ae7bdb26.d59fd817ecd4fc5285a661566d4acb90.jpeg'
                }
            ]
            for s in seeds:
                p = Product(id=uuid.UUID(s['id']), name=s['name'], description=s['description'], price=s['price'],
                            image_url=s['image_url'])
                db_session.add(p)
            db_session.commit()
        except Exception as e:
            # No detener el arranque si falla el seeding
            print(f'Error seeding products: {e}')
