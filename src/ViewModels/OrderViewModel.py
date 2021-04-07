import os
from kivy.properties import NumericProperty, ObjectProperty, StringProperty
from kivymd.uix.screen import MDScreen
from kivymd.toast import toast
from kivymd.uix.filemanager import MDFileManager
from functools import partial
from Models.Order import Order
from Models.Item import Item
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
import Database.DatabaseHandler as db

class OrderScreen(MDScreen):
    '''ViewModel for OrderView
    '''
    order_id = NumericProperty(1)
    order = ObjectProperty()
    custom_email_message = StringProperty()

    def on_pre_enter(self):
        '''Called when the view is opened
        '''
        self.dialog = None
        self.order = db.get_order(self.order_id)
        self.set_order_labels()
        self.set_item_labels()
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
            preview=True,
        )


    def set_order_labels(self):
        '''Sets the lables of the order based on the order property
        '''
        self.ids.order_id_lbl.text = f"Order Number: {self.order.order_id}"
        self.ids.order_name_lbl.text = f"Customer Name: {self.order.customer_name}"
        self.ids.order_address_lbl.text = f"Customer Street: {self.order.customer_address}"
        self.ids.order_post_code_lbl.text = f"Customer Postcode: {self.order.post_code}"
        self.ids.order_email_lbl.text = f"Customer Email: {self.order.email}"
        self.ids.order_status_lbl.text = f"Order status: {self.order.order_status}"
  

    def set_item_labels(self):
        '''Sets the lables of the item based on the order property
        '''
        self.ids.item_id_lbl.text = f"Item ID: {self.order.item.item_id}"
        self.ids.item_name_lbl.text = f"Item: {self.order.item.item_name}"
        self.ids.item_price_lbl.text = f"Price: {self.order.item.price}"
        self.ids.item_location_lbl.text = f"Warehouse Location: {self.order.item.warehouse_location}"
        if self.order.item.stock == 0:
            self.ids.item_stock_lbl.text = "Stock: Out of Stock"
            self.ids.item_stock_lbl.theme_text_color = "Error"
        else:
            self.ids.item_stock_lbl.text = f"Stock: {self.order.item.stock}"
            self.ids.item_stock_lbl.theme_text_color = "Primary"
   

    def close_screen(self):
        '''Will close the OrderView and navigate back to
        the PickingListView
        '''
        self.custom_email_message = ""
        self.ids.custom_email_input.text = ""
        self.parent.parent.parent.on_pre_enter()
        self.parent.transition.direction = "down"
        self.parent.current = "ListScreen"
        
    def add_to_shipping(self):
        '''Changes items status to 'Shipping' if the item is in stock and
        the current status is 'Ready'
        '''
        #When the order can be shipped
        if self.order.item.stock > 0 and self.order.order_status == 'Ready':
            db.decrement_item_stock(self.order.item.item_id)
            db.update_order_status(self.order.order_id, "Shipping")
            self.order = db.get_order(self.order.order_id)
            self.set_item_labels()
            self.set_order_labels()
            email = db.get_generic_email_message()
            #When using the generic email notification message
            if self.custom_email_message == '':
                email.update_full_email(self.order.customer_name, self.order.order_status)
                #If the email system was impliemtned email.send() would be called here
                self.show_alert_dialog("Order Shipped and email sent", f"Order ID: {self.order.order_id} added to shipping list\n\n{email.send(self.order.email)}")
            #When using the custom email notifcation message
            else:
                email.to_send = self.custom_email_message
                #If the email system was impliemtned email.send() would be called here
                self.show_alert_dialog("Order Shipped and custom email sent", f"Order ID: {self.order.order_id} added to shipping list\n\n{email.send(self.order.email)}")
        #When order is out of stock so cannot be sent to shipping
        elif self.order.item.stock == 0:
            self.show_alert_dialog("item Out of Stock", "This item is out of stock and cannot be added to shipping")
        #When order has already been sent for shipping
        elif self.order.order_status != 'Ready':
            self.show_alert_dialog("Order Already Shipping", "This item has already been added to the shipping list")

    def print_address_label(self):
        '''Will open up file dialog to get location of PDF then
        print it if one is selected via the select_path callback
        '''
        self.file_manager.show(os.path.expanduser("~")) # output manager to the screen at the home directory


    def select_path(self, path):
        '''It will be called when you click on the file name
        or the catalog selection button.
        :type path: str;
        :param path: path to the selected directory or file;
        '''

        self.exit_manager()
        self.order.print_pdf(path)

    def exit_manager(self, *args):
        '''Called when the user reaches the root of the directory tree.'''

        self.file_manager.close()
    
    def show_alert_dialog(self, popup_title, body):
        '''Called when the user reaches the root of the directory tree.
        :param popup_title: str: Title of the dialog
        :param Body: str: Body of the dialog
        '''
        self.dialog = MDDialog(
            title = popup_title,
            text= body,
            buttons=[MDFlatButton(text="OK", on_press=self.alert_dialog_close)])
        self.dialog.open()
    
    def alert_dialog_close(self, *args):
        '''Closes the alert dialog
        '''
        self.dialog.dismiss(force=True)

    def set_custom_email(self):
        self.custom_email_message = self.ids.custom_email_input.text