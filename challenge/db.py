import sqlite3
from models.models import ItemResponse

class Database():
    def __init__(self, db_path: str) -> None:
        self.conn = sqlite3.connect(db_path)
        self.curr = self.conn.cursor()
        self.curr.execute("""CREATE TABLE IF NOT EXISTS items
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT,
                        description TEXT,
                        location INTEGER,
                        FOREIGN KEY (location) REFERENCES locations (id))"""
                        )
        self.curr.execute("""CREATE TABLE IF NOT EXISTS locations
                        (id INTEGER PRIMARY KEY,
                        name TEXT,
                        process TEXT,
                        address TEXT)"""
                        )
    def select_row_by_id(self, id_):
        data = self.curr.execute("SELECT * FROM items WHERE id == ?", (id_,)).fetchone()
        return data
