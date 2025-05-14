import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("../db.sqlite3")
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS register (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            telegram_id VARCHAR(20),
            space_id VARCHAR(15)
            )
        """)
        self.conn.commit()

    def registration(self, telegram_id, space_id):
        self.cursor.execute("INSERT INTO register (telegram_id, space_id) VALUES (?, ?);", (telegram_id, space_id))
        self.conn.commit()

    def check_authentication(self, telegram_id):
        data = self.cursor.execute("SELECT * FROM register WHERE telegram_id = ?;", (telegram_id,)).fetchone()
        return data

    def get_coins(self, space_id):
        coins = self.cursor.execute("SELECT coins FROM users_student WHERE username = ?", (space_id,)).fetchone()
        return coins[0]

