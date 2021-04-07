import requests
from Models.Order import Order
from Models.Item import Item
import Database.DatabaseHandler as db

class ApiCommunicator:


    def __init__(self):
        '''Data represnation of a item
        :param item_id: int: ID of Item in database
        :param item_name: str: Name of item
        :param price: float: Price of item in GBP
        :param warehouse_location: int: Location of item in warehouse
        :param stock: int: Amount of item in warehouse
        '''
        self.uri = 'http://localhost:8080'
    

    def get_new_orders(self):
        try:
            r = requests.get(self.uri)
            if r:
                order_list = []
                for api_order in r.json():
                    item = db.get_item(api_order['item_id'])
                    order = Order(0, api_order['name'], api_order['address'], api_order['post_code'], api_order['email'], item, 'Ready')
                    order_list.append(order)
                db.put_orders(order_list)
                return True
            else:
                return False
        except:
            return False
           