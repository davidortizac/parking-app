from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models import Reserva
from database import get_db
from services.reserva_logic import validar_reserva
from services.sanciones import esta_sancionado
from services.rotacion import puede_reservar_por_rotacion
from datetime import datetime

router = APIRouter(prefix="/reservas", tags=["Reservas"])

@router.post("/")
def crear_reserva(reserva: Reserva, db: Session = Depends(get_db)):
    hoy = datetime.today().date()
    if reserva.fecha < hoy:
        raise HTTPException(status_code=400, detail="No se puede reservar para fechas pasadas")

    # Verificar sanción activa
    if esta_sancionado(reserva.usuario_id, reserva.fecha):
        raise HTTPException(status_code=403, detail="Tienes una sanción activa y no puedes reservar este día")

    # Verificar si el usuario está en grupo activo esta semana
    if not puede_reservar_por_rotacion(reserva.usuario_id, db):
        raise HTTPException(status_code=403, detail="Tu grupo no tiene asignación de parqueo esta semana")

    # Validaciones de política de parqueadero
    validar_reserva(reserva, db)

    db.add(reserva)
    db.commit()
    db.refresh(reserva)
    return reserva

