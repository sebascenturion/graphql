from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    nombre: str
    precio: float
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}

#htttp://localhost:8000/items/1?nombre=""
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

#htttp://localhost:8000/items?tipo="comestible"
@app.get("/items/")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):

    sql = "update items set nombre= "+item.nombre+", precio="+str(item.precio)+" where id ="+str(item_id) 
    print(sql)
    
    return {"nombre_item": item.nombre, "item_id": item_id,"en_oferta":item.is_offer}

