import sqlite3
from sqlite3 import Error
from pathlib import Path
from Models.Order import Order
from Models.Item import Item


db_file = f"{str(Path(__file__).parent)}/ECM2429.db"

def get_orders():
    """ Gets all orders """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as error:
        print(error)
    finally:
        if conn:
            sql = 'SELECT * FROM Orders'
            cur = conn.cursor()
            cur.execute(sql)
            results = cur.fetchall()
            conn.close()
            orders = []
            for result in results:
                order_id = result[0]
                name = result[1]
                address = result[2]
                post_code = result[3]
                email = result[4]
                item_id = result[5]
                status = result[6]
                item = get_item(item_id)
                order = Order(order_id, name, address, post_code, email, item, status)
                orders.append(order)
    return orders

def get_item(item_id: int):
    """ Get item from item ID """
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
    """ Get order from OrderID """
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
            conn.close()
            item = get_item(item_id)
    return Order(order_id, name, address, post_code, email, item, status)

def put_orders(orders: []):
    """ Put orders into the database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as error:
        print(error)
    finally:
        if conn:
            for order in orders:
                sql = f"""INSERT INTO Orders
                          (OrderID, Name, Address, PostCode, Email, ItemId, OrderStatus) 
                          VALUES 
                          (NULL,'{order.customer_name}','{order.customer_address}','{order.post_code}','{order.email}', {order.item.item_id}, '{order.order_status}')"""
                cur = conn.cursor()
                cur.execute(sql)
            conn.commit()
            conn.close()

def get_ready_orders():
    """ Get all orders with a status of ready """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as error:
        print(error)
    finally:
        if conn:
            sql = "SELECT * FROM Orders WHERE OrderStatus == 'Ready'"
            cur = conn.cursor()
            cur.execute(sql)
            results = cur.fetchall()
            conn.close()
            orders = []
            for result in results:
                order_id = result[0]
                name = result[1]
                address = result[2]
                post_code = result[3]
                email = result[4]
                item_id = result[5]
                status = result[6]
                item = get_item(item_id)
                order = Order(order_id, name, address, post_code, email, item, status)
                orders.append(order)
    return orders

def get_shipping_orders():
    """ Get all orders with a status of shipping """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as error:
        print(error)
    finally:
        if conn:
            sql = "SELECT * FROM Orders WHERE OrderStatus == 'Shipping'"
            cur = conn.cursor()
            cur.execute(sql)
            results = cur.fetchall()
            conn.close()
            orders = []
            for result in results:
                order_id = result[0]
                name = result[1]
                address = result[2]
                post_code = result[3]
                email = result[4]
                item_id = result[5]
                status = result[6]
                item = get_item(item_id)
                order = Order(order_id, name, address, post_code, email, item, status)
                orders.append(order)
    return orders

def update_order_status(order_id: int, status: str):
    """ Update an order to have a set status """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as error:
        print(error)
    finally:
        if conn:
            sql = f"UPDATE Orders SET OrderStatus = '{status}' WHERE OrderID == {order_id}"
            cur = conn.cursor()
            cur.execute(sql)
            conn.commit()
            conn.close()


if __name__ == '__main__':
    print('HELLO')