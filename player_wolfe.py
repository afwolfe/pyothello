#!/usr/bin/env python3
"""
    Name: player_wolfe.py
    Desc: Mr. Wolfe's player AI, uses minimax and AB pruning
    Author: Alex Wolfe
"""
from copy import copy

class Player():
    def __init__(self, color):
        self.name = "WolfeBot"
        self.type = "AI"
        self.color = color

    def next_move(self, board):
        #Humans use the mouse to play.
        pass

    def mini_max_decision(self, board):
        successors = board.get_valid_moves(self.player)

        if board.current_player is not self.color:
            #This is the other player's turn, we want to minimize them.
            for move in range(successors):
                temp = copy(board)