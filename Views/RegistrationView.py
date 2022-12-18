from kivy.uix.screenmanager import Screen
from kivy.clock import Clock

from Tables.UserTable import *

class RegistrationView(Screen):
    def register_user(
        self,
        user_name,
        user_password,
        user_password_2,
        login_error):

        # Test cases
        passwords_equals = user_password.text == user_password_2.text
        passwords_empty_1 = not user_password.text
        passwords_empty_2 = not user_password_2.text
        username_empty = not user_name.text
        
        # Checks if the fields are correct
        if (passwords_equals and not username_empty 
            and not passwords_empty_1 and not passwords_empty_2):
                # Goes to additional checks
                self.add_the_user(user_name.text, user_password.text)
        elif username_empty and passwords_equals:
            login_error.text = "Name field is required"
            Clock.schedule_once(self.update_label, 2)  
        elif username_empty or passwords_empty_1 or passwords_empty_2:
            login_error.text = "Please enter required fields"
            user_password_2.text = ""
            Clock.schedule_once(self.update_label, 2) 
        elif not passwords_equals:
            login_error.text = "Passwords don't match"
            user_password_2.text = ""
         
    def add_the_user(self, user_name, user_password):
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
        # If the username is already taken
        elif user_name in all_user_names():
            self.ids.login_error.text = "Username already taken"
            self.ids.reg_user_name.text = ""
            Clock.schedule_once(self.update_label, 5)
        # If passed all checks then the user can be registered
        else: 
            AddUser(user_name.capitalize(), user_password).add_user()
            self.ids.reg_user_name.text = ""
            self.ids.reg_user_password.text = ""
            self.ids.reg_user_password_2.text = ""

    def update_label(self, *args):
        self.ids.login_error.text = ''


    # Methods used to check the if there is a digit or character
    def has_numbers(self,inputString):
        return any(char.isdigit() for char in inputString)
    def has_char(self,inputString):
        return any(letter.isalpha() for letter in inputString)


            
        
     