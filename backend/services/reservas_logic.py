from datetime import datetime, timedelta
from models import Vehiculo, Reserva, Cupo, Restriccion, TipoVehiculo, FranjaHorario
from sqlalchemy.orm import Session
from fastapi import HTTPException
import calendar

# Constantes de cupos máximos
MAX_AUTOS = 6
MAX_MOTOS = 8

# Restricciones pico y placa semanales
RESTRICCIONES = {
    "lunes": [6, 9],
    "martes": [5, 7],
    "miércoles": [1, 8],
    "jueves": [0, 2],
    "viernes": [3, 4]
}

def validar_reserva(reserva: Reserva, db: Session):
    fecha = reserva.fecha
    dia_semana = calendar.day_name[fecha.weekday()].lower()

    # 1. Validar restricción por placa
    vehiculo = db.query(Vehiculo).filter_by(id=reserva.vehiculo_id).first()
    if not vehiculo:
        raise HTTPException(404, detail="Vehículo no encontrado")

    digito = int(vehiculo.placa[-1]) if vehiculo.tipo == TipoVehiculo.AUTOMOVIL else int(vehiculo.placa[0])
    if digito in RESTRICCIONES.get(dia_semana, []):
        raise HTTPException(403, detail="Restricción por pico y placa para este día")

    # 2. Validar que no tenga reserva previa ese día (excluyente auto/moto)
    reserva_existente = db.query(Reserva).filter_by(
        usuario_id=reserva.usuario_id,
        fecha=fecha
    ).first()
    if reserva_existente:
        raise HTTPException(400, detail="Ya tienes una reserva activa para ese día")

    # 3. Validar disponibilidad de cupo en esa franja y tipo
    cupo = db.query(Cupo).filter_by(
        fecha=fecha,
        franja=reserva.franja,
        tipo=vehiculo.tipo
    ).first()

    if not cupo:
        # Crear cupo si no existe
        cupo = Cupo(
            fecha=fecha,
            franja=reserva.franja,
            tipo=vehiculo.tipo,
            disponibles=MAX_AUTOS if vehiculo.tipo == TipoVehiculo.AUTOMOVIL else MAX_MOTOS,
            ocupados=0
        )
        db.add(cupo)
        db.commit()
        db.refresh(cupo)

    if cupo.ocupados >= cupo.disponibles:
        raise HTTPException(400, detail="No hay cupos disponibles para esta franja y tipo")

    # 4. Reservar espacio
    cupo.ocupados += 1
    db.add(cupo)
    db.commit()

    return True
