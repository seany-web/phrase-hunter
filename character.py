# Create your Character class logic in here.
class Character(str):
    def __init__(self, original, was_guessed=False):
        #test to ensure valid character
        if len(original) > 1:
            raise ValueError("Length of char cannot be more than 1")
        else:
            #set instance attributes
            self.original = original
            self.was_guessed = was_guessed

    def guess(self, player_guess):
        """This will take in a single attribute, the player's guess, and
         update the was_guessed attribute if the guessed character matches the original"""
        if player_guess.upper() == self.original.upper():
            self.was_guessed = True
            return True
        return False
    
    def show_character(self):
        """This will return the character object as a string or an underscore depending on the value 
        of the was guessed instance attribute"""
        if self.was_guessed == True or self.original == " ":
            return str(self)
        return "_"
        
