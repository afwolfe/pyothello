#!/usr/bin/env python3
import importlib
import sys
import tkinter as tk


from constants import *
from othello_canvas import OthelloCanvas
from board import Board

class OthelloUI(tk.Frame):
    """
    Main UI class for Othello. Contains all Tkinter elements and handles the triggering of the AI players
    """
    def __init__(self, master=None):
        """
        Initializes the OthelloUI, imports specified Player files from the command line.

        :param master: Optionally provides a master object for the tk.Frame
        """
        super().__init__(master)
        self.width=WIDTH
        self.height=HEIGHT
        self.grid()
        self.players = {}
        try:
            p1 = importlib.import_module(sys.argv[1])
        except (ImportError, IndexError) as e:
            print('error importing or nothing specified for WHITE, using human_player.')
            p1 = importlib.import_module('player')
        finally:
            self.players[WHITE] = p1.Player(WHITE)

        try:
            p2 = importlib.import_module(sys.argv[2])
        except (ImportError, IndexError) as e:
            print('error importing or nothing specified for BLACK, using human_player.')
            p2 = importlib.import_module('player')
        finally:
            self.players[BLACK] = p2.Player(BLACK)

        self.board = Board()

        self.create_widgets()

    def create_widgets(self):
        """
        Creates the widgets for the main UI frame

        :return: returns nothing
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
        :return: nothing
        """

        self.board.reset()
        self.game_canvas.reset()

    def turn_loop(self):
        """
        If the player isn't human, asks them to give their next move.

        :return: nothing
        """

        current = self.board.current_player
        if self.players[current].type is "Human":
            pass
        else:
            next_move = self.players[current].next_move(self.board)
            self.game_canvas.make_move(next_move)
        self.after(DELAY, self.turn_loop)



if __name__ == "__main__":
    #Initialize the UI
    app = OthelloUI()
    app.master.title('Othello')

    #Sets up the turn loop.
    app.after(DELAY, app.turn_loop)
    app.mainloop()

