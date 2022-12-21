from kivy.base import EventLoop
from kivymd.uix.button import MDFlatButton

from kivymd.uix.dialog import MDDialog
from kivy.core.window import Window


    


def hook_keyboard(window, key, *largs):

    def close_dialog(obj):
        dialog.dismiss()

    def close_app(obj):
        quit()

    dialog = None
    if key == 27:
        if not dialog:
            dialog = MDDialog(
                title = "Exit",
                text = "All unsaved changes will be lost.\nAre you sure you want to exit?",
                buttons = [
                    MDFlatButton(
                        text = "Cancel",
                        on_press = close_dialog
                    ),
                    MDFlatButton(
                        text = "Exit",
                        on_press = close_app
                    )
                ],
            )
        dialog.open()
        def close_dialog(obj):
            dialog.dismiss()
    return True

def press_back():
    EventLoop.window.bind(on_keyboard=hook_keyboard)