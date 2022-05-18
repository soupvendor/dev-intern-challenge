import sqlite3
from config import settings
from models.models import Item
from db import Database



# This gets passed the Item model to create an entry into the database
def create_entry(item: Item, db: Database):
    db.curr.execute("""INSERT INTO items
                    (name, description, location)
                    VALUES (?, ?, ?)""", 
                    (item.name, item.description, item.location),
                    )
    db.conn.commit()
    # new_data = db.get_newest_entry(db.curr.lastrowid)

    # return new_data
