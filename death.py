from plot import Plot
from sys import exit
from random import randint
import time

class Death(Plot):

    def enter(self):
        self.death_msg= [
            'Oh come on, even my grandma plays better than this!',
            "Don't take this the wrong way but you are pretty useless!",
            "Thanks for raising our hopes up mate, what a disappointment!",
            "You lost fool, Game Over!",
            "And just like that you dashed all our hopes",
            "Run along to your mother now, loser!",
            "Sigh, some adventurer you are mate!"
        ]
        print(f'{self.death_msg[randint(0, len(self.death_msg) - 1)]}\n') # randomly select death messages to display
        time.sleep(5)
        exit(1)

