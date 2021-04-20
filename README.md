# pyothello

A simple Python Othello implementation with a Tkinter GUI.

## Overview

This is a Python rewrite of an Othello game I made in undergrad implementing basic mini-max and alpha-beta pruning algorithms for an AI player.

The project can be used as a starting point for other AIs and can even have two different AI files battle each other as long as they meet the specifications below.

## Requirements

* Tkinter

## Usage

### Human vs. Human
Run `python main.py` to run the Othello game with in Human vs. Human mode.

### Playing against an AI file
Run `python player ai_module1` to play against an AI file (do not include the `.py` file extension.)
The first player is always `WHITE` and the second player is always `BLACK`.

### Pitting 2 AIs against each other
Run `python ai_module1 ai_module2`

If the program is unable to import one of the AIs for some reason, it will default to a Human player for that spot

## AI Player Structure

The `bad_ai_player.py` file shows an example of a poorly written AI that uses the `board.get_valid_moves()` function to get a list of valid moves and randomly chooses one.

To write your own AI, you should make a new file with a class that follows the structure in `ai_player.py`
In the `__init__()` function, you should specify the "name" of your AI player, and the "type" should be "AI."
The `next_move()` function will be given the current Board object and your player should return the next move as [row, col].