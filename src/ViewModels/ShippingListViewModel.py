from kivy.properties import BooleanProperty
from kivymd.uix.list import ThreeLineListItem
from kivymd.uix.screen import MDScreen
from kivymd.toast import toast
from Models.Order import Order
import Database.DatabaseHandler as db

class ShippingListScreen(MDScreen):

    def on_pre_enter(self):
        orders = db.get_shipping_orders()
        self.ids.shipping_list.clear_widgets()
        for order in orders:
            list_item = ThreeLineListItem(text=f"Order ID: {order.order_id}", secondary_text=f"Customer Name: {order.customer_name}", tertiary_text=f"Item: {order.item.item_name}",divider="Inset", font_style="H6")
            self.ids.shipping_list.add_widget(list_item)