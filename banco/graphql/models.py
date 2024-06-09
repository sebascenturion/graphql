# models.py
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

DATABASE_URL = "sqlite:///../banco_gql.db"

Base = declarative_base()

class Cliente(Base):
    __tablename__ = "clientes"
    id = Column(Integer, primary_key=True, index=True)
    cedula = Column(String, unique=True, index=True)
    nombre = Column(String, index=True)
    apellido = Column(String, index=True)
    cuentas = relationship("Cuenta", back_populates="cliente")

class Cuenta(Base):
    __tablename__ = "cuentas"
    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, ForeignKey('clientes.id'))
    cuenta = Column(Integer, index=True)
    pagos = relationship("Pagos", back_populates="cuenta")
    cliente = relationship("Cliente", back_populates="cuentas")

class Pagos(Base):
    __tablename__ = "pagos"
    id = Column(Integer, primary_key=True, index=True)
    cuenta_id = Column(Integer, ForeignKey('cuentas.id'))
    monto = Column(Integer)
    moneda = Column(String)
    numero_factura = Column(String)
    cuenta = relationship("Cuenta", back_populates="pagos")


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)
