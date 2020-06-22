import re

from character import Character

# Create your Phrase class logic here.
class Phrase:
    def __init__(self, phrase, solved=False):
        self.solved = solved
        self.phrase = phrase        
        self.characters = []
        for letter in phrase:
            self.characters.append(Character(letter))

        for character in self.characters:
            if not re.match(r'[a-z]', character, re.IGNORECASE):
                character.was_guessed = True


    def check_solved(self):
        """checks all character objects in the phrase to see if they have been guessed correctly and sets the solved instance attribute accordingly""" 
        # for letter in self.characters:
        #     if letter.was_guessed:
        #         self.solved = True
        #     else:
        #         self.solved = False
        # return self.solved
        my_list = []
        for letter in self.characters:
            my_list.append(letter.was_guessed)
        if all(my_list):
            self.solved = True
        else:
            self.solved = False
        return self.solved


    def show_phrase(self):
        """displays all characters in active phrase"""
        formatted_phrase = ""
        for letter in self.characters:
            formatted_phrase += letter.show_character() + " "
        return formatted_phrase
