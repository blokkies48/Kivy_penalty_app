from kivy.uix.screenmanager import Screen

class PenaltiesView(Screen):

    def load_content(self):
        g_map = self.ids.map
        g_map.lat = -26
        g_map.lon = 28
        g_map.zoom = 11
        pass


    
    