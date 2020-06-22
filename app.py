# Import your Game class
from game import Game
from phrase_list import phrase_list
# Create your Dunder Main statement.
if __name__ == "__main__":
    # Inside Dunder Main:
    ## Create an instance of your Game class
    new_game = Game(phrase_list)
    ## Start your game by calling the instance method that starts the game loop
    new_game.play_game()
