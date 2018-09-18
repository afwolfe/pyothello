#!/usr/bin/env python3
"""
    Name: board.py
    Desc: This module contains a Board class for Othello.
    Author: Alex Wolfe
"""

from constants import *
from disc import Disc


class Board:
    """
    Board class that implements Othello game logic.
    """

    def __init__(self):
        """
        Initializes the board by setting all of the initial values.
        """
        self.discs = [[Disc(EMPTY) for x in range(SIZE)] for y in range(SIZE)]

        self.discs[3][3].owner = WHITE
        self.discs[4][4].owner = WHITE

        self.discs[3][4].owner = BLACK
        self.discs[4][3].owner = BLACK

        self.scores = {WHITE: 2, BLACK: 2}
        self.depth = 0
        self.current_player = WHITE

        # _flips is a dict that caches move calculations.
        # get_discs_flipped and get_num_discs_flipped should be used instead of direct access.
        self._flips = {}

        # move_history holds each move as a 2D array [ [depth, player, pos], ...]
        # where pos is a tuple of (row, col)
        self.move_history = []

    def reset(self):
        """
        Resets the board by calling __init__ again.
        
        :return: None
        """
        self.__init__()

    def _update_scores(self):
        """
        Updates self.scores for each player using self.move_history to calculate the change in points.
        Should only be called by make_move

        :return: dict self.scores {WHITE: score, BLACK: score} after updating
        """
        change = len(self._flips[str(self.move_history[-1])])
        player = self.move_history[-1][1]
        self.scores[player] += change + 1
        self.scores[player * -1] -= change

        return self.scores

    def get_discs_flipped(self, player, pos):
        """
        Given the player and the move position, returns an array of discs that would be flipped at this position.
        Answers are cached in dict self._flips under key str([self.depth, player, pos]),
        where depth is the depth AFTER the move

        :param player: The player color from constants.
        :param pos: The position to play from.
        :return: array of possible moves [(row, col), ...]
        """

        discs_flipped = []
        temp_flip = []
        if str([self.depth + 1, player, pos]) in self._flips:
            # If we've already calculated the flips, return them.
            return self._flips[str([self.depth + 1, player, pos])]
        else:
            # We need to calculate them from scratch.
            for d in DIRECTIONS:
                # print("DIRECTION: ", d)
                # print("POS: ", pos)
                x = pos[0]
                y = pos[1]
                while 0 <= x < len(self.discs) and 0 <= y < len(self.discs[x]):
                    x += d[0]
                    y += d[1]
                    # print('[{}][{}]'.format(x, y))
                    try:
                        if self.discs[x][y].owner is self.current_player * -1 and x is not -1 and y is not -1:
                            # If the disc belongs to the other player and we didn't go backwards.
                            # print("Found a flip!")
                            # discs_flipped += 1
                            temp_flip.append([x, y])
                        else:
                            # print("End of this direction!")
                            if self.discs[x][y].owner is self.current_player:
                                # print("End is a matching disc.")
                                discs_flipped = discs_flipped + temp_flip
                            temp_flip = []
                            break
                    except IndexError:
                        # We reached the edge of the board.
                        break

            # Caches list of discs flipped in a dict with str([self.depth, player, pos]) as key
            self._flips[str([self.depth + 1, player, pos])] = discs_flipped

            return discs_flipped

    def get_num_discs_flipped(self, player, pos):
        """
        Given the player and the move position, returns how many discs would be flipped at this position.

        :param player: The player color from constants.
        :param pos: The position to play from.
        :return: int number of discs that would be flipped by a player at pos.
        """
        return len(self.get_discs_flipped(player, pos))

    def get_valid_moves(self, player):
        """
        Given the current player, returns an array of valid moves.

        :param player: A player as specified in constants.
        :return: an array of valid moves of the form [(row, col), ...]
        """
        valid_moves = []
        for r in range(SIZE):
            for c in range(SIZE):
                pos = (r, c)
                if self.is_legal_move(pos, player):
                    valid_moves.append(pos)
        return valid_moves

    def is_legal_move(self, pos, player=None):
        """
        Given the current player and position, returns whether or not the current move is legal.
        :param player: The player color from constants.
        :param pos: The position to play from.
        :return: boolean of whether or not the current player can move here.
        """
        if not player:
            player = self.current_player

        return self.discs[pos[0]][pos[1]].owner is EMPTY and self.get_num_discs_flipped(player, pos) > 0

    def make_move(self, pos, player=None):
        """
        Given a player and position (row, col), attempts to move and returns True.
        If it is not a valid move, returns False.

        :param player: The player color from constants.
        :param pos: The position to play from as tuple (row, col)
        :return: Boolean of whether or not the move succeeded
        """
        if not player:
            print("player not specified")
            player = self.current_player

        if not pos:
            raise Exception("pos not specified")

        if self.is_legal_move(pos, player):
            self.depth += 1
            self.discs[pos[0]][pos[1]].owner = player
            self.move_history.append([self.depth, player, pos])

            for d in self.get_discs_flipped(player, pos):
                x = d[0]
                y = d[1]
                self.discs[x][y].flip()

            # Success!
            self.current_player = self.current_player * -1
            if len(self.get_valid_moves(self.current_player)) is 0:
                self.current_player = self.current_player * -1
            self._update_scores()
            return True
        else:
            # Illegal move was attempted
            return False


    def terminal_test(self):
        return len(self.get_valid_moves(self.current_player)) == 0

    def board_string(self):
        """
        :return: A string showing B and W discs on the board.
        """
        board = ""
        for row in self.discs:
            board += "{}\n".format(row)

        return board

    def turn_string(self):
        """
        :return: A string stating whose turn it is.
        """
        if self.current_player == WHITE:
            p_string = "WHITE"
        else:
            p_string = "BLACK"
        return "It is {}'s turn".format(p_string)

    def score_string(self):
        """
        :return: A string comparing the current scores.
        """
        return "WHITE: {} | BLACK: {}".format(self.scores[WHITE], self.scores[BLACK])

    def __str__(self):
        """
        :return: Full string representation of the board including current player and score.
        """
        out_str = "Board with depth {}:\n".format(self.depth)
        out_str += self.board_string()
        out_str += self.score_string()
        out_str += self.turn_string()
        return out_str
