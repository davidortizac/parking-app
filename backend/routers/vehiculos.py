from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models import Vehiculo, Usuario
from database import get_db

router = APIRouter(prefix="/vehiculos", tags=["Vehiculos"])

@router.post("/")
def registrar_vehiculo(vehiculo: Vehiculo, db: Session = Depends(get_db)):
    if db.query(Vehiculo).filter_by(placa=vehiculo.placa).first():
        raise HTTPException(status_code=400, detail="Vehículo ya registrado")
    db.add(vehiculo)
    db.commit()
    db.refresh(vehiculo)
    return vehiculo