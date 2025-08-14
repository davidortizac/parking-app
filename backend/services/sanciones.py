
from sqlalchemy.orm import Session
from models import Reserva, Usuario
from datetime import datetime, timedelta
from fastapi import HTTPException

# Esta tabla se debería crear en models.py si se desea persistir sanciones
# class Sancion(Base):
#     __tablename__ = "sanciones"
#     id = Column(Integer, primary_key=True, index=True)
#     usuario_id = Column(Integer, ForeignKey("usuarios.id"))
#     fecha = Column(Date)
#     motivo = Column(String)


def verificar_inasistencias(db: Session, fecha_actual: datetime.date):
    # Buscar reservas pasadas activas sin uso confirmado (simplificado: asumimos que no fueron usadas)
    fecha_limite = fecha_actual - timedelta(days=1)
    reservas_no_usadas = db.query(Reserva).filter(
        Reserva.fecha == fecha_limite,
        Reserva.activa == True
    ).all()

    sancionados = []

    for reserva in reservas_no_usadas:
        # Desactivar reserva y registrar sanción
        reserva.activa = False
        db.commit()

        # Aquí podrías guardar una sanción en una tabla
        sancionados.append(reserva.usuario_id)
        print(f"Usuario {reserva.usuario_id} sancionado por no usar reserva el {reserva.fecha}")

    return sancionados


def esta_sancionado(usuario_id: int, fecha: datetime.date) -> bool:
    # Ejemplo simple: prohíbe reservar el mismo día de la semana siguiente si fue sancionado
    dia_semana_actual = fecha.weekday()
    semana_anterior = fecha - timedelta(days=7)
    return dia_semana_actual == semana_anterior.weekday()

# Nota: Se recomienda añadir un campo adicional a Usuario (por ejemplo, `fecha_sancion`) si no se implementa una tabla de sanciones
