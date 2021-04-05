from kivy.properties import BooleanProperty
from kivymd.uix.list import OneLineListItem
from kivymd.uix.screen import MDScreen
from kivymd.toast import toast
from Models.Order import Order
import Database.DatabaseHandler

class PickingListScreen(MDScreen):
    list_created = BooleanProperty(False)

    def on_pre_enter(self):
        #Bind this list up to your list of objects to be picked then go to an individual item screen on click
        order = Database.DatabaseHandler.get_order(1)
        if not self.list_created:
            items = [
                "Manage accounts",
                "Tax documents",
                "Passcode and Touch ID",
                "Notifications",
                "Personal Information",
                "Paperless settings",
                "Find ATMs",
                "Help",
                "Sign out",
            ]
            for i in items:
                list_item = OneLineListItem(
                    text=order.customer_name, divider="Inset", font_style="H6"
                )
                self.ids.picking_list.add_widget(list_item)
            self.list_created = True
    

    def refresh_button_clicked(self):
        toast("Current ready orders have been refreshed")
   
