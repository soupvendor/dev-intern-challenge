from typing import Iterator
from fastapi import FastAPI, Depends, Response, HTTPException
from models.models import Item, ItemResponse, Location
from config import settings
from db import Database
from crud import (
    create_entry,
    read_entry,
    update_entry,
    delete_entry,
    create_location_entry,
    list_locations,
    list_items,
)


def get_db() -> Iterator[Database]:
    yield Database(settings.db_path)


app = FastAPI()


@app.post("/items/", status_code=200, response_model=ItemResponse)
def create_item(item: Item, db: Database = Depends(get_db)) -> ItemResponse:
    data = create_entry(item, db)
    if not data:
        raise HTTPException(
            status_code=404, detail="Unabe to create item, make sure location is valid"
        )
    else:
        return data


@app.get("/items/{item_id}", status_code=200, response_model=ItemResponse)
def read_item(item_id: int, db: Database = Depends(get_db)) -> ItemResponse:
    item = read_entry(item_id, db)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    else:
        return item


@app.put("/items/{item_id}", status_code=200, response_model=ItemResponse)
def update_item(
    item_id: int, item: Item, db: Database = Depends(get_db)
) -> ItemResponse:
    data = update_entry(item_id, item, db)
    if not data:
        raise HTTPException(status_code=404, detail="Item not found")
    else:
        return data


@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int, db: Database = Depends(get_db)) -> Response:
    data = read_entry(item_id, db)
    if not data:
        return Response(status_code=404)
    else:
        delete_entry(item_id, db)
        return Response(status_code=204)


@app.get("/items/", status_code=200, response_model=list[ItemResponse])
def list_all_items(db: Database = Depends(get_db)) -> list[ItemResponse]:
    return list_items(db)


@app.post("/locations/{location_id}", status_code=200, response_model=Location)
def create_location(location: Location, db: Database = Depends(get_db)) -> Location:
    return create_location_entry(location, db)


@app.post("/locations/", status_code=200, response_model=list[Location])
def list_all_locations(db: Database = Depends(get_db)) -> list[Location]:
    return list_locations(db)
