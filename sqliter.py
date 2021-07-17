import sqlite3


class SQLighter:

    def __init__(self, database_file):
        self.connection = sqlite3.connect(database_file)
        self.cursor = self.connection.cursor()

    def close(self):
        self.connection.close()