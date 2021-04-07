import os
import sys
from pathlib import Path
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

from kivymd.app import MDApp
from kivymd.theming import ThemeManager

#This code is used when packaging the app into an exe 
#if getattr(sys, "frozen", False):  # bundle mode with PyInstaller
#    os.environ["RALLY_ROOT"] = sys._MEIPASS
#else:
#os.environ["RALLY_ROOT"] = str(Path(__file__).parent)

#This section of code loads in all of the view files for mapping to their respective View Model 
KV_DIR = f"{str(Path(__file__).parent)}/Views/"
for kv_file in os.listdir(KV_DIR):
    with open(os.path.join(KV_DIR, kv_file), encoding="utf-8") as kv:
        Builder.load_string(kv.read())

class MainViewModel(MDApp):
    '''ViewModel for MainView
    '''

    def build(self):
        '''Builds the appplication
        '''
        self.title = 'ECM2429 Assignment'
        self.theme_cls = ThemeManager()
        self.theme_cls.theme_style = "Light" #"Light" / "Dark"
        return Builder.load_file("MainView.kv")
    

    def navigate_home(self, screen_manager, toolbar):
        '''Navigates to HomeScreen
        '''
        screen_manager.transition.direction = "right"
        screen_manager.current = "HomeScreen"
        toolbar.title = "Home"

    def navigate_shipping(self, screen_manager, toolbar):
        '''Navigates to ShippingListView
        '''
        screen_manager.transition.direction = "right"
        screen_manager.current = "ShippingListScreen"
        screen_manager.get_screen("ShippingListScreen").on_pre_enter()
        toolbar.title = "Shipping List"

    def navigate_picking(self, screen_manager, toolbar):
        '''Navigates to ShippingListView
        '''
        screen_manager.transition.direction = "right"
        screen_manager.current = "PickingListScreen"
        screen_manager.get_screen("PickingListScreen").on_pre_enter()
        toolbar.title = "Picking List"

    def navigate_generic_email(self, screen_manager, toolbar):
        '''Navigates to ShippingListView
        '''
        screen_manager.transition.direction = "right"
        screen_manager.current = "EmailScreen"
        screen_manager.get_screen("EmailScreen").on_pre_enter()
        toolbar.title = "Generic Email Message"
        



MainViewModel().run()
