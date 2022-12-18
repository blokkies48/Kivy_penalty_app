from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager

error_occurred: bool = True

# TODO: Add Functionality to check if there is a logged in user or not 
logged_in: bool = True

try:
    # Views
    from Views.MainView import MainView
    from Views.LoginView import LoginView
    from Views.RegistrationView import RegistrationView
except Exception as error:
    from Views.ErrorView import ErrorView
    error_occurred = True
    error_message = error


THEME_ = "Light"
THEME_PALETTE = "Red"

class MainApp(MDApp):
    def theme_(self):
        self.theme_cls.theme_style = THEME_
        self.theme_cls.primary_palette = THEME_PALETTE

    def load_design(self):

        self.icon = r"DesignFiles\logo.png"
        Builder.load_file(r"DesignFiles\MainView.kv")

        if not error_occurred:
            Builder.load_file(r"DesignFiles\LoginView.kv")
            Builder.load_file(r"DesignFiles\RegistrationView.kv")
        else:
            Builder.load_file(r"DesignFiles\ErrorView.kv")

    def build(self):
        # Theme style
        self.theme_()

        # Design Files
        self.load_design()

        screen_manager = ScreenManager()

        if not error_occurred:
            # Screens
            screen_manager.add_widget(LoginView(name = "LoginView"))
            screen_manager.add_widget(RegistrationView(name = "RegistrationView"))
        else:
            if not logged_in:
                screen_manager.add_widget(ErrorView(
                name = "ErrorView", error_type=error_message))
            else:
                screen_manager.add_widget(MainView(name = "MainView"))
        return screen_manager


if __name__ == "__main__":
    MainApp().run()

