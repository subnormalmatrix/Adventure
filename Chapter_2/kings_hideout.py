import sys
sys.path.append('../')

from plot import Plot
from textwrap import dedent


class KingsHideout(Plot):

    def enter(self):
        print(dedent(""" 
        Well done on rescuing the Princess Mensima. The Kingdom of surface dwellers is forever in your debt.
        However, you are still not out of the woods yet. You have to take the Princess back to the King's hideout.
        You begin your slow descent of Manjaro into the surrounding valley. There's a shortcut to get the Princess safely to the King.
        You take this path, walking hand in hand with the princess when all of a sudden two sea dwellers jump out of nowhere.
        It soon becomes clear that they were lying in wait for you the whole time. What do you do?
        'Fight', 'Run' or 'Tell a joke'? \n
        """))
        choice = input('> ')

        if choice == 'Fight':
            print(dedent("""
            Well, well, well, Superman, that was unwise. You are easily subdued by your enemies.
            The Princess' scream is the last thing you hear before your head is torn off from your body.\n
            """))
            return 'death'

        elif choice == 'Run':
            print(dedent("""
            Quick thinking, sea dwellers are much slower on land than at sea.
            You run away together with the Princess in the other direction, traversing the long route to get to the King's hideout.
            Before long you lose your pursuers and stop to take a breath. You arrive safely at the King's Hideout together with Princess Mensima by nightfall
            \n
            """))
            return 'secret_weapon'

        elif choice == 'Tell a joke':
            print(dedent("""
            Unfortunately, you have run out of stupid jokes to tell. You are dead!
            Hades can't wait to hear your jokes in the afterlife \n
            """))
            return 'death'

        else:
            print(dedent("""
            Hmmm! I blame the system for churning out people that can't read. Pick one of the three choices.
            """))
            return 'kings_hideout'

