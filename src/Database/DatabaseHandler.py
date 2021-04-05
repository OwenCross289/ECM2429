import sqlite3
from sqlite3 import Error
from pathlib import Path
from Models.Order import Order
from Models.Item import Item


db_file = f"{str(Path(__file__).parent)}/ECM2429.db"

def get_orders():
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as error:
            print(error)
    finally:
        if conn:
            conn.close()

def get_item(item_id: int):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as error:
            print(error)
    finally:
        if conn:
            sql = f'SELECT * FROM Items WHERE ItemId == {item_id}'
            cur = conn.cursor()
            cur.execute(sql)
            result = cur.fetchone()
            item = Item(item_id, result[1], result[2], result[3], result[4])
            conn.close()
    return item

def get_order(order_id: int):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as error:
            print(error)
    finally:
        if conn:
            sql = f'SELECT * FROM Orders WHERE OrderID == {order_id}'
            cur = conn.cursor()
            cur.execute(sql)
            result = cur.fetchone()
            name = result[1]
            address = result[2]
            post_code = result[3]
            email = result[4]
            item_id = result[5]
            status = result[6]
            #order = Order(result[0],result[1], result[2],result[3],result[4], Item(), result[6] )
            conn.close()
            item = get_item(item_id)
    return Order(order_id, name, address, post_code, email, item, status)

def put_orders():
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as error:
            print(error)
    finally:
        if conn:
            conn.close()

def get_ready_orders():
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as error:
            print(error)
    finally:
        if conn:
            conn.close()

def get_shipping_orders():
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as error:
            print(error)
    finally:
        if conn:
            conn.close()

def update_order_status(id: int, status: str):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as error:
            print(error)
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    get_order(1)
