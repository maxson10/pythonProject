"""
from pygamelib import engine
from pygamelib.assets import graphics
from pygamelib import board_items
from pygamelib.gfx import core
from pygamelib import constants




DZ_board = engine.Board(ui_borders=graphics.WHITE_SQUARE, ui_board_void_cell=graphics.WHITE_SQUARE)


DZ_board.ui_border_left = "a"
DZ_board.ui_border_right = "o"
DZ_board.ui_border_top = "_"
DZ_board.ui_border_bottom = "-"


DZ_board.place_item( board_items.Wall(model=graphics.BLACK_SQUARE), 0, 0)
DZ_board.place_item( board_items.Door(model=graphics.RED_SQUARE), 9,9)
DZ_board.place_item( board_items.Camera(model=graphics.BLACK_SQUARE), 9, 0)
player = DZ_board.item(3,0)
player.sprixel = core.Sprixel("@-", bg_color=core.Color(0,0,0), is_bg_transparent=False)
DZ_board.move(player,constants.RIGHT)


DZ_board.display()

"""
# Дз к 5 уроку
class Yhenik:
    def __init__(self):

        self.name = 'Petya'
        self.clas = '9'


# Методы класса
    def priv(self):
        print('Привет петя с 9 класса')



b = Yhenik
print(b)
b.priv(1)
#------------------------------------------------------------------------
class animal:
    def __init__(self):

        self.name = 'kvadrober'
        self.sound = 'gav'


# Методы класса
    def golos(self):
        print('gav gav gav')



v = animal
print(b)
v.golos(1)

class Book:
    def __init__(self):

        self.name = 'nazv'
        self.avtor = 'kvadrober'


# Методы класса
    def vinfo(self):
        print('a b c d e f g')



o = Book
print(b)
o.vinfo(1)

class bloxfruit:
    def __init__(self):

        self.name = 'orange'
        self.color = 'orange'


# Методы класса
    def finfo(self):
        print('fkysno')


