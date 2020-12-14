import sys
sys.path.append('../')
from Chapter_1.cave_mouth import CaveMouth
from Chapter_1.river_crossing import RiverCrossing
from Chapter_1.the_woods import TheWoods
from Chapter_2.kings_hideout import KingsHideout
from Chapter_2.princess_blood import PrincessBlood
from Chapter_2.secret_weapon import SecretWeapon
from Chapter_3.final_chapter import FinalChapter
from death import Death



class PlotMaps(object):  # contains all plots of adventure game

    Plots = {
        'cave_mouth' : CaveMouth(),
        'the_woods' : TheWoods(),
        'river_crossing' : RiverCrossing(),
        'kings_hideout' : KingsHideout(),
        'princess_blood' : PrincessBlood(),
        'secret_weapon' : SecretWeapon(),
        'final_chapter' : FinalChapter(),
        'death' : Death()
    }

    def __init__(self, start_plot):
        self.start_plot = start_plot
    
    def next_plot(self, plot_name):  # get next plot
        val = PlotMaps.Plots.get(plot_name)
        return val
    
    def beginning(self):  # display current plot
        return self.next_plot(self.start_plot)

    

