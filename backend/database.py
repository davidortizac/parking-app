
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Leer la URL de conexión desde el entorno (o usar una por defecto)
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://admin:secret@localhost:5432/parqueadero")

# Crear el motor de conexión
engine = create_engine(DATABASE_URL)

# Crear una clase base para modelos
Base = declarative_base()

# Crear sesión local
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependencia para inyectar la sesión en rutas

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
