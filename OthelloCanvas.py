
import tkinter as tk 
from Board import Board
from Constants import *

from Constants import *
class OthelloCanvas(tk.Canvas):
    def __init__(self, board, **kwargs):
        tk.Canvas.__init__(self, **kwargs)
        self.width = WIDTH
        self.height = HEIGHT
        self.configure(background="#009933")

        self.board = board

        self.bind("<Button-1>", self.on_click)
        
        self.draw_grid()
        self.draw_discs()

    def mainloop(self):
        super().mainloop()

    def draw_grid(self):
        for i in range(SIZE):
            x = self.width/SIZE * i
            y = self.height/SIZE * i
            #Vertical
            self.create_line(x, 0, x, self.height)
            #Horizontal
            self.create_line(0,y, self.width, y)

    def draw_discs(self):
        disc_width = int(WIDTH/SIZE-OFFSET)
        disc_height = int(HEIGHT/SIZE-OFFSET)

        i=0
        for row in self.board.discs:
            y = HEIGHT/SIZE * i
            j=0
            for disc in row:
                x= WIDTH/SIZE * j
                if disc.player == WHITE:
                    d = self.create_oval(x + OFFSET, y + OFFSET, x + disc_width, y + disc_height, fill="#FFFFFF")
                elif disc.player == BLACK:
                    d = self.create_oval(x + OFFSET, y + OFFSET, x + disc_width, y + disc_height, fill="#000000")
                j+=1
            i+=1

    def on_click(self, event):
        print("clicked at: ({}, {})".format(event.x, event.y))
        row = int(event.y / HEIGHT * SIZE)
        col = int(event.x / WIDTH * SIZE) 
        print("row:", row)
        print("col:", col)
