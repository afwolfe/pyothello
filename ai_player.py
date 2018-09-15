#!/usr/bin/env python3

"""
    Name: ai_player
    Desc: This module contains an AI Player class for playing Othello.
    Author:
"""

class Player():
    """
    Starter Player for ai_player module.
    The game expects you to tell it your next move in the form [row, col] when next_move is called.
    """
    def __init__(self, color):
        """
        Names the Player, the type, and which color (WHITE or BLACK as defined in constants.py)
        """
        self.name = ""
        self.type = "AI"
        self.color = color
    def next_move(self, board):
        """
        Starter for next_move.
        Given the current board, return the best next move.
        """
        #do something with board
        #return the [row, col] you want to move in.
        return [0, 0]
