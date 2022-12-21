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


error_occurred: bool = False

# TODO: Add Functionality to check if there is a logged in user or not 

from mainView import MainView

from loginView import LoginView
from registrationView import RegistrationView


logged_in: bool = False

THEME_ = "Dark"
THEME_PALETTE = "Blue"

class MainApp(MDApp):
    def theme_(self):
        self.theme_cls.theme_style = THEME_
        self.theme_cls.primary_palette = THEME_PALETTE

    def load_design(self):

        self.icon = "logo.png"
        Builder.load_file(r"mainView.kv")

        Builder.load_file(r"loginView.kv")
        Builder.load_file(r"registrationView.kv")

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
        else:
            # Screens
            screen_manager.add_widget(MainView(name = "MainView"))
            screen_manager.add_widget(LoginView(name = "LoginView"))
            screen_manager.add_widget(RegistrationView(name = "RegistrationView"))

        return screen_manager

if __name__ == "__main__":
    # Check there is a logged in user
    # TODO: Have to make this more secure and tamper proof
    # Seems too hacky
    with open("loggedInUser.txt", "r",encoding='ascii') as f:
        content: str = ''
        for line in f:
            content += line
        if content != "":
            logged_in = True
    MainApp().run()

