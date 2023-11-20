"""Maze 3D, by AL Sweigart al@inventwithpython.com
Move around the maze and try to escape... in 3D!
View the code in thier book
Tags: extra-large, artistic, game, maze"""

import copy, sys, os

#Set up the constants:
WALL = '#'
EMPTY = ' '
START = 'S'
EXIT = 'E'
BLOCK = chr(9617) 
NORTH = 'NORTH'
SOUTH = 'SOUTH'
EAST = 'EAST'
WEST = 'WEST'

def wallStrToWallDict(wallStr):
    """Takes a string representationof a wall drawing 
    