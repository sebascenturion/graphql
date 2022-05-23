from pydantic import BaseModel

class Cuenta(BaseModel):
    cedula: str
    cuenta: int
