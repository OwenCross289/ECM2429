import sqlite3
from sqlite3 import Error
from pathlib import Path
from Models.Order import Order
from Models.Item import Item
from Models.Email import Email


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
    """ Get item from item ID 
    :param item_id: int: ID of item in database
    """
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
    """ Get order from OrderID 
    :param item_id: int: ID of order in database
    """
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
    """ Put orders into the database 
    :param orders: Order[]: List of orders to be added to the database
    """
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
    """ Update an order to have a set status 
    :param order_id: int: ID of order in database
    :param status: str: new status
    """
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

def decrement_item_stock(item_id: int):
    """ Reduces stock of item by one if greater than 0 
    :param item_id: int: ID of item in database
    """
    item = get_item(item_id)
    if item.stock > 0:
        conn = None
        try:
            conn = sqlite3.connect(db_file)
        except Error as error:
            print(error)
        finally:
            if conn:
                sql = f"UPDATE Items SET Stock = {item.stock - 1} WHERE ItemId == {item.item_id}"
                cur = conn.cursor()
                cur.execute(sql)
                conn.commit()
                conn.close()

def get_generic_email_message():
    """ Gets the generic email message
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as error:
        print(error)
    finally:
        if conn:
            sql = f"SELECT * FROM GenericEmailMessage"
            cur = conn.cursor()
            cur.execute(sql)
            result = cur.fetchone()
            conn.close()
            return Email(result[1], result[2], result[3])

def update_generic_email_message(email):
    """ Sets the generic email message
    :param email: Email: Email to use
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as error:
        print(error)
    finally:
        if conn:
            sql = f"UPDATE GenericEmailMessage SET Addresser = '{email.addresser}', Body = '{email.body}', SignOff = '{email.sign_off}' WHERE Id == {1}"
            cur = conn.cursor()
            cur.execute(sql)
            conn.commit()
            conn.close()