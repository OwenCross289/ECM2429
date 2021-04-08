import requests
from Models.Order import Order
from Models.Item import Item
import Database.DatabaseHandler as db

class ApiCommunicator:
    ''' Class for interfacing with the web API
    '''
    def __init__(self):
        '''Interface for the API 
        '''
        self.uri = 'http://localhost:8080'
    

    def get_new_orders(self):
        ''' Queries the API for new orders and add them to the database
        if it can connect to the API
        returns: bool: true if success, false if failure
        '''
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
           