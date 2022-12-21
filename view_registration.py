from kivy.uix.screenmanager import Screen
from kivy.clock import Clock

from table_users import *

class RegistrationView(Screen):
    def register_user(
        self,
        user_name,
        user_password,
        user_password_2,
        login_error):

        # lower case and getting text
        user_name = user_name.text.lower()
        user_password = user_password.text
        user_password_2 = user_password_2.text

        # Test cases
        passwords_equals = user_password == user_password_2
        passwords_empty_1 = not user_password
        passwords_empty_2 = not user_password_2
        username_empty = not user_name
        
        # Checks if the fields are correct
        if (passwords_equals and not username_empty 
            and not passwords_empty_1 and not passwords_empty_2):
                # Goes to additional checks
                self.add_the_user(user_name, user_password)

        elif (username_empty and passwords_equals 
        and not passwords_empty_1 and not passwords_empty_2):
            login_error.text = "Name field is required"
            Clock.schedule_once(self.update_label, 2) 

        elif username_empty or passwords_empty_1 or passwords_empty_2:
            login_error.text = "Please enter required fields"
            user_password_2 = ""
            Clock.schedule_once(self.update_label, 2) 

        elif not passwords_equals:
            login_error.text = "Passwords don't match"
            user_password_2 = ""
         
    def add_the_user(self, user_name, user_password):
        # Check if table exists
        table_exists = True
        try:
            all_user_names()
        except:
            table_exists = False

        # If the username is already taken
        if table_exists:
            if user_name in all_user_names():
                self.ids.login_error.text = "Username already taken"
                self.ids.reg_user_name.text = ""
                Clock.schedule_once(self.update_label, 5)
                return None

        # Validation checks
        # User name length check
        if len(user_name) < 5:
            self.ids.login_error.text = "User name can't be less than 5 characters"
            Clock.schedule_once(self.update_label, 5)

        # Password length check
        elif len(user_password) < 8 :
            self.ids.login_error.text = "Passwords needs to be at least 8"
            Clock.schedule_once(self.update_label, 5)

        # Make sure password has numbers and characters in it
        elif not (self.has_numbers(user_password)) or not self.has_char(user_password):
            self.ids.login_error.text = "Password requires at least one digit or character"
            Clock.schedule_once(self.update_label, 5)

        # If passed all checks then the user can be registered
        else: 
            try:
                AddUser(user_name.lower(), user_password.lower()).add_user()
                self.ids.reg_user_name.text = ""
                self.ids.reg_user_password.text = ""
                self.ids.reg_user_password_2.text = ""
            except Exception as e:
                print(e)
                self.ids.login_error.text = "No connection please try again"



    def update_label(self, *args):
        self.ids.login_error.text = ''


    # Methods used to check the if there is a digit or character
    def has_numbers(self,inputString):
        return any(char.isdigit() for char in inputString)
    def has_char(self,inputString):
        return any(letter.isalpha() for letter in inputString)


            
        
     