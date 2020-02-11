import random


class Dice():
    """Initializes a dice with: \n - sides"""
    def __init__(self, sides):
        self.sides = sides

    def play(self):
        """Returns a random value with the dice maximum face limit"""
        return random.randint(1, self.sides)
