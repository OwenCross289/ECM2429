from Models.Item import Item
from reportlab.pdfgen import canvas
import os

class Order:

    def __init__(self, order_id: int, customer_name: str, customer_address: str, post_code: str, email: str, item: Item, order_status):
        self.order_id = order_id
        self.customer_name = customer_name
        self.customer_address = customer_address
        self.post_code = post_code
        self.email = email
        self.item = item
        self.order_status = order_status

    def print_pdf(self, path):
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

