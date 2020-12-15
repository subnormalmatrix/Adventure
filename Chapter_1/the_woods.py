import sys
sys.path.append('../')

from plot import Plot
from textwrap import dedent

class TheWoods(Plot):

    def enter(self):
        print(dedent("""
        THE WOODS

        After making your way through the back of the cave, you stumble into the woods.
        You squint your eyes for a second, the sun shining brightly over your head.
        The air is fresh, the birds are chirping, the monkeys are running up and down the branches
        You take a moment to observe nature, but then you hear the voice of a woman screaming.
        You quickly chase after the sound of distress and chance upon two sea dwellers.
        One is covering her mouth with its webbed hand, she is struggling to break free.
        The Princess Mensima is truly beautiful but this is no time to be admiring her beauty as one sea dweller approaches.
        The other sea dweller uses the opportunity to escape.
        What do you do now ?
        'Fight', 'Tell a joke', 'Chase after the princess?'\n
         """))

        choice = input('>' )

        if choice == 'Fight':
            print(dedent("""
            From your previous encouter with a sea dweller, you know to aim for its head.
            You pick an unevenly shaped rock and throw it at its head.
            Its head smashes in, oozing a blue gooey substance which is probably its blood.
            You then chase after the Princess\n
            """))
            return 'river_crossing'

        elif choice == 'Tell a joke':
            print(dedent("""
            If a comedian is what it took to save the kingdom, we would have employed the services of the King's Jester.
            You are kicked in the groin, you grovel to the ground, writhing in pain.
            Your head is stamped on, your brain matter spewing everywhere\n
            """
            ))
            return 'death'

        elif choice == 'Chase after the princess':
            print(dedent("""
            It's a bad move Romeo, an uppercut lands perfectly on your chin. It's a knockout, an untimely death\n
            """))
            return 'death'

        else:
            print('Pick one of the choices and pay attention to the casing idiot!')
            return 'the_woods'