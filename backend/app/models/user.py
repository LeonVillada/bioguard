from sqlalchemy import Column, Integer, String, DateTime, Text
from datetime import datetime
from app.db.session import Base

class User(Base):
    """
    Representa a una persona autorizada en el sistema.
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    
    # Nombre completo de la persona
    name = Column(String, nullable=False)
    
    # Identificador único (ej. número de empleado o cédula)
    employee_id = Column(String, unique=True, index=True, nullable=False)

    # El 'Embedding' facial. Se guarda como un texto largo (JSON) 
    # que contiene los vectores matemáticos del rostro.
    face_encoding = Column(Text, nullable=False)

    # Fecha en que se registró por primera vez
    created_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<User(name='{self.name}', employee_id='{self.employee_id}')>"
