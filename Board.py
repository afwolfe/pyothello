#!/usr/bin/env python3
from Constants import *
from Disc import Disc
class Board():
    """
    Board class that implements Othello game logic.
    """
    def __init__(self):
        self.discs = []
        self.reset_discs()

        self.depth = 0
        self.current_player = WHITE
        self.flips = {}

    def reset_discs(self):
        self.discs = [[Disc(EMPTY) for x in range(SIZE)] for y in range(SIZE)]

        self.discs[3][3].player = WHITE
        self.discs[4][4].player = WHITE

        self.discs[3][4].player = BLACK
        self.discs[4][3].player = BLACK

    def get_num_discs_flipped(self, player, pos):

        #Memoized disc flipping? {depth, player, pos} as key?
        discs_flipped = []
        for direction in DIRECTIONS:
            #print("DIRECTION: ", direction)
            x = pos[0]
            y = pos[1]
            while 0 <= x < len(self.discs)-1 and 0 <= y < len(self.discs[x])-1:
                #print('[{}][{}]'.format(x,y))
                x += direction[0]
                y += direction[1]
                if self.discs[x][y].player is self.current_player * -1:
                    #discs_flipped += 1
                    discs_flipped.append([x, y])
                else:
                    #print("End of discs, new direction!")
                    break
        key = "{}.{}.{}".format(self.depth, player, pos)
        self.flips[key] = discs_flipped

        return len(discs_flipped)

    def is_legal_move(self, player, pos):
        return (self.discs[pos[0]][pos[1]].player is EMPTY and self.get_num_discs_flipped(player, pos) > 0)

    def make_move(self, player, pos):
        if self.is_legal_move(player, pos):
            self.discs[pos[0]][pos[1]].player = player

            key = "{}.{}.{}".format(self.depth, player, pos)
            for d in self.flips[key]:
                x = d[0]
                y = d[1]
                self.discs[x][y].flip()

            # for direction in DIRECTIONS:
            #     #print("DIRECTION: ", direction)
            #     x = pos[0]
            #     y = pos[1]
            #     while 0 <= x < len(self.discs)-1 and 0 <= y < len(self.discs[x])-1:
            #         #print('[{}][{}]'.format(x,y))
            #         x+= direction[0]
            #         y+= direction[1]
            #         if self.discs[x][y].player is self.current_player * -1:
            #             self.discs[x][y].flip()
            #         else:
            #             #print("End of discs, new direction!")
            #             break
            
            #Success!
            self.depth += 1
            return True
        else:
            #Illegal move was attempted
            return False

    def __str__(self):
        out_str = "Board with depth {}:\n".format(self.depth)
        for row in self.discs:
            out_str += "{}\n".format(row)
        out_str += "It is {}'s turn".format(self.current_player)
        return out_str


