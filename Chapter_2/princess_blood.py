import sys
sys.path.append('../')

from plot import Plot
from textwrap import dedent
from random import randint

class PrincessBlood(Plot):
    
    def enter(self):
        print(dedent("""
        PRINCESS BLOOD
        
        You have successfully retrieved the secret weapon and brought it to the King's hideout.
        The legend makes it clear that secret weapon can only be operated by the blood of the King's daughter.
        The King's team of scientists and historians have studied the weapon and found something interesting.
        There's a small nob at the base of the weapon that would not budge unless a single digit between 0-9 is entered.
        Much like the situation in the cave no one can tell what will happen after all attempts to guess this code correctly fails.
        Once again the fate of an entire Kingdom rests on your shoulders! You have only 5 attempts\n
        """))

        code = f'{randint(0,9)}'
        guesses = 0
        guess = input('[keypad]> ')

        while guess != code and guesses < 4:
            print('Wrong!')
            guesses += 1
            guess = input('[keypad]')

        if guess == code:
            print(dedent("""
            You guessed the number correctly, a glass vial slows pops out. The scientists carefully fill this vial with blood so graciously provided by the Princess.
            When the vial is placed back into the weapon it makes a clicking sound and then the color changes from bright green to dark red, showing the weapon is activated.
            All that is left now is to attack the base of the sea dwellers and finish off every last one of them!
            
            END OF CHAPTER 2!
            \n
            """)) 
            return 'final_chapter'

        else:
            print(dedent("""
            You failed at guessing the correct digit. There is a loud click, followed by a release of poisnous gas.
            It kills everyone including yourself.You are dead! Way to go champ! \n
            """))
            return 'death'


