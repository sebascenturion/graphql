# Crear entorno virtual e instalar FastAPI
pip install virtualenv
virtualenv -p python3 venv 
# si lo anterior no funciona
python3 -m venv venv

# Activar entorno virtual
./venv/Scripts/activate
pip install fastapi

# Levantar una aplicacion FastAPI
fastapi dev <app>.py

## Agregar al launch.json para poder hacer debug
{
            "name": "FastAPI Basic auth",
            "type": "python",
            "request": "launch",
            "module": "uvicorn",
            "cwd": "${workspaceFolder}/seguridad",
            "args": [
              "basic:app",
              "--reload",
              "--port", //these arg are optional
              "3003"
            ]
        }

# Ejecución por consola del bancoBaseAPI
1. Posicionarse dentro de la carpeta banco
2. fastapi dev .\BancoBaseAPI.py  