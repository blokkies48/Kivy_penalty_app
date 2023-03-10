from kivy.uix.screenmanager import Screen
from kivymd.uix.list import OneLineListItem
from table_users import *
from kivy.clock import Clock

from threading import Thread



class AdminView(Screen):
    # Class variables
    current_tab_name : str = 'Penalties';
    user_data : list[str] = [];
    users_loaded : bool = True;

    def current_tab(self, active_tab):
        self.current_tab_name = active_tab.name
        if self.current_tab_name != "Users":
            self.remove_content()
        elif self.current_tab_name == "Users" and not self.users_loaded:
            self.load_users()
            self.users_loaded = True

    def logout(self):
        with open(r"logged_in_user_data.txt", "w",encoding='ascii') as f:
            f.write('')
        self.manager.current = 'LoginView'
        self.manager.transition.direction = 'right' 

    def on_load(self):
        self.user_data = []
        with open(r"logged_in_user_data.txt", 'r',encoding='ascii') as f:
            for line in f:
                self.user_data.append(line.strip("\n"))

        self.ids.user_name.text = ("Hi, " 
        + self.user_data[1].capitalize())

        Clock.schedule_once(self.load_users, 5)
        self.users_loaded = True

        def show_loading():
            self.ids.error_message.color = 'grey'
            self.ids.error_message.text = "Loading Users, Please Wait..."
            Clock.schedule_once(self.update_label, 5)

        show_loading()

        self.get_users_from_db()

    def load_users(self, *args):
        if len(self.ids.all_users_list.children) == 0:
            try:
                # Need index 0,1,3 to display
                with open("text_all_users.txt", "r") as f:
                    for user in f:
                        name = user.split(" ")
                        widget = OneLineListItem(
                            text = f"ID: {name[0]}, Name: {name[1].capitalize()}, Role: {name[3].capitalize()}",
                            on_release = self.select_user
                        )
                        self.ids.all_users_list.add_widget(widget)    
            except:
                self.ids.error_message.color = 'red'
                self.ids.error_message.text = "Error reload"
                Clock.schedule_once(self.update_label, 5)
        if len(self.ids.all_users_list.children) == 0:
            self.ids.error_message.color = 'red'
            self.ids.error_message.text = "Error reload"
            Clock.schedule_once(self.update_label, 5)

    # TODO: When user is selected       
    def select_user(self, list_item):
        print(list_item.text)

    def update_label(self, *args):
        self.ids.error_message.text = ''


    def remove_content(self):
        self.ids.all_users_list.clear_widgets()
        self.users_loaded = False


    def fab_pressed(self):
        if self.current_tab_name != None:
            
            if self.current_tab_name == "Users":
                self.manager.current = 'RegistrationView'
                self.manager.transition.direction = 'left'
            elif self.current_tab_name == "Penalties":
                print("Added Penalties")

    # Clock.schedule_once(self.background_load, 5)
    def get_users_from_db(self):
        # Clock.schedule_once(self.background_load_users, 0.001)
        
        t = Thread(target=self.background_load_users, args=(2, 5))
        t.daemon = True
        t.start()


    def background_load_users(self, *args):
        try:
            with open("text_all_users.txt", "w") as f:
                for user in all_users():
                    for item in user:
                        f.write(str(item) + " ")
                    f.write("\n")
        except:
            self.ids.database_error.color = 'red'
            self.ids.database_error.text = "Database error, reload app"

    def add_penalty(self):
        self.manager.current = 'PenaltiesView'
        self.manager.transition.direction = 'left'
