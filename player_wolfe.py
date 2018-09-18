#!/usr/bin/env python3
"""
    Name: player_wolfe.py
    Desc: Mr. Wolfe's player AI, uses minimax and AB pruning
    Author: Alex Wolfe
"""
from copy import copy

from constants import *

class Player():
    def __init__(self, color):
        self.name = "WolfeBot"
        self.type = "AI"
        self.color = color

    def next_move(self, board):
        # TODO: Fix AI passing None for pos?
        move = self.mini_max_decision(board)
        print("decision:", move)
        board.make_move(move)

    def mini_max_decision(self, board):
        successors = board.get_valid_moves(board.current_player)
        self.board = board

        if board.current_player is BLACK:
            max_move = successors[0]
            max_state = copy(board)
            max_state.make_move(max_move)
            value = self.max_value(max_state)
            for move in successors:
                temp = copy(board)
                temp.make_move(move)
                if value < self.max_value(temp):
                    max_move = move
            return max_move
        else:
            min_move = successors[0]
            min_state = copy(board)
            min_state.make_move(min_move)
            value = self.min_value(min_state)
            for move in successors:
                temp = copy(board)
                if value > self.min_value(temp):
                    min_move = move
            return min_move

    def cutoff_test(self, state, depth):
        if state.terminal_test() or state.depth is depth:
            return True
        return False

    def utility(self, state):
        values = []
        for move in state.get_valid_moves(state.current_player):
            values.append(state.get_num_discs_flipped(state.current_player, move))

        try:
            if state.current_player is WHITE:
                return min(values)
            else:
                return max(values)
        except ValueError:
            return 0

    def max_value(self, state):

        if self.cutoff_test(state, self.board.depth+3):
            return self.utility(state)
        else:
            max_value = float("-inf")
            successors = state.get_valid_moves(self.color)
            for move in successors:
                temp = copy(state)
                temp.make_move(move)
                max_value = max(self.min_value(temp), max_value)
            return max_value

    def min_value(self, state):
        if self.cutoff_test(state, self.board.depth+3):
            return self.utility(state)
        else:
            min_value = float("inf")
            successors = state.get_valid_moves(self.color)
            for move in successors:
                temp = copy(state)
                temp.make_move(move)
                min_value = min(self.min_value(temp), min_value)
            return min_value

    def ab_search(self, board):
        successors = board.get_valid_moves(self.color)
        self.board = board

        if board.current_player is BLACK:
            max_move = successors[0]
            value = self.ab_max_value(max_move, float("-inf"), float("inf"))

            for move in successors:
                temp = copy(board)
                temp.make_move(move)
                if value < self.ab_max_value(temp, float("-inf"), float("inf")):
                    max_move = move
            return max_move

        else:
            min_move = successors[0]
            value = self.ab_min_value(min_move, float("-inf"), float("inf"))
            for move in successors:
                temp = copy(board)
                temp.make_move(min_move)
                if value> self.ab_min_value(temp, float("-inf", float("inf"))):
                    min_move = move

    def ab_max_value(self, state, alpha, beta):
        if self.cutoff_test(state, self.board.depth + 3):
            return self.utility(state)
        else:
            max_value = float("-inf")
            successors = state.get_valid_moves(state.current_player)
            for move in successors:
                temp = copy(state)
                temp.make_move(move)
                max_value = max(self.ab_min_value(temp, alpha, beta), max_value)
                if max_value > beta:
                    return max_value

                alpha = max(alpha, max_value)
            return max_value

    def ab_min_value(self, state, alpha, beta):
        if self.cutoff_test(state, self.board.depth + 3):
            return self.utility(state)
        else:
            min_value = float("inf")
            successors = state.get_valid_moves(state.current_player)
            for move in successors:
                temp = copy(state)
                temp.make_move(move)
                min_value = min(self.ab_max_value(temp, alpha, beta), min_value)
                if min_value < alpha:
                    return min_value

                beta = min(beta, min_value)
            return min_value
