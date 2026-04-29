import cv2
from deepface import DeepFace
import logging

# Configuramos un logger para ver mensajes informativos en la consola
logging.basicConfig(level=logging.INFO)

def run_test():
    # 1. ACCESO A LA CÁMARA
    # '0' le indica a OpenCV que use la cámara web integrada por defecto.
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: No se pudo acceder a la cámara. Revisa si otra app la está usando.")
        return

    print("--- Prueba de Cámara iniciada ---")
    print("Instrucciones: Mírate en la cámara. Presiona 'q' para cerrar la prueba.")

    while True:
        # 2. CAPTURA DE IMAGEN (FRAME)
        # 'ret' es un booleano (True/False) que dice si la captura fue exitosa.
        # 'frame' es la imagen real capturada en ese instante.
        ret, frame = cap.read()
        if not ret:
            print("Error al capturar el video.")
            break

        try:
            # 3. DETECCIÓN DE ROSTROS CON IA
            # extract_faces busca caras en la imagen actual.
            # 'detector_backend=opencv' es el método más rápido para tiempo real.
            # 'enforce_detection=False' evita que el programa falle si no hay nadie frente a la cámara.
            results = DeepFace.extract_faces(
                img_path=frame, 
                detector_backend='opencv', 
                enforce_detection=False
            )

            # 4. DIBUJAR RESULTADOS
            # Si DeepFace encuentra algo, nos da las coordenadas (x, y, ancho, alto).
            for res in results:
                face_area = res["facial_area"]
                x, y, w, h = face_area["x"], face_area["y"], face_area["w"], face_area["h"]
                
                # Dibujamos un rectángulo verde (0, 255, 0) alrededor de la cara detectada.
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                
                # Ponemos un pequeño texto arriba del cuadro.
                cv2.putText(frame, "IA: Rostro Detectado", (x, y - 10), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        except Exception as e:
            # Si ocurre un error técnico en la IA, lo ignoramos para que el video siga fluyendo.
            pass

        # 5. MOSTRAR EL VIDEO
        # Crea una ventana llamada 'BioGuard AI' con el video procesado.
        cv2.imshow('BioGuard AI - Prueba de Detección', frame)

        # 6. CONDICIÓN DE SALIDA
        # Espera 1 milisegundo. Si detecta la tecla 'q', rompe el ciclo.
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 7. LIMPIEZA
    # Muy importante: liberamos la cámara para que otras apps puedan usarla.
    cap.release()
    cv2.destroyAllWindows()
    print("Prueba finalizada con éxito.")

if __name__ == "__main__":
    run_test()
