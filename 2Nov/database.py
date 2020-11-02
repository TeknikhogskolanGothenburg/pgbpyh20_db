import sqlite3


class DB:
    def __init__(self, db_file_name):
        self.db_file_name = db_file_name
        self.connection = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_file_name)
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()