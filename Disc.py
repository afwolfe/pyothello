#!/usr/bin/env python3
from Constants import *
import tkinter as tk

class Disc():
    def __init__(self, player=EMPTY):
        self.player = player
        self.oval = None

    def flip(self):
        self.player = self.player * -1

    def is_played(self):
        return (self.player is not EMPTY)

    def __str__(self):
        return "Disc of player {}".format(self.player)


    def __repr__(self):
        if self.player is WHITE:
            return "W"
        elif self.player is BLACK:
            return "B"
        else:
            return "-"
