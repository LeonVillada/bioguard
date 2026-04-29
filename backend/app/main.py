from fastapi import FastAPI, Depends, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.services import user_service, access_service
import os
import shutil

app = FastAPI(title="BioGuard AI API", version="1.0.0")

# 1. LISTA DE AMIGOS (CORS)
# Aquí le decimos al backend que confíe en el frontend que corre en el puerto 3000
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], # Permitir todos los métodos (GET, POST, etc.)
    allow_headers=["*"], # Permitir todos los encabezados
)

# Creamos una carpeta temporal para guardar las fotos que nos envíen
UPLOAD_DIR = "data/temp_uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/")
def read_root():
    return {"message": "Bienvenido a BioGuard AI - El servidor está funcionando"}

@app.post("/register")
async def register(name: str, employee_id: str, file: UploadFile = File(...), db: Session = Depends(get_db)):
    """
    Ruta para registrar un nuevo usuario enviando su foto.
    """
    # Guardamos la foto temporalmente
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    # Llamamos a la 'Secretaria' para que haga el registro
    result = user_service.register_new_user(db, name, employee_id, file_path)
    
    # Borramos la foto temporal (por privacidad)
    os.remove(file_path)
    
    return result

@app.post("/verify")
async def verify(file: UploadFile = File(...), db: Session = Depends(get_db)):
    """
    Ruta para que el 'Guardia' verifique si alguien puede pasar.
    """
    # Guardamos la foto temporalmente
    file_path = os.path.join(UPLOAD_DIR, f"verify_{file.filename}")
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    # Llamamos al 'Guardia' para la verificación
    result = access_service.verify_access(db, file_path)
    
    # Borramos la foto temporal
    os.remove(file_path)
    
    return result
