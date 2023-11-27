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
    ALL_OPEN or CLOSED and returns a representstion in a dictionary
    with (x, y) tuples as keys and single character strings of the 
    character to draw at that x, y location"""
    wallDict = {}
    height = 0
    width = 0
    for y, line in enumerate(wallStr.splitlines()):
        if y > height:
            height = y
    for x, character in enumerate(line):
        if x > width:
            width = x
        wallDict[(x, y)] = character
    wallDict['height'] = height + 1
    wallDict['width'] = width + 1
    return wallDict

EXIT_DICT = {(0, 0): 'E', (1, 0): 'X', (2, 0): 'I',
             (3, 0): 'T', 'height': 1, 'width': 4}

#The way we create the string to display is by converting the pictures.
#in these multiline strings to dictionaries using wallStrToWallDict().
#Then we compose the wall for the player's location and direction by
# "pasting" the wall dictionaries in CLOSED on top of the wall dictionary
# in ALL_OPEN

ALL_OPEN = wallStrToWallDict(r'''
................                             
   .........                          
____        ____                     
...|\....../|...                 
...||__...__||...                             
...||.|\./|.||...                             
...||.|.X.|.||...                             
...||.|/.\.|.||...                             
                             
                             
                           '''.strip() )