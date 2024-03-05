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
        # define hp between 1-20
        self.hp = random.randint(1, 20)
        # random str between 4-8
        self.strength = random.randint(4, 8)
        # random def between 1-4
        self.defense = random.randint(1, 4)
        # random acc between 1-10
        self.accuracy = random.randint(1, 10)

    # define attack. Arg of self and other
    def attack(self, other):
        # random die role to see if you successfully hit
        if(random.randint(1, 10) <= self.accuracy):
            # how much damage the hit will cause
            damage = self.strength - other.defense
            # how much hp is reduced by the damage
            other.hp -= damage
            # print response for damage done and how much hp is left
            print(f"${self.name} hit ${other.name} for ${damage} damage, they have ${other.hp} left!")
        else:
            # print response for failing an attack
            print(f"${self.name} fails to attack ${other.name}")


# FUNCTIONS


# GAME LOOP

# infinite loop - running forever
while(true):
    pass