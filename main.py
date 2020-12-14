import sys
sys.path.append('../')
from plot_maps import PlotMaps
from game_engine import GameEngine

load_map = PlotMaps('cave_mouth')
load_game = GameEngine(load_map)
load_game.play()

