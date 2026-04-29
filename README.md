# 🛡️ BioGuard AI - Facial Security System

**BioGuard AI** es una plataforma de seguridad biométrica de nivel profesional que integra Inteligencia Artificial avanzada para el reconocimiento facial y la gestión de accesos en tiempo real. 

Este proyecto fue diseñado bajo principios de **Arquitectura Limpia** (Clean Architecture), separando la lógica de procesamiento de visión artificial de la interfaz de usuario.

---

## 🚀 Características Principales

*   **Reconocimiento Facial 1:N**: Identificación de usuarios mediante embeddings vectoriales utilizando el modelo `Facenet512`.
*   **Procesamiento de IA con DeepFace**: Extracción de rasgos biométricos con alta precisión y tolerancia a variaciones de iluminación.
*   **Dashboard Moderno**: Interfaz de usuario "Glassmorphism" construida con Next.js 14+, ofreciendo una experiencia fluida y responsive.
*   **Asistente de Registro Biométrico**: Proceso guiado paso a paso con previsualización en tiempo real y guías de posicionamiento.
*   **Base de Datos Vectorial**: Almacenamiento eficiente de encodings faciales mediante SQLAlchemy y SQLite.
*   **API Robusta**: Backend desarrollado con FastAPI para una comunicación de baja latencia.

---

## 🛠️ Stack Tecnológico

### Backend (Cerebro de IA)
*   **Python 3.10+**
*   **FastAPI**: Framework web de alto rendimiento.
*   **DeepFace (TensorFlow/Keras)**: Para el análisis biométrico.
*   **OpenCV**: Procesamiento de frames de video.
*   **SQLAlchemy**: ORM para gestión de base de datos.
*   **NumPy**: Operaciones matemáticas vectoriales (Similitud de Coseno).

### Frontend (Interfaz de Usuario)
*   **Next.js 14+ (App Router)**
*   **React hooks**: Gestión de estados complejos y ciclo de vida de la cámara.
*   **Tailwind CSS**: Diseño moderno y estilizado.
*   **Lucide React**: Iconografía profesional.

---

## 📂 Estructura del Proyecto

```bash
bioguard_ai/
├── backend/            # Lógica de IA y API (FastAPI)
│   ├── app/
│   │   ├── core/       # Motores de IA y Visión
│   │   ├── services/   # Lógica de negocio (Registro/Verificación)
│   │   ├── models/     # Modelos de Base de Datos
│   │   └── db/         # Configuración de persistencia
├── frontend/           # Interfaz de Usuario (Next.js)
│   ├── app/            # Dashboard y Componentes
│   └── public/         # Activos estáticos
└── data/               # Almacenamiento de base de datos (ignorado en Git)
```

---

## 🛠️ Instalación y Configuración

### 1. Clonar el repositorio
```bash
git clone https://github.com/tu-usuario/bioguard_ai.git
cd bioguard_ai
```

### 2. Configurar el Backend
```bash
cd backend
python -m venv venv
source venv/Scripts/activate  # En Windows: .\backend\venv\Scripts\activate
pip install -r requirements.txt
python app/db/init_db.py     # Inicializar base de datos
uvicorn app.main:app --reload
```

### 3. Configurar el Frontend
```bash
cd ../frontend
npm install
npm run dev
```

---

## ✒️ Autor
*   **Dani Leon** - *Desarrollo de Software e IA*

---

## 📄 Licencia
Este proyecto es de uso libre para fines educativos y portafolio profesional.
