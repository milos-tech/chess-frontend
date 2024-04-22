from tkinter import *

import customtkinter as ctk
from CTkTable import *

from viewmodels.exams import *

class Home(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.refresh_button = ctk.CTkButton(self, text="Refresh", command=self.update_table)
        self.refresh_button.grid(row=0, column=0, sticky="e")

        self.update_table()

    def update_table(self):
        self.refresh_button.configure(state=DISABLED)
        data = get_all_games(return_objects=True)

        values = [
            ["results"] # table headers
        ]

        for game in data:
            try:
                value = [
                    game.results
                ]
                values.append(value)
            except Exception as e:
                raise e
            
        table = CTkTable(master=self, values=values)
        table.grid(row=1, column=0, pady=(20, 20), sticky="nsew")
        self.refresh_button.configure(state=NORMAL)