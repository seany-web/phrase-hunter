import re

from character import Character

# Create your Phrase class logic here.
class Phrase:
    """Instatiates a new phrase object and turns the phase into a list of Character objects.
    Also sets the WAS_GUESSED attribute on any non-alpha characters to True.
    This is so the player doesn't have to guess symbols as part of the phrase"""
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
        """Checks all character objects in the phrase to see if they have been guessed correctly and
        sets the solved instance attribute if all accordingly""" 
        characters_guessed_correctly = []
        for letter in self.characters:
            characters_guessed_correctly.append(letter.was_guessed)
        if all(characters_guessed_correctly):
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
