import sqlite3

class Database():
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.curr = self.conn.cursor()
        self.curr.execute("""CREATE TABLE IF NOT EXISTS items
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT,
                        description TEXT,
                        logcation INTEGER)"""
                        )
    def get_newest_entry(self, id_: int):
        data = self.curr.execute("SELECT * FROM items WHERE id == ?", (id))
        return data