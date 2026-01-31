import uuid
import datetime
from sqlalchemy import Column, String, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.models.base import Base

class Order(Base):
    """Modelo para representar una orden de compra."""
    __tablename__ = 'orders'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(120), nullable=False)
    product_id = Column(UUID(as_uuid=True), ForeignKey('products.id'), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now)

    # Relación con el modelo Product
    product = relationship("Product", backref="orders")

    def __repr__(self):
        return f'<Order {self.id}>'
