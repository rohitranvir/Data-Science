from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
class Item(BaseModel):
    text:str=None
    is_done:bool=False
app=FastAPI()

@app.get("/")
def route():
    return {"h1":"hiii"}
items=[]
@app.post("/items")
def create_item(item:Item):
    items.append(item)
    return items

@app.get("/items/{item_id}")
def get_item(item_id:int):
    if item_id <=len(items):
        item=items[item_id]  
        return item
    else:
        raise HTTPException(status_code=404,    detail= "Data Not present at this postion")
    

@app.get("/get_items")
def list_items(limit: int=10):
    return items[0:limit]
