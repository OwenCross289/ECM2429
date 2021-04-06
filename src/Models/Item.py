class Item:

    def __init__(self, item_id: int, item_name: str, price: float, warehouse_location: int, stock: int):
        '''Data represnation of a item
        :param item_id: int: ID of Item in database
        :param item_name: str: Name of item
        :param price: float: Price of item in GBP
        :param warehouse_location: int: Location of item in warehouse
        :param stock: int: Amount of item in warehouse
        '''
        self.item_id = item_id
        self.item_name = item_name
        self.price = price
        self.warehouse_location = warehouse_location
        self.stock = stock