from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager

import ssl
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context


from view_main import MainView
from view_login import LoginView
from view_registration import RegistrationView
from view_penalties import PenaltiesView

from back_button_pressed import *
press_back()

logged_in: bool = False

THEME_ = "Dark"
THEME_PALETTE = "Blue"

class MainApp(MDApp):
    def theme_(self):
        self.theme_cls.theme_style = THEME_
        self.theme_cls.primary_palette = THEME_PALETTE

    def load_design(self):

        self.icon = "logo.png"
        Builder.load_file(r"kivy_main_view.kv")

        Builder.load_file(r"kivy_login_view.kv")
        Builder.load_file(r"kivy_registration_view.kv")
        Builder.load_file(r"kivy_penalties_view.kv")

    def build(self):
        # Theme style
        self.theme_()

        # Design Files
        self.load_design()

        screen_manager = ScreenManager()

        if not logged_in:
            # Screens
            screen_manager.add_widget(LoginView(name = "LoginView"))
            screen_manager.add_widget(RegistrationView(name = "RegistrationView"))
            screen_manager.add_widget(MainView(name = "MainView"))
            screen_manager.add_widget(PenaltiesView(name = "PenaltiesView"))
        else:
            # Screens
            screen_manager.add_widget(MainView(name = "MainView"))
            screen_manager.add_widget(LoginView(name = "LoginView"))
            screen_manager.add_widget(RegistrationView(name = "RegistrationView"))
            screen_manager.add_widget(PenaltiesView(name = "PenaltiesView"))

        return screen_manager

if __name__ == "__main__":
    # Check there is a logged in user
    # TODO: Have to make this more secure and tamper proof
    # Seems too hacky
    with open("logged_in_user_data.txt", "r",encoding='ascii') as f:
        content: str = ''
        for line in f:
            content += line
        if content != "":
            logged_in = True
    MainApp().run()

