from kivy.uix.screenmanager import Screen
from kivymd.uix.list import OneLineListItem
from kivy.uix.label import Label

import re

class PenaltiesListView(Screen):
    search_results = []
    # Add wherever changing screen
    def back(self):
        self.ids.list_of_penalties.clear_widgets()
        self.manager.current = "PenaltiesView"
        self.manager.transition.direction = 'right'

    # TODO: Change this out.
    def search(self, keyword):
        self.ids.list_of_penalties.clear_widgets()

        with open("penalties_list.txt", "r") as f:
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
                self.ids.list_of_penalties.add_widget(widget)
        else:
            widget = Label(
                text = "No Results Found",
                )
            self.ids.list_of_penalties.add_widget(widget)

        self.search_results = []
        self.ids.keyword.text = ''

    def select_item(self, obj):
        with open("penalties_selected.txt", "w") as f:
            f.write("Penalty: " + obj.text + "\n")
        self.back()

    def clear(self):
        with open("penalties_selected.txt", "w") as f:
            f.write("")
        self.back()
        