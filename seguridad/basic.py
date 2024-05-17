from typing import Annotated
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()
security = HTTPBasic()

def get_current_user(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = "usuario"
    correct_password = "contraseña"
    if credentials.username != correct_username or credentials.password != correct_password:
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")
    return credentials.username

@app.get("/secure", tags=["seguridad"])
async def secure_endpoint(username: str = Depends(get_current_user)):
    return {"mensaje": f"Hola, {username}. Esta es una ruta segura."}

@app.get("/users/me")
def read_current_user(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    authenticate(credentials)
    return {'consulta exitosa': credentials.username}

@app.get("/users/me")
def get_time(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    authenticate(credentials)
    return  {'consulta exitosa': credentials.username}

def authenticate(credentials):
     #return {"username": credentials.username, "password": credentials.password}
    correct_username = "usuario"
    correct_password = "contrasenha"
    if credentials.username != correct_username or credentials.password != correct_password:
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")
