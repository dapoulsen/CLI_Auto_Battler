from game import *
from readchar import readkey, readchar

def main():
    game = Game()

    game.start_game()
    while (game.status):
        game.start_menu_decider()
        k = readkey()
        if k == "x":
            game.end_game()
            exit(0)
        


if __name__ == "__main__":
    main()