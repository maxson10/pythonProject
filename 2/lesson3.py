#Дз урок 2
#r = 6
#pi = 3.14156
#area = pi * r
#print(area)
#
#def culculate_circkle;
#
#
#    pi = 3.14156
#    area = pi * r ** 2
#
#a = culculate_circkle(2)
#print (int(a))
#N3
#
#def get_number(stroka,symbol):
#    a = 0
#    for i in stroka:
#      a =+ 1
# #       print(a)
#
#get_number(stroka"hello",simb"l")

import pygamelib

from pygamelib import engine
from pygamelib.assets.graphics import MAGENTA_SQUARE, BLUE_SQUARE

my_board = engine.Board()


my_board.ui_border_left = "a"
my_board.ui_border_right = "o"
my_board.ui_border_top = "_"
my_board.ui_border_bottom = "_"
my_board.display()


from pygamelib import engine
from pygamelib.assets import graphics
from pygamelib import board_items
from pygamelib.gfx import core
from pygamelib import constants


new_board = engine.Board(ui_borders=graphics.RED_SQUARE, ui_board_void_cell=graphics.WHITE_SQUARE)
new_board.place_item( board_items.Wall(model=graphics.BLUE_SQUARE), 0, 0)
new_board.place_item( board_items.Door(model=graphics.BLUE_SQUARE), 9, 9)
new_board.place_item( board_items.NPC(model=graphics.BLUE_SQUARE), 0, 9)
new_board.place_item( board_items.Player(model=graphics.BLUE_SQUARE), 9, 0)
player = new_board.item(4,2)
player.sprixel = core.Sprixel("--", bg_color=core.Color(0,0,0), is_bg_transparent=False)
new_board.place_item(board_items.Door(sprixel=core.Sprixel("||",bg_color=core.Color(255,0,0))),2,3)
#new_board.move(player,constants.RIGHT)
new_board.display()