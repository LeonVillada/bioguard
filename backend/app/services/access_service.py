from sqlalchemy.orm import Session
from app.models.user import User
from app.models.access_log import AccessLog
from app.core.face_engine import face_engine
import json
import numpy as np

def verify_access(db: Session, image_path: str):
    """
    Verifica si la persona en la imagen tiene acceso permitido.
    """
    # 1. Obtenemos los números de la cara actual
    current_embedding = face_engine.get_face_embedding(image_path)
    
    if current_embedding is None:
        return {"status": "denied", "reason": "No se detectó rostro"}

    # 2. Traemos a todos los usuarios registrados del baúl
    users = db.query(User).all()
    
    best_match = None
    # Para Similitud de Coseno, 0.4 es un excelente punto de equilibrio
    # Menos de 0.4 significa que las caras son MUY parecidas.
    min_distance = 0.4 

    # 3. Comparamos usando Similitud de Coseno (más profesional)
    curr_vec = np.array(current_embedding)
    
    for user in users:
        saved_vec = np.array(json.loads(user.face_encoding))
        
        # Fórmula de Similitud de Coseno
        dot_product = np.dot(curr_vec, saved_vec)
        norm_curr = np.linalg.norm(curr_vec)
        norm_saved = np.linalg.norm(saved_vec)
        cosine_distance = 1 - (dot_product / (norm_curr * norm_saved))
        
        print(f"DEBUG: Comparando con {user.name} - Distancia: {cosine_distance:.4f}")

        if cosine_distance < min_distance:
            min_distance = cosine_distance
            best_match = user

    # 4. Resultado final
    if best_match:
        # Si lo encontramos, anotamos el éxito en el cuaderno (Logs)
        new_log = AccessLog(user_id=best_match.id, access_granted=True, reason="Reconocido")
        db.add(new_log)
        db.commit()
        return {"status": "granted", "user": best_match.name}
    else:
        # Si no lo conocemos, anotamos el fallo
        new_log = AccessLog(access_granted=False, reason="Desconocido")
        db.add(new_log)
        db.commit()
        return {"status": "denied", "reason": "Persona no autorizada"}
