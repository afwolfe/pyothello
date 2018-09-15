#!/usr/bin/env python3
import tkinter as tk

from Constants import *
from OthelloCanvas import OthelloCanvas

class OthelloUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__()
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        #self.menu = tk.Menu(self,)

        self.game_canvas = OthelloCanvas(width=WIDTH, height=HEIGHT)
        self.game_canvas.grid()

        self.quit_button = tk.Button(self, text='Quit',
            command=self.quit)

        self.quit_button.grid()

if __name__ == "__main__":
    app = OthelloUI()
    app.master.title('Othello')
    app.mainloop()

