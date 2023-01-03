from kivy.uix.screenmanager import Screen
from kivy.clock import Clock

from table_users import *
# Pushes text input above virtual keyboard
from kivy.core.window import Window
Window.softinput_mode = "below_target"

# For login user
from kivy.uix.screenmanager import NoTransition, SlideTransition


from table_guards import all_guard_pers


# TODO: 
class LoginView(Screen):
    content: list[str] = []

    def login(self, username, user_password):
        self.ids.login_error.color = 'grey'
        self.ids.login_error.text = "Logging in please wait..."
        Clock.schedule_once(lambda _: self.login_logic(username, user_password), 0.001)

    def login_logic(self, username, user_password, *args):
        try:
            username: str = username.text
            user_password: str = user_password.text

            if username != "" and user_password != "":
                user = CurrentUser().get_user(username.lower())
                # TODO: remove before production
                print(user)
                    
                if user_password in user:
                    # User details
                    # TODO: Add user time stamp here
                    with open(r"logged_in_user_data.txt", "w",encoding='ascii') as f:
                        for item in user:
                            f.write(str(item) + "\n")
                    self.ids.user_name.text = ''
                    self.ids.user_password.text = ''
                    Clock.schedule_once(self.update_label, 5)
                    # Get pers_no 
                    with open("pers_no.txt" , "w", encoding="ascii") as f:
                        for number in all_guard_pers():
                            f.write(str(number) + "\n")
                    # Determines user or admin 
                    if user[-1] == 'admin':
                        print((user[-1]) + "Logged in admin")
                        self.manager.current = 'AdminView'
                        self.manager.transition.direction = 'left'
                    else:
                        self.manager.current = 'UserView'
                        self.manager.transition.direction = 'left'
                else:
                    self.ids.login_error.color = 'red'
                    self.ids.login_error.text = "Enter a valid password"
                    self.ids.user_password.text = ''
                    Clock.schedule_once(self.update_label, 5)

            else:
                self.ids.login_error.color = 'red'
                self.ids.login_error.text = "Don't leave the fields empty"
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
            # TODO: fix error message before production
            self.ids.login_error.text = str(e)
            Clock.schedule_once(self.update_label, 5)

    def update_label(self, *args):
        self.ids.login_error.text = ''

    # Check there is a logged in user
    # TODO: Have to make this more secure and tamper proof
    # Seems too hacky
    def check_login(self):
        try:
            with open("logged_in_user_data.txt", "r",encoding='ascii') as f:
                self.content: list[str] = []
                for line in f:
                    self.content.append(line.strip("\n"))
                return len(self.content) != 0, self.content[-1] == "admin"
        except:
            return False, False

    def on_start(self):
        Clock.schedule_once(self.if_logged_in, .00001)
    
    # TODO: Add logic to check time stamp
    def if_logged_in(self, *args):
        login_info = self.check_login()
        print(login_info)
        # If logged in and is a admin
        # (if logged in, if admin) how tuple works
        if (login_info[0] and login_info[1]):
            username = self.content[1]
            user = CurrentUser().get_user(username.lower())
            if "admin" in user and user[2] == self.content[2]:
                self.manager.transition = NoTransition()
                self.manager.current = 'AdminView'
                self.manager.transition = SlideTransition()
        elif login_info[0]:
            self.manager.transition = NoTransition()
            self.manager.current = 'UserView'
            self.manager.transition = SlideTransition()

            
