from kivy.uix.screenmanager import Screen
from kivy.app import App

class ErrorView(Screen):
    def __init__(self, error_type,**kw):
        super().__init__(**kw)
        self.error_type =  error_type
        self.ids.error_type.text = str(error_type)
    # Extend reload functionality 
    def reload(self):
        App.get_running_app().stop()