from sqlalchemy.orm import Session
from models import Usuario
from typing import Dict, List
from datetime import datetime, timedelta
import math

# Simulación de grupos rotativos semanales según cantidad de usuarios
# Se recomienda tener un campo en Usuario llamado `grupo_rotacion` para mantener asignación

SEMANA_ACTUAL = datetime.today().isocalendar().week


def asignar_grupos(db: Session, usuarios_por_grupo: int = 5) -> Dict[int, List[int]]:
    usuarios = db.query(Usuario).order_by(Usuario.id).all()
    total = len(usuarios)
    grupos = math.ceil(total / usuarios_por_grupo)

    resultado = {}
    for i in range(grupos):
        resultado[i + 1] = []

    for idx, usuario in enumerate(usuarios):
        grupo_id = (idx % grupos) + 1
        resultado[grupo_id].append(usuario.id)
        # si se desea guardar la asignación en base de datos:
        # usuario.grupo_rotacion = grupo_id

    db.commit()
    return resultado


def grupo_que_rota_esta_semana(db: Session) -> List[int]:
    semana = datetime.today().isocalendar().week
    usuarios = db.query(Usuario).all()

    # Rotación simple: cada grupo usa el parqueadero una semana sí, una no
    # Por ejemplo: grupo 1 rota en semana impar, grupo 2 en semana par
    grupo_actual = (semana % 2) + 1
    ids = [u.id for u in usuarios if (u.id % 2) + 1 == grupo_actual]
    return ids


def puede_reservar_por_rotacion(usuario_id: int, db: Session) -> bool:
    grupo = (usuario_id % 2) + 1
    semana = datetime.today().isocalendar().week
    return (semana % 2) + 1 == grupo
