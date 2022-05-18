from typing import Iterator
from fastapi import FastAPI, Depends, Response, HTTPException
from models.models import Item, ItemResponse, ItemResponseTemplate, Location
from config import settings
from db import Database
from crud import create_entry, read_entry, update_entry, delete_entry, create_location_entry


def get_db() -> Iterator[Database]:
    yield Database(settings.db_path)




app = FastAPI()




@app.post("/inventory/", status_code=200, response_model=ItemResponseTemplate)
def create_item(item: Item, db: Database = Depends(get_db)) -> ItemResponse:
    return create_entry(item, db)


@app.get("/inventory/{item_id}", status_code=200, response_model=ItemResponseTemplate)
def read_item(item_id: int, db: Database = Depends(get_db)) -> ItemResponse:
    return read_entry(item_id, db)

@app.put("/inventory/{item_id}", status_code=200, response_model=ItemResponseTemplate)
def update_item(item_id: int, item: Item, db: Database = Depends(get_db)) -> ItemResponse:
    return update_entry(item_id, item, db)

@app.delete("/inventory/{item_id}", status_code=204)
def delete_item(item_id: int, db: Database = Depends(get_db)) -> Response:
    data = read_entry(item_id, db)
    if not data:
        return Response(status_code=404)
    else:
        delete_entry(item_id, db)
        return Response(status_code=204)

@app.post("/location/{location_id}", status_code=200, response_model=Location)
def create_location(location: Location, db: Database = Depends(get_db)) -> Location:
    return create_location_entry(location, db)