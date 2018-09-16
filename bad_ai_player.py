#!/usr/bin/env python3

from random import randint

"""
    Name: bad_ai_player
    Desc: This module contains a "bad" AI Player class for playing Othello. It picks a random valid move.
    Author: Alex Wolfe
"""

class Player():
    """
    "Bad" AI player that chooses a random move.
    """
    def __init__(self, color):
        """
        Initialize the player
        """
        self.name = "BadBot"
        self.type = "AI"
        self.color = color
    def next_move(self, board):
        """
        Given a board, returns a random valid move
        """
        valid_moves = board.get_valid_moves(self.color)
        if len(valid_moves) > 0:
            return valid_moves[randint(0, len(valid_moves)-1)]
        else:
            return (0, 0)
