from kivymd.uix.list import ThreeLineListItem
from kivymd.uix.screen import MDScreen
from kivymd.toast import toast
from Models.Order import Order
from functools import partial
import Database.DatabaseHandler as db

class PickingListScreen(MDScreen):
    '''ViewModel for PickingListView
    '''

    
    def on_pre_enter(self):
        '''Called when view is navigated to
        '''
        orders = db.get_ready_orders()
        self.ids.picking_list.clear_widgets()
        for order in orders:
            list_item = ThreeLineListItem(text=f"Order ID: {order.order_id}", secondary_text=f"Customer Name: {order.customer_name}", tertiary_text=f"Item: {order.item.item_name}",divider="Inset", font_style="H6")
            list_item.bind(on_press=partial(self.navigate_to_item_screen, order.order_id))
            self.ids.picking_list.add_widget(list_item)
    

    def refresh_button_clicked(self):
        '''Calls the API to get more orders
        '''
        db.update_order_status(1, "Ready")
        toast("Current ready orders have been refreshed")

    def navigate_to_item_screen(self, order_id, *args):
        '''Navigates to OrderView
        :param order_id: int: ID of Order in database to be passed to OrderViewModel
        '''
        self.ids.screen_manager.transition.direction = "up"
        self.ids.screen_manager.get_screen('OrderScreen').order_id = order_id
        self.ids.screen_manager.current = "OrderScreen"
        toast(f"You clicked order with ID {order_id}")
   
