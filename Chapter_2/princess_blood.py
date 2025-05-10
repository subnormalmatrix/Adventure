import sys
sys.path.append('../')

from plot import Plot
from textwrap import dedent
import random

class PrincessBlood(Plot):
    
    def enter(self):
        print(dedent("""
        PRINCESS BLOOD
        
        You have successfully retrieved the secret weapon and brought it to the King's hideout.
        The legend is clear: the weapon can only be activated by the blood of the King's daughter — but that alone is not enough.

        A sealed dial lies at the base of the weapon, unmoving.
        The King’s scholars discovered an inscription barely legible on the metal casing — clues to a 3-digit code required to awaken the device.

        "Begin with the smallest odd prime — neither too low nor too high."
        "The second is its square — power compounding itself."
        "The last is lonely, yet necessary. The number before nothing, and the start of all things."

        You realize this isn’t just a code — it’s a test. One mistake, and the dial may lock for good.
        You have three attempts to enter the correct sequence.

        The fate of the Kingdom once again rests on your shoulders \n
        """))


        code = "391"
        guess = input('[keypad]> ')


        if guess.strip() == code:
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


