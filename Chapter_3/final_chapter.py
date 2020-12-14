import sys
sys.path.append('../')

from plot import Plot
from textwrap import dedent
from random import randint

class FinalChapter(Plot):

    def enter(self):
        print(dedent("""
        The King has mustered all his able warriors and appointed you as their captain to lead them into battle.
        Your task is to infiltrate the enemy's base, plant the weapon at the centre of the enemy's cap and then disarm it.
        Using stealth mode techniques, your army together with yourself disarm and kill all the sea dwellers guarding the entrance.
        You then proceed into an inner room where the center should be located, but not before telling your army to make haste for shelter.
        You move cautiously and slowly approach the center. That is when you notice a lone huge figure standing a few metres away.
        The King of the sea dwellers, it is a very fearsome creature with many scars across its face and smells ten times as bad as its surbodinates.
        What do you do now? 
        'Slowly place the weapon' or 'Throw the weapon'?\n
        """))
        choice = input('> ')

        if choice == 'Slowly place the weapon':
            print(dedent("""
            You make a gesture of dropping the weapon and your foe starts to sweat and puts its hands up in surrender.
            You inch closely towards the center and then carefully place the bomb on the floor. You quickly run out of the room, reaching for the disarmer in your pocket in the process.
            You only have three attempts to correctly guess the number between 0-6 to activate the weapon. Failure would mean certain death!
            """))
            code = f'{randint(0,5)}'
            guesses = 0
            guess = input('[keypad]> ')

            while guess != code and guesses < 2:
                print('Wrong!')
                guesses += 1
                guess = input('[keypad]')

            if guess == code:
                print(dedent("""
                You guessed correctly. Not long after, you hear the all too familiar clicking sound as you run desperately for the hills of Manjaro to take cover.
                The King of sea dwellers is too scared to move and before long the weapon goes off, wiping out the bloody sea dwellers!
                Hurray! Hurray! Hurray! Hurray!


                Thank you great adventurer for saving the Kingdom of surface dwellers. It is true what they say, "Never judge a book by its cover".
                You looked like a total fraud but then you proved to be competent in the end. Unfortunately, this is not your normal happily ever after.
                You don't get the beautiful Princess Mensima. You should go out and bond with people in the real world.
                


                Glad you took time to play this game. Hope you enoyed it!
                Copyright MatrixStudios
                \n
                """))
            else:
                print(dedent("""
                You failed at guessing the correct digit. The King sea dweller pounces on you and mauls you to death. Mission failed!
                 \n
                """))
                return 'death'

        elif choice == 'Throw the weapon':
            print(dedent("""
            In a panic you throw the weapon at the King of sea dwellers. He tries to catch it but misses.
            The weapon hits the floor and cracks, exploding instantenously. Just like that everything turns to dust, including yourself.
            You are totally annihilated but hey at least you took the darn King of sea dwellers and the remaining sea dwellers with you\n
            """))
            return 'death'

        else:
            print('Learn to follow simple instructions')
            return 'final_chapter'

