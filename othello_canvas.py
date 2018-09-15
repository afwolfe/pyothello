
import tkinter as tk 

from board import Board
from player import Player
from constants import *

class OthelloCanvas(tk.Canvas):
    def __init__(self, master, board, **kwargs):
        tk.Canvas.__init__(self, master=master, **kwargs)
        self.width = WIDTH
        self.height = HEIGHT
        self.configure(background=BG)


        self.board = board

        self.bind("<Button-1>", self.on_click)
        
        self.draw_grid()
        self.draw_discs()

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
                x = WIDTH/SIZE * j
                if disc.player is not EMPTY:
                    disc.oval = self.create_oval(x + OFFSET, y + OFFSET, x + disc_width, y + disc_height, fill=COLORS[disc.player])
                j += 1
            i += 1

    def make_move(self, move):
        if (self.board.make_move(self.board.current_player, move)):
            #print(self.board)
            self.master.status.set("{} | {}".format(
                self.board.turn_string(), self.board.score_string()))
            self.draw_discs()
        else:
            self.master.status.set("{} | Invalid move... try again.".format(
                self.board.turn_string()))
        
        if len(self.board.get_valid_moves(self.board.current_player)) is 0:
            self.master.status.set("Game Over!!! | {}".format(self.board.score_string()))
        

    def on_click(self, event):
        #print("clicked at: ({}, {})".format(event.x, event.y))
        row = int(event.y / HEIGHT * SIZE)
        col = int(event.x / WIDTH * SIZE) 
        #print("row:", row)
        #print("col:", col)
        if self.master.players[self.board.current_player].type is "Human":
            self.make_move([row, col])

    def reset(self):
        self.delete('all')
        self.draw_grid()
        self.draw_discs()
