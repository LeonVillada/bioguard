from sqlalchemy.orm import Session
from app.models.user import User
from app.core.face_engine import face_engine
import json

def register_new_user(db: Session, name: str, employee_id: str, image_path: str):
    """
    Coordina el registro de una nueva persona en el sistema.
    """
    # 1. Le pedimos al Experto que analice la foto y nos dé los números
    embedding = face_engine.get_face_embedding(image_path)
    
    if embedding is None:
        return {"status": "error", "message": "No se detectó un rostro claro en la imagen."}

    # 2. Convertimos la lista de números a texto (JSON) para poder guardarla en la DB
    embedding_json = json.dumps(embedding)

    # 3. Creamos el objeto Usuario con sus datos
    new_user = User(
        name=name,
        employee_id=employee_id,
        face_encoding=embedding_json
    )

    # 4. Usamos el 'Teléfono Mágico' para guardar todo en el baúl
    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return {"status": "success", "user_id": new_user.id, "name": new_user.name}
    except Exception as e:
        db.rollback()
        return {"status": "error", "message": f"Error al guardar en base de datos: {e}"}
