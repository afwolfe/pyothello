import tkinter as tk

from board import Board
from player import Player
from constants import *


class OthelloCanvas(tk.Canvas):
    """
    Subclass of tkinter.Canvas with Othello specific methods.
    """

    def __init__(self, master, board, **kwargs):
        """
        Initializes the OthelloCanvas.
        :param master: Specifies the master tkinter element.
        :param board: The othello Board object to represent
        :param kwargs: any other kwargs that tkinter takes.
        """
        tk.Canvas.__init__(self, master=master, **kwargs)
        self.width = WIDTH
        self.height = HEIGHT
        self.configure(background=BG)

        self.board = board

        self.bind("<Button-1>", self.on_click)

        self.draw_grid()
        self.draw_discs()

    def draw_grid(self):
        """
        Draws the Othello grid of SIZE on the canvas (self).
        :return: None
        """
        for i in range(SIZE):
            x = self.width / SIZE * i
            y = self.height / SIZE * i
            # Vertical
            self.create_line(x, 0, x, self.height)
            # Horizontal
            self.create_line(0, y, self.width, y)

    def draw_discs(self):
        """
        Draws the discs on the Canvas if they exist on the board.
        :return: None
        """
        disc_width = int(WIDTH / SIZE - OFFSET)
        disc_height = int(HEIGHT / SIZE - OFFSET)

        i = 0
        for row in self.board.discs:
            y = HEIGHT / SIZE * i
            j = 0
            for disc in row:
                x = WIDTH / SIZE * j
                if disc.oval_id:
                    # If the disc was already drawn, just recolor it.
                    self.itemconfig(disc.oval_id, fill=COLORS[disc.owner])
                elif disc.owner is not EMPTY:
                    # elif the disc didn't already have an ID, we need to create it and save the ID.
                    disc.oval_id = self.create_oval(x + OFFSET, y + OFFSET, x + disc_width, y + disc_height,
                                                    fill=COLORS[disc.owner])
                j += 1
            i += 1

    def make_move(self, move):
        """
        Sends the specified move to the Board object and updates the UI accordingly
        :param move: (row, col) sends the specified move to the board.
        :return: None
        """
        #print(move)
        if self.board.make_move(move, self.board.current_player):
            # print(self.board)
            self.master.status.set("{} | {}".format(
                self.board.turn_string(), self.board.score_string()))
            self.draw_discs()
        else:
            self.master.status.set("{} | Invalid move... try again.".format(
                self.board.turn_string()))

        if self.board.terminal_test():
            self.master.status.set("Game Over!!! | {}".format(self.board.score_string()))

    def on_click(self, event):
        """
        On click, if the current player is human makes a move.
        :param event: the click event
        :return: None
        """
        if self.master.players[self.board.current_player].type is "Human":
            row = int(event.y / HEIGHT * SIZE)
            col = int(event.x / WIDTH * SIZE)
            self.make_move([row, col])
            # print("clicked at: ({}, {})".format(event.x, event.y))
            # print("row:", row)
            # print("col:", col)

    def reset(self):
        """
        Resets the UI by deleting all elements and redrawing the board.
        :return: None
        """
        self.delete('all')
        self.draw_grid()
        self.draw_discs()
