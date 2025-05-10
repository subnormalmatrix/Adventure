import sys
sys.path.append('../')

from plot import Plot
from textwrap import dedent

class SecretWeapon(Plot):

    def enter(self):
        print(dedent("""
        SECRET WEAPON

        Great job so far! The King is pleased with you and showers you with many gifts. However, he asks you to help him once again.
        Legend has it that a secret weapon of mass destruction is hidden in an unmarked location between the foothills of Manjaro
        and the swamp region of Mosengo. During the time you were gone, the surveyors of the King's court pinpointed its exact location.
        All that remains is its retrieval. The King orders two of his most trusted bodyguards and one of his brightest surveyors
        to accompany you to the site.

        Soon enough, you arrive at the location. It's an abandoned hideout—a cave of sorts with ancient writings and hieroglyphics.
        The surveyor takes the lead. You follow behind, together with the two guards, cautiously watching for booby traps.
        A few more steps and the surveyor suddenly stops, pointing at a strange-looking case. He tells you the case houses
        the secret weapon the legend foretold—but there is more to this tale.

        On closer inspection, you realize the casing requires a four-digit code (each digit 0–9) to open. You have only one chance
        to enter the correct code before the mechanism locks forever.

        Etched on the metal are these riddles to guide you to the sequence:
        1. "Begin with the smallest prime in the Fibonacci sequence."
        2. "Next, continue to the very next number in that sequence."
        3. "Then, follow the pattern: each number is the sum of its two predecessors."
        4. "Finally, stop at the first value less than ten after repeating this sum."

        Make your single attempt wisely; failure is fatal.
        """))


        passcode = '2358'
        guess = input('[keypad]> ')

        if guess.strip() == passcode:
            print(dedent("""
            With a soft click, the case opens, revealing the secret weapon. It gives off a bright green glow. The surveyor carefully
            places the weapon in a reinforced bag. With the prize secured, you and your party depart the cave, victorious.
            """))
            return 'princess_blood'
        else:
            print(dedent("""
            A deafening click resonates through the chamber. The edges of the case glow red, then the mechanism seals shut forever.
            A tremor shakes the cave, and darkness overtakes you. Game over.
            """))
            return 'death'
