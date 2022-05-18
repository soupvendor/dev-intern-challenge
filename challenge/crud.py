import sqlite3
from config import settings
from models.models import Item, ItemResponse, Location
from db import Database



def create_entry(item: Item, db: Database) -> ItemResponse:
    db.curr.execute(
        """INSERT INTO items
                    (name, description, location)
                    VALUES (?, ?, ?)""",
        (item.name, item.description, item.location),
    )
    db.conn.commit()
    new_id = db.curr.lastrowid
    data = ItemResponse(
        id=new_id, name=item.name, description=item.description, location=item.location
    )
    return data


def read_entry(id_: int, db: Database) -> ItemResponse:
    entry = db.select_row_by_id(id_)
    data = ItemResponse(
        id=entry[0], name=entry[1], description=entry[2], location=entry[3]
    )
    return data


def update_entry(id_: int, item: Item, db: Database) -> ItemResponse:
    params = [item.name, item.description, item.location, id_]
    db.curr.execute(
        "UPDATE items SET name = ?, description = ?, location = ? WHERE id == ?",
        (params),
    )
    db.conn.commit()
    data = db.select_row_by_id(id_)
    if data:
        payload = ItemResponse(
            id=data[0], name=data[1], description=data[2], location=data[3]
        )
        return payload


def delete_entry(id_: int, db: Database) -> None:
    data = db.select_row_by_id(id_)
    if data:
        db.curr.execute(
            """DELETE FROM items
            WHERE id == ?""",
            (id_,),
        )
        db.conn.commit()


# Bonus feature


def create_location_entry(location: Location, db: Database) -> Location:
    db.curr.execute(
        """INSERT INTO locations
                    (id, name, process, address)
                    VALUES (?, ?, ?, ?)""",
        (location.id, location.name, location.process, location.address),
    )
    db.conn.commit()
    data = Location(
        id=location.id,
        name=location.name,
        process=location.process,
        address=location.address,
    )
    return data
