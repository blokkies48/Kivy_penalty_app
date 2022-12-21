from kivy.uix.screenmanager import Screen



class MainView(Screen):
    # Class variables
    current_tab_name : str = None;
    user_data : list[str] = [];
    

    def current_tab(self, active_tab):
        self.current_tab_name = active_tab.name

        print(self.current_tab_name)

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
