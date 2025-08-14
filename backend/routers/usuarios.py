from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models import Usuario
from database import get_db

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

@router.post("/")
def crear_usuario(usuario: Usuario, db: Session = Depends(get_db)):
    existe = db.query(Usuario).filter_by(correo=usuario.correo).first()
    if existe:
        raise HTTPException(status_code=400, detail="Usuario ya registrado")
    db.add(usuario)
    db.commit()
    db.refresh(usuario)
    return usuario

@router.get("/")
def listar_usuarios(db: Session = Depends(get_db)):
    return db.query(Usuario).all()
