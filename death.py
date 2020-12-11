from plot import Plot
from sys import exit
from random import randint

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
        print(f'\n{self.death_msg[randint(0, len(self.death_msg) - 1)]}') # randomly select death messages to display
        exit(1)

trial = Death()
trial.enter()