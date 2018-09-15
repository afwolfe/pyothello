#!/usr/bin/env python3
import importlib
import sys
import tkinter as tk


from constants import *
from othello_canvas import OthelloCanvas
from board import Board
from player import Player

class OthelloUI(tk.Frame):
    """
    Main UI class for Othello. Contains all Tkinter elements and handles the triggering of the AI players
    """
    def __init__(self, argv, master=None):
        """
        Initializes the OthelloUI, imports specified Player files from the command line
        """
        super().__init__(master)
        self.width=WIDTH
        self.height=HEIGHT
        self.grid()
        self.players = {}
        try:
            p1 = importlib.import_module(argv[1])
            self.players[WHITE] = p1.Player(WHITE)
        except ImportError:
            print('error importing {}, using human_player.'.format(argv[1]))
            self.players[WHITE] = Player(WHITE)

        try:
            p2 = importlib.import_module(argv[2])
            self.players[BLACK] = p2.Player(BLACK)
        except ImportError:
            print('error importing {}, using human_player.'.format(argv[1]))
            self.players[BLACK] = Player(BLACK)

        self.board = Board()

        self.create_widgets()

    def create_widgets(self):
        """
        Creates the widgets for the main UI frame
        """

        self.game_canvas = OthelloCanvas(self, self.board, width=WIDTH, height=HEIGHT)
        self.game_canvas.grid(row=0, column=0)

        self.side_bar = tk.LabelFrame(self, text="Controls:")
        self.side_bar.grid(row=0, column=1)

        self.reset_button = tk.Button(self.side_bar, text="Reset",
            command=self.reset_ui)

        #self.reset_button.grid(row=0, column=1)
        self.reset_button.pack()

        self.quit_button = tk.Button(self.side_bar, text='Quit',
            command=self.quit)
        #self.quit_button.grid(row=0, column=1)
        self.quit_button.pack()

        self.status = tk.StringVar()
        self.status_bar = tk.Label(self, bd=1, relief=tk.SUNKEN, anchor=tk.W,
                              textvariable=self.status,
                              font=('arial', 16, 'normal'))
        self.status.set('Status Bar')
        self.status_bar.grid(row=2)

    def reset_ui(self):
        """
        Resets the game board and clears the Canvas.
        """
        self.board.reset()
        self.game_canvas.reset()

    def turn_loop(self):
        """
        If the player isn't human, asks them to give their next move.
        """
        current = self.board.current_player
        if self.players[current].type is "Human":
            pass
        else:
            next_move = self.players[current].next_move(self.board)
            self.game_canvas.make_move(next_move)
        self.after(DELAY, self.turn_loop)



if __name__ == "__main__":
    app = OthelloUI(sys.argv)
    app.master.title('Othello')
    app.after(DELAY, app.turn_loop)
    app.mainloop()

