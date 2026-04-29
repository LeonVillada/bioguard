from deepface import DeepFace
import numpy as np

class FaceEngine:
    """
    El 'Maestro de las Caras'. 
    Este objeto contiene toda la lógica para procesar rostros.
    """

    def __init__(self, model_name="Facenet512"):
        # Elegimos 'Facenet512' porque es uno de los más precisos del mundo.
        # Crea una firma de 512 números para cada cara.
        self.model_name = model_name

    def get_face_embedding(self, image_path):
        """
        Recibe una imagen y devuelve la 'firma' (vector) del rostro.
        """
        try:
            # Pedimos a DeepFace que extraiga los números de la cara
            # Usamos 'Facenet512' para máxima precisión.
            results = DeepFace.represent(
                img_path=image_path,
                model_name=self.model_name,
                enforce_detection=True,
                detector_backend='opencv'
            )
            
            # Si encuentra una cara, nos devuelve sus números (embedding)
            if results:
                return results[0]["embedding"]
            
            return None
            
        except Exception as e:
            print(f"Error al procesar el rostro: {e}")
            return None

# Creamos una instancia única para usarla en todo el proyecto
face_engine = FaceEngine()
