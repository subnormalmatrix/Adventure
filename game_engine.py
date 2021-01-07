import time
import sys

class GameEngine(object):

    def __init__(self, plot_map):
        self.plot = plot_map
    
    def play(self):
        current_plot = self.plot.beginning()  # opening scene of adventure game
        last_plot = self.plot.next_plot('final_chapter')    # last scene of adventure game

        while current_plot != last_plot:
            next_plot_name = current_plot.enter()      # next scene name
            time.sleep(3)
            
            for i in range(21):
                sys.stdout.write('\r')
                sys.stdout.write('LOADING [%-20s] %d%%' % ('='*i, 5*i))
                sys.stdout.flush()
                time.sleep(0.50)
                
            print('\n')

            current_plot = self.plot.next_plot(next_plot_name)

        # print out the last plot
        current_plot.enter()



    