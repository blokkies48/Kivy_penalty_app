from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.graphics import Ellipse, Color, Line
import os

# Code from https://groups.google.com/g/kivy-users/c/ib2NUFOnHeQ
class SignatureView(Screen):
    def on_pre_enter(self, *args):
        pass
    def clear_pressed(self):
        if os.path.isfile('signatures.png'):
            os.remove("signatures.png")

    def _exportImage(self):
        dirname = r""
        # TODO: CHANGE THIS
        #dirname = App.get_running_app().user_data_dir
        filename = os.path.join(dirname, 'signatures.png')
        self.export_to_png(filename)

    


    class MyPaintWidget(Widget):
        def on_touch_down(self, touch):
            color = (1,1,1)
            SignatureView().ids.done.disabled = 'False'
            with self.canvas:
                Color(*color)
                d = 30.
                touch.ud['line'] = Line(points=(touch.x, touch.y), width=1.4)
        def on_touch_move(self, touch):
            touch.ud['line'].points += [touch.x, touch.y]

    

        
