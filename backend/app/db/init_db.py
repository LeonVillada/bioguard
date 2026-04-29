from app.db.session import engine, Base
# Importamos los modelos para que SQLAlchemy sepa que existen antes de crear las tablas
from app.models.user import User
from app.models.access_log import AccessLog

def init_database():
    print("Iniciando creación de tablas en la base de datos...")
    # Este comando crea todas las tablas definidas en los modelos
    Base.metadata.create_all(bind=engine)
    print("¡Base de datos creada exitosamente!")

if __name__ == "__main__":
    init_database()
