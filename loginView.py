from kivy.uix.screenmanager import Screen
from kivy.clock import Clock

from userTable import *

# TODO: 
class LoginView(Screen):
    def login(self, username, user_password):
        self.ids.login_error.color = 'grey'
        self.ids.login_error.text = "Logging in please wait..."
        Clock.schedule_once(lambda _: self.login_logic(username, user_password), 0.1)

    def login_logic(self, username, user_password, *args):
        try:
            username: str = username.text
            user_password: str = user_password.text

            user = CurrentUser().get_user(username.lower())
            # TODO: remove before production
            print(user)


            if user_password in user:
                with open(r"loggedInUser.txt", "w",encoding='ascii') as f:
                    for item in user:
                        f.write(str(item) + "\n")
                self.ids.user_name.text = ''
                self.ids.user_password.text = ''
                Clock.schedule_once(self.update_label, 5)
                self.manager.current = 'MainView'
                self.manager.transition.direction = 'left'
            else:
                self.ids.login_error.color = 'red'
                self.ids.login_error.text = "Enter a valid password"
                self.ids.user_password.text = ''
                Clock.schedule_once(self.update_label, 5)
            
        except TypeError as e:
            print(e)
            self.ids.login_error.color = 'red'
            self.ids.login_error.text = "Invalid Login"
            self.ids.user_password.text = ''
            Clock.schedule_once(self.update_label, 5)
        except Exception as e:
            print(e)
            self.ids.login_error.color = 'red'
            self.ids.login_error.text = str(e)
            Clock.schedule_once(self.update_label, 5)

    def update_label(self, *args):
        self.ids.login_error.text = ''

            
