from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from app.config import SQLALCHEMY_DATABASE_URI

# Motor de base de datos conectado a PostgreSQL
engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=False)

# Sesión de base de datos
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

# Base para los modelos declarativos
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    """
    Inicializa la base de datos y crea las tablas si no existen.
    Importa los modelos aquí para que se registren en el metadata de la Base.
    """
    # Importar todos los modelos aquí para que se registren en `Base.metadata`
    from . import product, order
    Base.metadata.create_all(bind=engine)
