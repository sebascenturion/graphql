import strawberry
from typing import List, Optional
from strawberry.types import Info
from models import Cliente as ClienteModel, Cuenta as CuentaModel, Pagos as PagosModel, SessionLocal
from sqlalchemy.orm import joinedload
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import IntegrityError

@strawberry.type
class Cuenta:
    id: int
    cliente_id: int
    cuenta: int
    pagos: List["Pago"]

@strawberry.type
class Pago:
    id: int
    cuenta_id: int
    monto: int
    moneda: str
    numero_factura: str
    cuenta: Cuenta

@strawberry.type
class Cliente:
    id: int
    cedula: str
    nombre: str
    apellido: str
    cuentas: List[Cuenta]

@strawberry.type
class Query:

    @strawberry.field
    def all_clientes(self, info: Info, nombre: Optional[str] = None) -> List[Cliente]:
        session = SessionLocal()
        query = session.query(ClienteModel).options(
            joinedload(ClienteModel.cuentas).joinedload(CuentaModel.pagos)
        )
        if nombre:
            query = query.filter(ClienteModel.nombre == nombre)
        clientes = query.all()
        return clientes
    
    @strawberry.field
    def pagos_por_cuenta(self, info: Info, cuenta: int) -> List[Pago]:
        session = SessionLocal()
        pagos = session.query(PagosModel).options(
            joinedload(PagosModel.cuenta)
        ).filter(PagosModel.cuenta_id == cuenta).all()
        return pagos

    @strawberry.field
    def all_cuentas(self, info: Info) -> List[Cuenta]:
        session = SessionLocal()
        cuentas = session.query(CuentaModel).all()
        return cuentas

    @strawberry.field
    def all_pagos(self, info: Info) -> List[Pago]:
        session = SessionLocal()
        pagos = session.query(PagosModel).all()
        return pagos

@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_cliente(self, info: Info, cedula: str, nombre: str, apellido: str) -> Cliente:
        if not cedula or not cedula.strip():
            raise ValueError("La cédula es requerida y no puede estar vacía.")
        if not nombre or not nombre.strip():
            raise ValueError("El nombre es requerido y no puede estar vacío.")
        if not apellido or not apellido.strip():
            raise ValueError("El apellido es requerido y no puede estar vacío.")

        session = SessionLocal()
        cliente = ClienteModel(cedula=cedula, nombre=nombre, apellido=apellido)
        session.add(cliente)
        session.commit()
        session.refresh(cliente)
        return cliente

    @strawberry.mutation
    def create_cuenta(self, info: Info, cliente_id: int, cuenta: int) -> Cuenta:
        if not cuenta:
            raise ValueError("El número de cuenta es requerido.")
        session = SessionLocal()
        cuenta_model = CuentaModel(cliente_id=cliente_id, cuenta=cuenta)
        try:
            session.add(cuenta_model)
            session.commit()
            session.refresh(cuenta_model)
        except IntegrityError:
            session.rollback()
            raise ValueError("El número de cuenta debe ser único.")
        return cuenta_model

    @strawberry.mutation
    def create_pago(self, info: Info, cuenta_id: int, monto: int, moneda: str, numero_factura: str) -> Pago:
        if not numero_factura or not numero_factura.strip():
            raise ValueError("El número de factura es requerido y no puede estar vacío.")
        if not moneda or not moneda.strip():
            raise ValueError("La moneda es requerida y no puede estar vacía.")
        if monto <= 0:
            raise ValueError("El monto debe ser mayor que cero.")

        session = SessionLocal()
        try:
            # Validar existencia de cuenta y cliente
            cuenta = session.query(CuentaModel).filter(CuentaModel.id == cuenta_id).one()
            cliente = session.query(ClienteModel).filter(ClienteModel.id == cuenta.cliente_id).one()
            
            # Crear pago
            pago = PagosModel(cuenta_id=cuenta_id, monto=monto, moneda=moneda, numero_factura=numero_factura)
            session.add(pago)
            session.commit()
            session.refresh(pago)
            session.refresh(pago.cuenta)
        except NoResultFound:
            session.rollback()
            raise ValueError("La cuenta o cliente no existen o no coinciden.")
        except IntegrityError:
            session.rollback()
            raise ValueError("No se puede pagar más de una vez una misma factura. Todos los datos son requeridos.")
        return pago
    
schema = strawberry.Schema(query=Query, mutation=Mutation)
