class Item:

    def __init__(self, item_id: int, item_name: str, price: float, warehouse_location: int, stock: int):
        self.item_id = item_id
        self.item_name = item_name
        self.price = price
        self.warehouse_location = warehouse_location
        self.stock = stock