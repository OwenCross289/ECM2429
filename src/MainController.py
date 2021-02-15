from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

from kivymd.app import MDApp
from kivymd.theming import ThemeManager

class MainController(MDApp):
    def build(self):
        self.title = 'ECM2429 Assignment'
        self.theme_cls = ThemeManager()
        self.theme_cls.theme_style = "Light" #"Light" / "Dark" 
        return Builder.load_file("MainView.kv")
    
    def show_home(self, screen_manager):
        screen_manager.current = "HomeScreen"

MainController().run()