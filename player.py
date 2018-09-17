#!/usr/bin/env python3

class Player():
    def __init__(self, color):
        self.name = "Player"
        self.type = "Human"
        self.color = color

    def next_move(self, board):
        #Humans use the mouse to play.
        pass