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

#View imports
from view_user import UserView
from view_login import LoginView
from view_registration import RegistrationView
from view_penalties import PenaltiesView
from view_admin import AdminView
from view_signatures import SignatureView

# Handle back button
from back_button_pressed import *
press_back()

THEME_ = "Dark"
THEME_PALETTE = "Blue"

class MainApp(MDApp):
    def theme_(self):
        self.theme_cls.theme_style = THEME_
        self.theme_cls.primary_palette = THEME_PALETTE

    def load_design(self):

        self.icon = "logo.png"
        Builder.load_file(r"kivy_user_view.kv")
        Builder.load_file(r"kivy_login_view.kv")
        Builder.load_file(r"kivy_registration_view.kv")
        Builder.load_file(r"kivy_penalties_view.kv")
        Builder.load_file(r"kivy_admin_view.kv")
        Builder.load_file(r"kivy_signature_view.kv")

    def build(self):
        # Theme style
        self.theme_()

        # Design Files
        self.load_design()

        screen_manager = ScreenManager()

        screen_manager.add_widget(LoginView(name = "LoginView"))
        screen_manager.add_widget(AdminView(name = "AdminView"))
        screen_manager.add_widget(UserView(name = "UserView"))
        screen_manager.add_widget(PenaltiesView(name = "PenaltiesView"))
        screen_manager.add_widget(RegistrationView(name = "RegistrationView"))
        screen_manager.add_widget(SignatureView(name = "SignatureView"))
        return screen_manager


if __name__ == "__main__":

    MainApp().run()

