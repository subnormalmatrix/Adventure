import sys
sys.path.append('../')

from plot import Plot
from textwrap import dedent

class FinalChapter(Plot):

    def enter(self):
        print(dedent("""
        FINAL CHAPTER
        
        The King has mustered all his able warriors and appointed you as their captain to lead them into battle.
        Your task is to infiltrate the enemy's base, plant the weapon at the centre of the enemy's camp, and then disarm it.
        Using stealth techniques, you and your army neutralize the sea dwellers guarding the entrance.
        You then proceed into an inner chamber where the device must be deactivated.
        Inside stands a lone, fearsome figure—the King of the sea dwellers, scarred and foul-smelling.
        What do you do now?
        'Slowly place the weapon' or 'Throw the weapon'?
        """))
        choice = input('> ')

        if choice.lower().strip() == 'slowly place the weapon':
            print(dedent("""
            You gesture to drop the weapon. The foe hesitates, then raises its hands in surrender.
            You inch forward and carefully place the bomb at the chamber's center.
            Now, you must deactivate it. A panel slides open revealing a keypad—four digits, each 0–9.
            You have one chance to enter the correct code before it locks forever.

            Etched above the keypad are these cryptic riddles:
            1. "The smallest polygon with all right angles — its sides are your start."
            2. "The number of legs on an arachnid but mirrored."
            3. "Identify the universe's first perfect number."
            4. "A quintet less nothing — what remains?"

            Deactivate wisely; failure means certain doom.
            """))

            passcode = '4865'
            guess = input('[keypad]> ')

            if guess == passcode:
                print(dedent("""
                A soft click echoes as the panel unlocks. You snatch the disarmer and sprint out of the chamber.
                Moments later, the device powers down completely. The King of sea dwellers flees in terror.
                Victory is yours! You and your warriors return to the surface as heroes.
                """))
                return 'victory'
            else:
                print(dedent("""
                An ominous buzz fills the room. The keypad glows red and seals shut.
                The device overloads — an explosion frees you no mercy.
                """))
                return 'death'

        elif choice.lower().strip() == 'throw the weapon':
            print(dedent("""
            In panic, you hurl the weapon at the King of sea dwellers.
            It shatters on impact, detonating instantly. Everything turns to ash, including you.
            """))
            return 'death'

        else:
            print('Learn to follow simple instructions.')
            return 'final_chapter'
