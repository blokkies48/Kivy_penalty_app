from kivy.uix.screenmanager import Screen
# Pushes text input above virtual keyboard
from kivy.core.window import Window
Window.softinput_mode = "below_target"
#
from datetime import date, datetime

import os
import geocoder

from view_signatures import SignatureView
from table_penalties_given import AddPenaltyGiven

class PenaltiesView(Screen):
    content = []
    officer_pers_nos = []

    def save_to_database(self):

        location = str(geocoder.ip('me').latlng)
        officer_no = self.ids.officer_on_duty.text
        penalty = self.ids.penalty_selected.text
        site = self.ids.site.text
        report = self.ids.report.text
        supervisor = self.content[1].capitalize()
        date_of_penalty = str(date.today())
        time_of_penalty = str(datetime.now().strftime('%H:%M:%S'))

        # Add penalty check if fails then write to text file data
        try:
            AddPenaltyGiven(
                location=location, officer=officer_no,
                penalty=penalty, site=site, report=report,
                supervisor=supervisor, date=date_of_penalty, time=time_of_penalty
            ).add_penalty_given()
        except:
            with open("penalties.txt", "a") as f:

                f.write("=====")

                f.write(location)
                f.write(officer_no)
                f.write(penalty)
                f.write(site)
                f.write(report)
                f.write(supervisor)
                f.write(date_of_penalty)
                f.write(time_of_penalty)

                f.write("=====")
        self.back()


    def load_content(self):
        with open("officer_selected.txt", "r") as f:
            for line in f:
                
                if "Officer:" in line:
                    new_line = line.strip("Officer: ")
                    self.ids.officer_on_duty.text = str(new_line.strip("\n"))
                    break
            else:
                self.ids.officer_on_duty.text = "Officer's Pers No"

        with open("penalties_selected.txt", "r") as f:
            for line in f:
                
                if "Penalty:" in line:
                    new_line = line.strip("Penalty: ").split(",")
                    
                    self.ids.penalty_selected.text = new_line[0]
                    break
            else:
                self.ids.penalty_selected.text = "Select Penalty"
        
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
        with open("officer_selected.txt", "w") as f:
            f.write("")
        with open("penalties_selected.txt", "w") as f:
            f.write("")

        self.ids.site.text = ''
        self.ids.report.text = ''
        signature_screen = self.manager.get_screen('SignatureView')
        signature_screen.ids._painter_id.canvas.clear()
        signature_screen.ids.is_signed.text = "Not Signed"

        SignatureView().ids._painter_id.canvas.clear()

    def sign(self):
        self.manager.current = "SignatureView"
        self.manager.transition.direction = 'left'


    def select_officer(self):
        self.manager.current = "GuardsView"
        self.manager.transition.direction = 'left'
        
    def select_penalty(self):
        self.manager.current = "PenaltiesListView"
        self.manager.transition.direction = 'left'



     


    
    