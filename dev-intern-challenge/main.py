from fastapi import FastAPI
from models.models import Item
from config import settings
from db import Database
from crud import create_entry


db = Database(settings.db_path)

app = FastAPI()




@app.post("/inventory/", status_code=200, response_model=Item)
def create_item(item: Item, db_path=db) -> Item:
    return create_entry(item, db_path)






# @app.get("/inventory/{item_id}", status_code=200, response_model=Item)
# def get_item(item_id: int):

