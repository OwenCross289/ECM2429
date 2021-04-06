from kivymd.uix.list import ThreeLineListItem
from kivymd.uix.screen import MDScreen
from kivymd.toast import toast
from Models.Order import Order
from functools import partial
import Database.DatabaseHandler as db

class GenericEmailScreen(MDScreen):
    '''ViewModel for GenericEmailView
    '''

  
    def on_pre_enter(self):
        '''Called when view is navigated to
        '''
        orders = db.get_ready_orders()
        