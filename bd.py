from typing import Union
from models.cuenta import Cuenta


class Repositorio:

    cuentaTabla : dict[int, Cuenta] = {}

    @classmethod
    def registrarCuenta(cls, cuenta:Cuenta):
        cls.cuentaTabla[cuenta.cuenta] = cuenta

    @classmethod
    def getCuenta(cls, id:int):
        return cls.cuentaTabla[id]

