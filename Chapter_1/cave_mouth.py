import sys
sys.path.append('../')
from plot import Plot
from textwrap import dedent

class CaveMouth(Plot):
    def enter(self):
        print(dedent('''
        Welcome to Adventure 1.0.
        Life on the surface has changed for the worst ever since the arrival of the sea dwellers.
        The land has been ravaged by wars, wild fires and drought. 
        The sea dwellers have a deep disdain for the surface dwellers and have not held back in making this fact clear.
        They have killed a lot of the surface dwellers, the remaining survivors have been turned into slaves or are on the run for their lives.
        The king of the surface dwellers has a daughter named Mensima, the future of the kingdom rests on her shoulders. 
        The surface dwellers have a very powerful weapon hidden somewhere on the land. Legend has it that only the blood of the King's daughter would be able to operate this weapon. 
        Unfortunately Princess Mensima has been captured by a group of sea dwellers. The last sighting of them was in the lost hills of Manjaro heading for an abandoned cave.
        You are to rescue the princess and then continue on many perilous journeys to save the kingdom of the surface dwellers. Bon Voyage!
        \n'''))
        name = input("What is your name? > ")
        choice_1 = input(f"\nGreat Adventurer {name}, infront of you lies the mouth of the cave. Will you 'Enter' or 'Run Away' like a spineless coward? > ")
        print('\n')
        if choice_1 == 'Enter':
            print(dedent("""
            Oh great and marvelous adventurer, the kingdom of surface dwellers thanks you for the courage.
            Do yout best! Rescue Princess Mensima and save the kingdom of the surface dwellers\n"""))
            
            print(dedent("""
            Upon entering the cave, your footsteps startles one of the sea dwellers who happened to be taking a piss nearby.
            It stinks of deep waters, its breath smells like fish. 
            It watches you from the dark with its beady green eyes, its scaly skin shimmering in the dark like silver.
            Even from where it stands, you feel its blood lust.
            What do you do? 'Tell a joke', 'Fight it or 'Charge through'?\n"""))

            choice_2 = input('> ')

            if choice_2 == 'Tell a joke':
                print(dedent("""
                Luckily for you, all those years of telling corny lame jokes seem to have paid off.
                The sea dweller is holding its sides and laughing, rolling on the floor. 
                You manage to grab a stick lying around and hit the head of this disgusting beast, killing it instantly.
                However, it seems the others together with the princess have escaped through an opening in the back of the cave. 
                Track and rescue the princess\n"""))
                return 'the_woods'

            elif choice_2 == 'Fight it':
                print(dedent("""
                Watching a couple of anime episodes does not make you a fighter mate!. The sea dweller kills you with one blow """))
                return 'death'

            elif choice_2 == 'Charge through' :
                print(dedent("""
                You think this is a game of football?. You get mowed down like a pancake, see you in the afterlife"""))
                return 'death'

            else:
                print('You definitely failed your English class. Pick one of the three choices')
                return 'cave_mouth'


        elif choice_1 == 'Run Away':
            print('Even a eunuch has more balls than you do. What a loser!')
            return 'death'
        
        else:
            print("Pick one of the two choices moron!. It's either you man up and 'Enter' the cave or 'Run Away' like a coward, jeez!!!")
            return 'cave_mouth'

