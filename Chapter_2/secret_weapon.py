import sys
sys.path.append('../')

from plot import Plot
from textwrap import dedent
from random import randint

class SecretWeapon(Plot):

    def enter(self):
        print(dedent("""
        Great job so far!. The King is pleased with you and showers you with many gifts. However, he asks you to help him once again.
        Legend has is that a secret weapon of mass destruction is hidden in an unmarked location between the foothills of Manjaro
        and the swamp region of Mosengo. During the time you were gone, the surveyours of the King's court were able to pinpoint the exact location of the weapon.
        All that is left is its retrieval. The King orders two of his most trusted bodyguards and one of his brightest surveyors to accompany you to the site.
        
        Soon enough you arrive at the location. It's an abandoned hideout, a cave of sorts with ancient writings and hieroglyphics.
        The surveyor takes the lead, you follow behind together with the two guards cautiously watching for any booby traps.
        A few more steps and the surveyor suddenly stops. He seems to be pointing to a strange looking case. The surveyor then tells you the
        case houses the secret weapon the legend foretold, but there is something the legend left out. 
        
        On closer inspection, you realise the casing requires a four digit code eah digit between 0-9 to be entered before it can ever be opened.
        You only have 10 attempts to enter the code, fail and something indescribable and certainly not good might befall you.

        """))

        passcode = f'{randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}'
        hint = list(passcode)
        hint.pop(1) # remove second number
        hint.pop(1) # remove third number
        guesses = 0  # number of guesses
        m = 0

        guess = input('[keypad]> ')
        
        while  passcode != guess and  guesses < 9:
            print("Wrong!")

            if m == 0:
                choice = input("Do you want a hint? y' or 'n'?> ")
                if choice == 'y':
                    print(f'\nthe first and last numbers are {hint}')
                    m += 1
                elif choice == 'n':
                    pass
            guesses += 1
            guess = input('[keypad]> ')

        if guess == passcode:
            print(dedent("""
            With a soft click, the case opens, revealing the secret weapon. It gives off a bright green glow, the surveyor takes the weapon with great care and places it in a bag.
            The party together with yourself leave the cave headed for the king's hideout\n
            """))
            return 'princess_blood'

        else:
            print(dedent("""
            After the last try at cracking the code, there's a loud noise, followed by a quake, the cave collapses in, killing and burying you all in the process.
            Game over!\n
            """))
            return 'death'















        