from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
from models.cliente import Cliente
from models.cuenta import Cuenta
from bd import Repositorio
app = FastAPI()


#Recursos
# 1 - Cliente
# 2 - Pago 


@app.post("/clientes")
def registar_cliente(cliente: Cliente):
    Repositorio.insertarCliente(cliente)
    return cliente

@app.get("/clientes")
def recuperar_clientes():
    registros: dict[int, Cliente]= Repositorio.recuperar_clientes()
    return list(registros)