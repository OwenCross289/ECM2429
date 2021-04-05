from Models.Item import Item

class Order:

    def __init__(self, order_id: int, customer_name: str, customer_address: str, post_code: str, email: str, item: Item, order_status):
        self.order_id = order_id
        self.customer_name = customer_name
        self.customer_address = customer_address
        self.post_code = post_code
        self.email = email
        self.item = item
        self.order_status = order_status
