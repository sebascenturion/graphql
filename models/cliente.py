from typing import Union
from pydantic import BaseModel


class Cliente(BaseModel):
    id: Union[int, None] = None
    cedula: str
    nro_cuenta: int