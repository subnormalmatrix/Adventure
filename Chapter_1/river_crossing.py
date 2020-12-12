import sys
sys.path.append('../')

from plot import Plot
from textwrap import dedent

class RiverCrossing(Plot):

    def enter(self):
        print(dedent("""
        After defeating the sea dweller, you chase after the remaining foe and the princess.
        The sound of twigs breaking under your sole as you follow the screams of Princess Mensima.
        Suddenly you see two figures struggling in the distance, you quicken your pace.
        You see the sea dweller slowly backing away from the river bank, its arm locking the princess neck in an embrace
        You look to the left and see the river, it's wide and certainly cannot be crossed without a boat.
        You then turn your attention to your foe, with the princess as its hostage what do you do?
        'Tell a joke', 'Charge at the foe' or 'Pelt foe with a stone'?\n
        """))

        choice = input('> ')

        if choice == 'Tell a joke':
            print(dedent("""
            After five minutes of listening to your corny jokes, the sea dweller gets bored. It chokes the princess to death.
            It then charges towards you, spears you to the ground and gouges your eyes out. You are dead!\n
            """))
            return 'death'

        elif choice == 'Charge at the foe':
            print(dedent("""
            You charge at your foe, startled by your choice of action, it releases its grip of the Princess and tries to brace itself for collision.
            The princess wisely moves out of the way, just seconds before you spear the sea dweller to the ground.
            You waste no time bashing its head with you bare fists. Its blue gooey blood spluttering all over your face and fists.
            Alas, you have rescued the Princess Mensima, she gracefully offers her thanks to you for saving her life and besieges 
            you to take her home to her Father. You accept the request and make your way back with her to the King's hideout.

            GREAT JOB SO FAR! END OF CHAPTER 1\n
            """))
            return "king's_hideout"

        elif choice == "Pelt foe with a stone":
            print(dedent("""
            You fly three stones in quick succession, aiming for the head of the sea dweller but it uses the princess as its shield.
            Two of the stones hit her, one strikes her head and kills her instantly.
            Realizing your foolish mistake, you sink your knees down to the earth as you let a loud shriek.
            While you cry like a baby leaving yourself totally unguarded, the sea dweller charges at you and kills you.\n
            """))
            return 'death'

        else:
            print('Learn to follow instructions, pick one of the three choices')
            return 'river_crossing'