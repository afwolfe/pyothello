#!/usr/bin/env python3
from constants import *


class Disc:
    """
    Basic Disc class for Othello.
    Stores the player color and a tkinter canvas item ID as specified in constants.
    """
    def __init__(self, player=EMPTY):
        """
        Initializes the Disc instance.

        :param player: The player color, must be WHITE or BLACK from constants.
        """
        self.owner = player
        self.oval_id = None

    def flip(self):
        """
        Flips the oval by setting the player to the opposite.
        :return:
        """
        self.owner = self.owner * -1

    def is_played(self):
        """
        Determines if the disc has been played yet.
        :return: True if the disc belongs to a player.
        """
        return (self.owner is not EMPTY)

    def __str__(self):
        """

        :return: Human readable string about the oval.
        """
        return "Disc of player: {}, oval_id: {}".format(self.owner, self.oval_id)

    def __repr__(self):
        """

        :return: the player of the disc in one char form.
        """
        if self.owner is WHITE:
            return "W"
        elif self.owner is BLACK:
            return "B"
        else:
            return "-"
