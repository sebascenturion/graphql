from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
from models.cliente import Cliente
from models.cuenta import Cuenta
from bd import Repositorio
import json
from fastapi.encoders import jsonable_encoder

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
    listObjetos =  list(registros) #lista DE objetos CLIENTES 
    listaJson = jsonable_encoder(listObjetos) #convertimos lista de objetos a json

    return listaJson


@app.get("/clientes/{id}")
def recuperar_cliente(id:int):
    cliente: Cliente= Repositorio.recuperar_cliente(id)
    return cliente
