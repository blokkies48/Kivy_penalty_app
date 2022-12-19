from kivy.uix.screenmanager import Screen
from kivy.clock import Clock

from Tables.UserTable import *




# TODO: 
class LoginView(Screen):
    def login(self, username, user_password):

        username: str = username.text
        user_password: str = user_password.text

        try:
            password_check = False
            #CurrentUser().get_user()
            print("Logging in...")
            allUsers()
            user = CurrentUser().get_user(username.lower())
            # TODO: remove before production
            print(user)

            if user_password in user:
                password_check = True

            # Logic for when user logs in
            if password_check:
                with open(r"User_info\LoggedInUser.csv", "w") as f:
                    for item in user:
                        f.write(str(item) + "\n")
                self.manager.current = 'MainView'
                self.manager.transition.direction = 'left'
        except:
            self.ids.login_error.text = "Invalid Login"
            Clock.schedule_once(self.update_label, 5)


    def update_label(self, *args):
        self.ids.login_error.text = ''
            
