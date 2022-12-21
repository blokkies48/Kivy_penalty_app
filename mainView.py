from kivy.uix.screenmanager import Screen



class MainView(Screen):
    # Class variables
    current_tab_name : str = None;
    user_data : list[str] = [];
    

    def current_tab(self, active_tab):
        self.current_tab_name = active_tab.name

        print(self.current_tab_name)

    def logout(self):

        with open(r"loggedInUser.txt", "w",encoding='ascii') as f:
            f.write('')
        self.manager.current = 'LoginView'
        self.manager.transition.direction = 'right' 

    def on_load(self):
        self.user_data = []
        with open(r"loggedInUser.txt", 'r',encoding='ascii') as f:
            for line in f:
                self.user_data.append(line.strip("\n"))

        self.ids.user_name.text = ("Hi, " 
        + self.user_data[1].capitalize())

        #  certifi==2022.12.7,charset-normalizer==2.1.1,docutils==0.19,idna==3.4,Kivy==2.1.0,kivy-deps.angle==0.3.3,kivy-deps.glew==0.3.1,kivy-deps.sdl2==0.4.5,Kivy-Garden==0.1.5,kivymd==1.0.2,mysql-connector==2.2.9,mysql-connector-python==8.0.31,Pillow==9.3.0,protobuf==3.20.1,Pygments==2.13.0,pypiwin32==223,pywin32==305,requests==2.28.1,urllib3==1.26.13