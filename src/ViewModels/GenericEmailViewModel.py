from kivymd.uix.list import ThreeLineListItem
from kivymd.uix.screen import MDScreen
from kivymd.toast import toast
from Models.Email import Email
from functools import partial
import Database.DatabaseHandler as db

class GenericEmailScreen(MDScreen):
    '''ViewModel for GenericEmailView
    '''

  
    def on_pre_enter(self):
        '''Called when view is navigated to
        '''
        self.email = db.get_generic_email_message()
        self.ids.email_message.text = self.email.to_send
        self.ids.addresser_input.text = self.email.addresser
        self.ids.body_input.text = self.email.body
        self.ids.sign_off_input.text = self.email.sign_off
    
    def update_preview(self):
        self.email.addresser = self.ids.addresser_input.text
        self.email.body = self.ids.body_input.text
        self.email.sign_off = self.ids.sign_off_input.text
        self.email.update_full_email()
        self.ids.email_message.text = self.email.to_send

    
    def update_database(self):
        self.update_preview()
        db.update_generic_email_message(self.email)
        