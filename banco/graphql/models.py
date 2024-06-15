from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.orm.exc import NoResultFound

DATABASE_URL = "sqlite:///../banco_gql.db"

Base = declarative_base()

class Cliente(Base):
    __tablename__ = "clientes"
    id = Column(Integer, primary_key=True, index=True)
    cedula = Column(String, index=True, nullable=False)
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    cuentas = relationship("Cuenta", back_populates="cliente")

class Cuenta(Base):
    __tablename__ = "cuentas"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    cliente_id = Column(Integer, ForeignKey('clientes.id'), nullable=False)
    cuenta = Column(Integer, unique=True, nullable=False)
    pagos = relationship("Pagos", back_populates="cuenta")
    cliente = relationship("Cliente", back_populates="cuentas")

class Pagos(Base):
    __tablename__ = "pagos"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    cuenta_id = Column(Integer, ForeignKey('cuentas.id'), nullable=False)
    monto = Column(Integer, nullable=False)
    moneda = Column(String, nullable=False)
    numero_factura = Column(String, nullable=False, unique=True)
    cuenta = relationship("Cuenta", back_populates="pagos")

    __table_args__ = (UniqueConstraint('numero_factura', name='_numero_factura_uc'),)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)
