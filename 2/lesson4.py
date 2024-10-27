#Примеры

"""from pygamelib import engine, board_items, constants
from pygamelib.gfx import core
from pygamelib.assets import graphics


def update_game(game: engine.Game, key, elapsed_time):
    # The update function is called every frame and always receive 3 arguments:
    # game: the game object
    # key: the key pressed by the user (if any) or None
    # delta_time: the time passed since the last frame (in seconds)

    # First, we add the elapsed time to the timer.
    game.tutorial_01_timer += elapsed_time

    # Then we check if the timer is greater than 2 seconds.
    if game.tutorial_01_timer > 2:
        # If so, we reset the timer and change the level.
        game.tutorial_01_timer = 0
        # We increase the number of time we changed level.
        game.tutorial_01_counter += 1
        # We change the level.
        if game.current_level == 1:
            game.change_level(2)
        else:
            game.change_level(1)

        # We don't forget to place the current board and its name in the top left corner
        # of the screen.
        game.screen.place(mygame.current_board().name, 0, 0)
        game.screen.place(mygame.current_board(), 1, 0)

        # Now we check if we have changed level 10 times.
        if game.tutorial_01_counter == 10:
            # If so, we stop the game.
            game.stop()

        # And finally we update the screen.
        game.screen.update()


if __name__ == "__main__":

    # Create a new game instance.
    # The game has a name (here it is "Demo game"), it is up to you to use or not that
    # name.
    # We set the game to run in real time (default is to run turn by turn). MODE_RT is
    # for real time, MODE_TBT is for turn based.
    # We also give the game engine a reference to the update_game function. This
    # function for every frame.
    # Please refer to the documentation for more information about the Game class:
    # https://pygamelib.readthedocs.io/en/latest/pygamelib.engine.Game.html
    mygame = engine.Game(
        name="Demo game", user_update=update_game, mode=constants.MODE_RT
    )
    # Then we create 2 basic boards. Please have a look at the wiki for a complete
    # tutorial on Boards:
    # https://github.com/pygamelib/pygamelib/wiki/Getting-started-Board
    # And the documentation for the Board class:
    # https://pygamelib.readthedocs.io/en/latest/pygamelib.engine.Board.html
    board1 = engine.Board(
        name="Level 1",
        ui_board_void_cell=graphics.BLUE_SQUARE,  # blue background
        player_starting_position=[0, 0],  # The player starts at the top left corner
    )
    board2 = engine.Board(
        name="Level 2",
        ui_board_void_cell=graphics.MAGENTA_SQUARE,  # black background
        player_starting_position=[4, 4],  # The player starts at position [4, 4]
    )

    # Then we create a player that will be represented by a Unicorn emoji.
    # We explicitly set the background to be transparent, so the player will take the
    # background color of the board.
    # For more information on board items, please refer to the documentation:
    # https://pygamelib.readthedocs.io/en/latest/board_items.html
    mygame.player = board_items.Player(
        name="DaPlay3r",
        sprixel=core.Sprixel(graphics.Models.UNICORN, is_bg_transparent=True),
    )

    # We add the boards to the game.
    mygame.add_board(1, board1)
    mygame.add_board(2, board2)

    # We change the level to the first one.
    mygame.change_level(1)
    # We place the current board and its name in the top left corner of the screen.
    mygame.screen.place(mygame.current_board().name, 0, 0)
    mygame.screen.place(mygame.current_board(), 1, 0)

    # Now we add 2 variables to the game object to keep track of the amount of times
    # we changed level and to have a timer.
    mygame.tutorial_01_counter = 0
    mygame.tutorial_01_timer = 0

    # And we start the game. Everything will now be handled by the user_update function.
    mygame.run()
"""
"""a = input("Ввод")
print(a)

def get_test_data():
    a = input("Ввод")
    print(a)

get_test_data
"""
"""class Bicicle:
    def __init__(self):
        color = 'red'
        type = "gorn"
        speed = "20"
        price ="???"


    def stop(self):
        print("стою")

    def ride(self):
        print("еду")

b = Bicicle()
print(b)

b.ride(1)

b.stop(1)
"""

class Cat:
    def __init__(self):
        self.color = 'white'
        self.brits = "nan"
        self.age = "4"

    def sleep(self):
        print("спит")

    def eat(self):
        print("ест")
    def getinfo(self):
        print('Цвет Белый', "породы нет", "возраст 4")
c = Cat

c.sleep

c.eat

#cat1 = Cat(color="black" , age = 3, brits = "good")
#cat2 = Cat(color="grown", age=4, brits="very good")

#print(cat1.age)
#print(cat1.color)
#print(cat1.brits)

