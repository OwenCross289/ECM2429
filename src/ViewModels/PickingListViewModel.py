from kivy.properties import BooleanProperty
from kivymd.uix.list import OneLineListItem
from kivymd.uix.screen import MDScreen

class PickingListScreen(MDScreen):
    list_created = BooleanProperty(False)

    def on_pre_enter(self):
        #Bind this list up to your list of objects to be picked then go to an individual item screen on click
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
                    text=i, divider="Inset", font_style="H6"
                )
                self.ids.picking_list.add_widget(list_item)
            self.list_created = True

    
