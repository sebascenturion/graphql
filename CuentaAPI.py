from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
from models.cuenta import Cuenta
from bd import Repositorio
app = FastAPI()


@app.post("/cuentas/{cuenta_id}")
def update_item(cuenta_id: int, cuenta: Cuenta):
    Repositorio.registrarCuenta(cuenta)
    
    
    #return {"cuenta": cuenta.cuenta, "mensaje": "ok"}
    return cuenta


@app.get("/cuentas/{cuenta_id}")
def update_item(cuenta_id: int, q: Union[str, None] = None):
    return Repositorio.getCuenta(cuenta_id)
    
    
    #return {"cuenta": cuenta.cuenta, "mensaje": "ok"}
    #return cuenta
