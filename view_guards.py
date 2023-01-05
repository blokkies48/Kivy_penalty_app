from kivy.uix.screenmanager import Screen
from kivymd.uix.list import OneLineListItem
from kivy.uix.label import Label

import re

class GuardsView(Screen):
    search_results = []
    # Add wherever changing screen
    def back(self):
        self.ids.list_of_guards.clear_widgets()
        self.manager.current = "PenaltiesView"
        self.manager.transition.direction = 'right'
    def search(self, keyword):
        self.ids.list_of_guards.clear_widgets()

        with open("pers_no.txt", "r") as f:
            for line in f:
                if keyword in line:
                    cleaned_line_1 = re.findall('[a-zA-Z]', line)
                    cleaned_line_2 = re.findall('[0-9]', line)
                    self.search_results.append("".join(cleaned_line_1) + " " + "".join(cleaned_line_2))

        if len(self.search_results) != 0 and keyword != "":
            for item in self.search_results:
                widget = OneLineListItem(
                    text = item,
                    on_release=self.select_item
                )
                self.ids.list_of_guards.add_widget(widget)
        else:
            widget = Label(
                text = "No Results Found",
                )
            self.ids.list_of_guards.add_widget(widget)

        self.search_results = []
        self.ids.keyword.text = ''

    def select_item(self, obj):
        with open("officer_selected.txt", "w") as f:
            f.write("Officer: " + obj.text + "\n")
        self.back()

    def clear(self):
        with open("officer_selected.txt", "w") as f:
            f.write("")
        self.back()
        