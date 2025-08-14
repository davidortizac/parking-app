from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from models import Cupo, Reserva, Usuario, Vehiculo
from database import get_db
from typing import List
from datetime import datetime

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])

@router.get("/")
def obtener_disponibilidad(fecha: str = Query(...), db: Session = Depends(get_db)) -> List[dict]:
    try:
        fecha_obj = datetime.strptime(fecha, "%Y-%m-%d").date()
    except ValueError:
        return []

    cupos = db.query(Cupo).filter(Cupo.fecha == fecha_obj).all()
    respuesta = []

    for cupo in cupos:
        reservas = db.query(Reserva).filter_by(
            fecha=fecha_obj,
            franja=cupo.franja,
            tipo=cupo.tipo
        ).all()

        usuarios = []
        for r in reservas:
            usuario = db.query(Usuario).filter_by(id=r.usuario_id).first()
            if usuario:
                usuarios.append(f"{usuario.nombre} {usuario.apellido}")

        respuesta.append({
            "tipo": cupo.tipo.value,
            "franja": cupo.franja.value,
            "disponibles": cupo.disponibles,
            "ocupados": cupo.ocupados,
            "usuarios": usuarios
        })

    return respuesta
