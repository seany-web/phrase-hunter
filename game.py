import re
import random

from character import Character
from phrase import Phrase

# Create your Game class logic in here.
class Game:
    def __init__(self, phrases):
        self.phrases = [Phrase(phrase) for phrase in phrases]
        self.current_phrase = random.choice(self.phrases)
        self.lives = 5
        self.game_active = False

    def game_state(self, action):
        """This will either start or end the game by changing the game_active instance attribute"""
        if action == "start":
            self.game_active = True
        elif action == "stop":
            self.game_active = False

    def get_player_input(self):
        """This will prompt the player to enter a guess and validate the input"""
        waiting_for_input = True
        while(waiting_for_input):
            answer = input("Please enter your guess: ")
            if not re.search(r'[a-z]', answer):
                print("{} is not a valid guess. Please try again.".format(answer))
            elif len(answer) > 1:
                print("{} is too long. You may only enter a single character per guess.".format(answer)
            )
            else:
                waiting_for_input = False
        return answer

    def determine_win_loss(self):
        """This will check if the player has won or lost the game"""
        if self.lives == 0:
            self.game_state("stop")
            print("You have run out of guesses.")
        elif self.current_phrase.solved:
            self.game_state("stop")
            print("Congratulations. You have successfully guessed the phrase.")

    def play_game(self):
        """This controls the flow of the game and prints messages to the player"""
        self.game_active = True
        # start game loop
        while(self.game_active):
            # print phrase in current state
            print(self.current_phrase.show_phrase())
            # prompt user to enter a guess
            player_guess = self.get_player_input()
            # if guess does not match phrase
            if player_guess not in self.current_phrase.phrase:
                # player loses a life
                self.lives -= 1
                print("You have {} out of 5 lives remaining.".format(self.lives))
                # check win/loss state
                self.determine_win_loss()
            # otherwise
            else:
                for letter in self.current_phrase.characters:
                    letter.guess(player_guess)
                #check if solved
                self.current_phrase.check_solved()
                # check win/loss state
                self.determine_win_loss()
            # otherwise continue game loop

            #prompt player to play again
