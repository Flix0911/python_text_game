# Lets build a game
# ------------------------------------

import random

# GAME STATE

# game dictionary
game_state = {
    "gold": 0,
    "location": "arena"
}

# location dictionary
location = {
    # where can you go from arena:
    "arena": {
        # can go from barracks back to arena
        "barracks": "arena",
        # can go from training ground back to arena
        "training ground": "arena"
    }
}

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

# win condition - function - 2 args of self and other
def win_conditions(self, other):
    # if your hp is less than 1, you lose
    if (self.hp < 1):
        print("You have died, you lose!")
        # if True, game is over
        return True
    if (other.hp < 1):
    # if other's hp is less than 1, you win
        print(f"${other.name} has died, you win!")
        # if false, game is over
        return False
    
# game set up
    
    # ask for the players name
    player_name = input("What is your name?")

    # player_name is now the Character name
    player = Character(player_name)

    # other character
    goblin = Character("Goblin")

# GAME LOOP

# infinite loop - running forever
while(true):
    # your text input
    input("Do you want to [f]ight, [d]efend, or [q]uit")