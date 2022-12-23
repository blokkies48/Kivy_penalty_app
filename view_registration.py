from kivy.uix.screenmanager import Screen
from kivy.clock import Clock

# What was this for again??? 
from kivy.core.window import Window
Window.softinput_mode = "below_target"
#
# For role selection

#  

from table_users import *

class RegistrationView(Screen):
    def register_user(
        self,
        user_name,
        user_password,
        user_password_2,
        user_role,
        login_error):
            self.ids.login_error.color = 'grey'
            self.ids.login_error.text = "Registering user please wait..."
            Clock.schedule_once(lambda _: self.register_user_next(
            user_name,user_password,user_password_2,user_role,login_error), 0.001)
    user_role: str = "None"
    def register_user_next(
        self,
        user_name,
        user_password,
        user_password_2,
        user_role,
        login_error):
        self.ids.login_error.color = 'red'
        # lower case and getting text
        user_name = user_name.text.lower()
        user_password = user_password.text
        user_password_2 = user_password_2.text
        user_role = user_role.text

        # Test cases
        passwords_equals = user_password == user_password_2
        passwords_empty_1 = not user_password
        passwords_empty_2 = not user_password_2
        username_empty = not user_name
        user_role_incorrect = user_role == "Select role"

        


        if (username_empty and passwords_equals 
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
         
        elif user_role_incorrect:
            login_error.text = "Please select a user role"
            Clock.schedule_once(self.update_label, 2) 

        # Validation checks
        # User name length check
        elif len(user_name) < 5:
            self.ids.login_error.text = "User name can't be less than 5 characters"
            Clock.schedule_once(self.update_label, 5)

        # Password length check
        elif len(user_password) < 8 :
            self.ids.login_error.text = "Passwords needs to be at least 8 characters"
            Clock.schedule_once(self.update_label, 5)

        # Make sure password has numbers and characters in it
        elif not (self.has_numbers(user_password)) or not self.has_char(user_password):
            self.ids.login_error.text = "Password requires at least one digit and character"
            Clock.schedule_once(self.update_label, 5)

        # If passed all checks then the user can be registered
        # Checks if the fields are correct
        elif (passwords_equals and not username_empty 
            and not passwords_empty_1 and not passwords_empty_2
            and not user_role_incorrect):
                # Goes to additional checks
                self.add_the_user(user_name, user_password,user_role)
                # TODO: Remove this before production
                print(user_name, user_password,user_role)
        

    def add_the_user(self, user_name, user_password,user_role):

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
        
        failed: bool = False 
        try:
            Clock.schedule_once(lambda x : self.add_to_database(
            user_name.lower(), user_password.lower(), user_role.lower()), .001)
            self.ids.reg_user_name.text = ""
            self.ids.reg_user_password.text = ""
            self.ids.reg_user_password_2.text = ""
            self.ids.reg_user_role.text = 'Select role'
            self.ids.login_error.color = 'grey'
            self.ids.login_error.text = "Registration was successful!"
            Clock.schedule_once(self.update_label, 8)
            
        except Exception as e:
            print(e)
            failed = True
            self.ids.login_error.color = 'red'
            self.ids.login_error.text = "Error occurred No connection please try again"
            Clock.schedule_once(self.update_label, 8)
        # Check if table exists
       

    def add_to_database(self,user_name, user_password, user_role):
        AddUser(user_name, user_password, user_role).add_user()


    def update_label(self, *args):
        self.ids.login_error.text = ''


    # Methods used to check the if there is a digit or character
    def has_numbers(self,inputString):
        return any(char.isdigit() for char in inputString)
    def has_char(self,inputString):
        return any(letter.isalpha() for letter in inputString)

    # Open role selection

    def open_role_selection(self):
        def close_dialog(obj):
            dialog.dismiss()

        def select_role(obj):
            if obj.text == "None":
                self.ids.reg_user_role.text = "Select role"
            else:    
                self.ids.reg_user_role.text = obj.text
            close_dialog(obj)


        dialog = None
        if not dialog:
            dialog = MDDialog(
                title="Select role",
                type="confirmation",
                items=[
                    ItemConfirm(text="Admin", on_release=select_role),
                    ItemConfirm(text="User", on_release=select_role),
                    ItemConfirm(text="None", on_release=select_role),
                ],
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        on_release=close_dialog
                    ),
                ],
            )
        dialog.open()

from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineAvatarIconListItem


class ItemConfirm(OneLineAvatarIconListItem):
    divider = None

    def set_icon(self, instance_check):
        pass
# END SELECT ROLE POPUP

'''
Creating an app from scratch using python, kivy, kivymd, mysql, and more for my first client. I used some of my knowledge from my first attempt at my demo app. 



Some features that I have included so far.

- Connecting to an online hosted database rather than a locally hosted SQL server.

- Multi-threading is used to load users.

- Bunch of password and registration checks.

- Map feature that works with geo location.

- And much more to come.



I have also done a lot of testing using android devices along side android studio.

I used buildozer and google colab to build the apk. 



This is the start and the app is still buggy and requires a lot more tweaks and a lot more functionality. 



Thought I might as well document my progress and see how I improve over time.



This took me about a few days of work so far, but I have learned a lot and want to thank Madeleine Greyling and SEKURITEIT SONDER GRENSE GAUTENG for the opportunity to do this. 
'''

