from kivy.uix.screenmanager import Screen
# Pushes text input above virtual keyboard
from kivy.core.window import Window
Window.softinput_mode = "below_target"
#


from datetime import date, datetime
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog

import os
import geocoder

class PenaltiesView(Screen):
    content = []

    def load_content(self):
        with open("logged_in_user_data.txt", "r") as f:
            for line in f:
                self.content.append(line)
        # For the map
        g_location = geocoder.ip('me')
        lat = g_location.latlng[0]
        lon = g_location.latlng[1]
        map_marker = self.ids.marker
        map_marker.lat = lat
        map_marker.lon = lon
        g_map = self.ids.map
        g_map.lat = lat
        g_map.lon = lon
        g_map.zoom = 15
        # Auto filled in fields
        self.ids.supervisor.text = f"Report done by: {self.content[1].capitalize()}"
        self.ids.date.text = f"On: {date.today()}"
        self.ids.time.text = f"At: {datetime.now().strftime('%H:%M:%S')}"
        # TODO:
        # Load images
        if os.path.isfile('signatures.png'):
            self.ids.signed.text = "Signed"
        else:
            self.ids.signed.text = "Not signed"


    def back(self):

        if "admin" in self.content[-1]:
            self.manager.current = 'AdminView'
            self.manager.transition.direction = 'right'
        else:
            self.manager.current = 'UserView' 
            self.manager.transition.direction = 'right'
        self.content = []
        if os.path.isfile('signatures.png'):
            os.remove("signatures.png")

    def sign(self):
        self.manager.current = "SignatureView"



     


    
    