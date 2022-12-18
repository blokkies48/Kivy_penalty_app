from kivy.uix.screenmanager import Screen

class MainView(Screen):
    # Class variables
    current_tab_name : str = None;
    

    def current_tab(self, active_tab):
        self.current_tab_name = active_tab.name

        print(self.current_tab_name)
