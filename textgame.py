# Lets build a game
# ------------------------------------

import random

# GAME STATE


# CHARACTER CLASS
class Character:

    # define the constructor / function that makes a character
    # arg of self and the name
    def __ini__(self, name):
        # define your name
        self.name = name
        # random str between 4-8
        self.strength = random.randint(4, 8)
        # random def between 1-4
        self.defense = random.randint(1, 4)
        # random acc between 1-10
        self.accuracy = random.randint(1, 10)

    # define attack. Arg of self and other
    def attack(self, other):


# FUNCTIONS


# GAME LOOP

# infinite loop - running forever
while(true):
    pass