import sqlite3
from sqlite3 import Error

class DatabaseHandler:


    def __init__(self, db_file):
        self.db_file = db_file

    def create_connection(self):
        """ create a database connection to a SQLite database """
        conn = None
        try:
            conn = sqlite3.connect(self.db_file)
            print(sqlite3.version)
            print(self.db_file)
        except Error as error:
            print(error)
        finally:
            if conn:
                conn.close()

    def create_table(self):
        """ create a database connection to a SQLite database """
        conn = None
        try:
            conn = sqlite3.connect(self.db_file)
            print(sqlite3.version)
        except Error as error:
            print(error)
        finally:
            if conn:
                conn.close()


if __name__ == '__main__':
    x = DatabaseHandler("../ECM2429.db")
    x.create_connection()
