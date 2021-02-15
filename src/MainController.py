from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.theming import ThemeManager

class ListView():
    def __init__(self, x):
        x = 1

    def change_text(self, t):
        t.text = "CHANGED!"

class MainController(MDApp):
    ListViewController = ListView(1)
    def build(self):
        self.title = 'ECM2429 Assignment'
        self.theme_cls = ThemeManager()
        self.theme_cls.theme_style = "Light" #"Light" / "Dark" 
        return Builder.load_file("MainView.kv")
    
    def show_home(self, screen_manager):
        screen_manager.current = "HomeScreen"
    
    def change_text(self):
       print("hehehe")

MainController().run()