from sqlalchemy import Column, Integer, String, Date, ForeignKey, Enum, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import enum

Base = declarative_base()

class TipoVehiculo(str, enum.Enum):
    AUTOMOVIL = "automovil"
    MOTOCICLETA = "motocicleta"

class FranjaHorario(str, enum.Enum):
    MANANA = "manana"  # 8am - 12m
    TARDE = "tarde"    # 12m - 6pm
    DIA_COMPLETO = "dia_completo"  # 8am - 6pm

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    apellido = Column(String)
    cargo = Column(String)
    correo = Column(String, unique=True, index=True)
    celular = Column(String)
    perfil = Column(String)

    vehiculos = relationship("Vehiculo", back_populates="usuario")
    reservas = relationship("Reserva", back_populates="usuario")

class Vehiculo(Base):
    __tablename__ = "vehiculos"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    tipo = Column(Enum(TipoVehiculo))
    placa = Column(String, unique=True)

    usuario = relationship("Usuario", back_populates="vehiculos")
    reservas = relationship("Reserva", back_populates="vehiculo")

class Reserva(Base):
    __tablename__ = "reservas"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    vehiculo_id = Column(Integer, ForeignKey("vehiculos.id"))
    fecha = Column(Date)
    franja = Column(Enum(FranjaHorario))
    tipo = Column(Enum(TipoVehiculo))
    activa = Column(Boolean, default=True)

    usuario = relationship("Usuario", back_populates="reservas")
    vehiculo = relationship("Vehiculo", back_populates="reservas")

class Restriccion(Base):
    __tablename__ = "restricciones"

    id = Column(Integer, primary_key=True, index=True)
    tipo = Column(Enum(TipoVehiculo))
    digito = Column(Integer)
    dia_semana = Column(String)  # lunes, martes, etc.
    fecha_inicio = Column(Date)
    fecha_fin = Column(Date)

class Cupo(Base):
    __tablename__ = "cupos"

    id = Column(Integer, primary_key=True, index=True)
    fecha = Column(Date)
    franja = Column(Enum(FranjaHorario))
    tipo = Column(Enum(TipoVehiculo))
    disponibles = Column(Integer)
    ocupados = Column(Integer)

class Sancion(Base):
    __tablename__ = "sanciones"
    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    fecha = Column(Date)
    motivo = Column(String)
