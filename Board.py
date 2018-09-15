#!/usr/bin/env python3
"""
    Name: board.py
    Desc: This module contains a Board class for Othello.
    Author: Alex Wolfe
"""

from constants import *
from disc import Disc

class Board():
    """
    Board class that implements Othello game logic.
    """
    def __init__(self):
        self.discs = [[Disc(EMPTY) for x in range(SIZE)] for y in range(SIZE)]

        self.discs[3][3].player = WHITE
        self.discs[4][4].player = WHITE

        self.discs[3][4].player = BLACK
        self.discs[4][3].player = BLACK

        self.scores = {WHITE: 2, BLACK: 2}
        self.depth = 0
        self.current_player = WHITE
        self.flips = {}
        self.move_history = []


    def reset(self):
        """
        Resets the board by calling init again.
        """
        self.__init__()

    def update_scores(self):
        """
        Updates self.scores for each player using self.move_history to calculate the change in points.
        """
        change = len(self.flips[str(self.move_history[-1])])
        player = self.move_history[-1][1]
        self.scores[player] += change + 1
        self.scores[player * -1] -= change

    def get_num_discs_flipped(self, player, pos):
        """
        Given the player and the move position, returns how many discs would be flipped at this position.
        Answers are cached in dict self.flips under key str([self.depth, player, pos]), where depth is the depth AFTER the move
        """
        discs_flipped = []
        temp_flip = []
        for d in DIRECTIONS:
            #print("DIRECTION: ", d)
            #print("POS: ", pos)
            x = pos[0]
            y = pos[1]
            while 0 <= x < len(self.discs) and 0 <= y < len(self.discs[x]):
                x += d[0]
                y += d[1]
                #print('[{}][{}]'.format(x, y))
                try:
                    if self.discs[x][y].player is self.current_player * -1:
                        #print("Found a flip!")
                        #discs_flipped += 1
                        temp_flip.append([x, y])
                    else:
                        #print("End of this direction!")
                        if self.discs[x][y].player is self.current_player:
                            #print("End is a matching disc.")
                            discs_flipped = discs_flipped + temp_flip
                        temp_flip = []
                        break
                except IndexError:
                    #We reached the edge of the board.
                    break
        
        #Caches list of discs flipped in a dict with str([self.depth, player, pos]) as key
        self.flips[str([self.depth+1, player, pos])] = discs_flipped
        return len(discs_flipped)

    def get_valid_moves(self, player):
        """
        Given the current player, returns an array of valid moves in the form [[row, col], ...]
        """
        valid_moves = []
        for r in range(SIZE):
            for c in range(SIZE):
                pos = [r, c]
                if self.is_legal_move(player, pos):
                    valid_moves.append(pos)
        return valid_moves

    def is_legal_move(self, player, pos):
        """
        Given the current player and position, returns whether or not the current move is legal.
        """
        return (self.discs[pos[0]][pos[1]].player is EMPTY and self.get_num_discs_flipped(player, pos) > 0)

    def make_move(self, player, pos):
        """
        Given a player and position [row, col], attempts to move and returns True.
        If it is not a valid move, returns False.
        """
        if self.is_legal_move(player, pos):
            self.depth += 1
            self.discs[pos[0]][pos[1]].player = player
            self.move_history.append([self.depth, player, pos])

            for d in self.flips[str(self.move_history[-1])]:
                x = d[0]
                y = d[1]
                self.discs[x][y].flip()
            
            #Success!
            self.current_player = self.current_player * -1
            # if len(self.get_valid_moves(self.current_player)) is 0:
            #     self.current_player = self.current_player * -1
            self.update_scores()
            return True
        else:
            #Illegal move was attempted
            return False
    def turn_string(self):
        """
        Returns a string saying whose turn it is.
        """
        if self.current_player == WHITE:
            p_string = "WHITE"
        else:
            p_string = "BLACK"
        return "It is {}'s turn".format(p_string)

    def score_string(self):
        """
        Returns a string comparing the current scores.
        """
        return "WHITE: {} | BLACK: {}".format(self.scores[WHITE], self.scores[BLACK])

    def __str__(self):
        """
        String representation of the board.
        """
        out_str = "Board with depth {}:\n".format(self.depth)
        for row in self.discs:
            out_str += "{}\n".format(row)

        out_str += self.score_string()
        out_str += self.turn_string()
        return out_str
