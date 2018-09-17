SIZE = 8

# White and black must be opposites -1 and 1, the game makes some assumptions based on this.
WHITE = -1
BLACK = 1
EMPTY = 0
DELAY = 1000

# Each direction you can look for flips on an Othello board.
DIRECTIONS = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 1),
    (1, 0)]
    

# Customize the UI
COLORS = {
    WHITE: "#EEEEEE",
    BLACK: "#111111"
}
BG = "#009030"
WIDTH = 500
HEIGHT = 500
OFFSET = 5
