from typing import Union
from pydantic import BaseModel
import sqlite3



def init_db(nombre_db: str):
    conn = sqlite3.connect(nombre_db)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cedula TEXT UNIQUE,
            nombre TEXT,
            apellido TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cuentas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente_id INTEGER,
            cuenta INTEGER,
            FOREIGN KEY(cliente_id) REFERENCES clientes(id) ON DELETE CASCADE
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pagos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente_id INTEGER,
            cuenta_id INTEGER,
            numero_factura TEXT,
            monto INTEGER,
            moneda TEXT,
            FOREIGN KEY(cliente_id) REFERENCES clientes(id) ON DELETE CASCADE,
            FOREIGN KEY(cuenta_id) REFERENCES cuentas(id) ON DELETE CASCADE
        )
    ''')
    conn.commit()
    conn.close()



class Cliente(BaseModel):
    id: Union[int, None] = None
    cedula: str
    nombre: str = None
    apellido: str= None