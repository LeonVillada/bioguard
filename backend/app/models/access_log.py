from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from datetime import datetime
from app.db.session import Base

class AccessLog(Base):
    """
    Guarda el historial de cada intento de acceso al sistema.
    """
    __tablename__ = "access_logs"

    id = Column(Integer, primary_key=True, index=True)
    
    # Relación con el usuario (si fue identificado)
    # Puede ser NULL si es una persona desconocida
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    
    # Fecha y hora exacta del intento
    timestamp = Column(DateTime, default=datetime.utcnow)

    # ¿Fue exitoso el acceso?
    access_granted = Column(Boolean, default=False)

    # Motivo (ej. "Reconocido", "Falla en Liveness", "Desconocido")
    reason = Column(String)

    # Ruta a la foto capturada en el momento (evidencia)
    snapshot_path = Column(String, nullable=True)

    def __repr__(self):
        return f"<AccessLog(timestamp='{self.timestamp}', granted={self.access_granted})>"
