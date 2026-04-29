from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# 1. Definimos la ruta de la base de datos
# La guardaremos en la carpeta 'data' que creamos al inicio
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
DB_PATH = os.path.join(BASE_DIR, "data", "bioguard.db")

# 2. Creamos la URL de conexión para SQLite
SQLALCHEMY_DATABASE_URL = f"sqlite:///{DB_PATH}"

# 3. El 'engine' es el motor que habla con el archivo .db
# 'check_same_thread=False' es necesario solo para SQLite en FastAPI
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# 4. SessionLocal es la fábrica de conexiones
# Cada vez que necesitemos guardar o leer algo, pediremos una sesión aquí
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 5. Base es la clase de la que heredarán todos nuestros modelos (tablas)
Base = declarative_base()

# Función para obtener la base de datos (se usará en FastAPI más adelante)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
