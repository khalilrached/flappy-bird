from lib import *

game = Game(720, 1280)

if __name__ == "__main__":
    while True:
        game.draw()
        if game.isOver():
            game.restart()
