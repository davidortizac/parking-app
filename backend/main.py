from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine
from models import Base

# Routers
from routers.usuarios import router as usuarios_router
from routers.vehiculos import router as vehiculos_router
from routers.reservas import router as reservas_router
from routers.dashboard import router as dashboard_router

# Crear estructura de tablas
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Gestión Parqueadero")

# Permitir peticiones desde el frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir routers
app.include_router(usuarios_router)
app.include_router(vehiculos_router)
app.include_router(reservas_router)
app.include_router(dashboard_router)

@app.get("/")
def root():
    return {"message": "API Gestión de Parqueaderos funcionando"}
