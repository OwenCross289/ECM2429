from Models.Item import Item
from reportlab.pdfgen import canvas
import os

class Order:

    def __init__(self, order_id: int, customer_name: str, customer_address: str, post_code: str, email: str, item: Item, order_status: str):
        '''Data represnation of a customer order
        :param order_id: int: ID of Order in database
        :param customer_name: str: Name of customer who placed order
        :param customer_address: str: Address of customer who placed order
        :param post_code: int: Post code of customer who placed order
        :param email: str: email of customer who placed order
        :param item: Item: Item the customer has ordered
        :param order_status: str: Status of order, should only be 'Ready' or 'Shipping'
        '''
        self.order_id = order_id
        self.customer_name = customer_name
        self.customer_address = customer_address
        self.post_code = post_code
        self.email = email
        self.item = item
        self.order_status = order_status

    def print_pdf(self, path: str):
        '''Prints a shipping label, currently writes to disk
        as prototype
        :param path: str: Folder location to write pdf
        '''
        #As this is just a prototype this just creates a PDF in specified location.
        document_title = "ECM2429 Store"
        file_name = os.path.join(path, f"{self.customer_name}{self.order_id}.pdf")
        
        #create pdf doc in memory
        pdf = canvas.Canvas(file_name)
        pdf.setTitle(document_title)

        pdf.setFontSize(36)
        pdf.drawCentredString(300, 720, document_title)

        pdf.setFontSize(18)
        pdf.drawCentredString(300, 680, f"{self.customer_name}")
        pdf.drawCentredString(300, 660, f"{self.customer_address}")
        pdf.drawCentredString(300, 640, f"{self.post_code}")

        pdf.save()

