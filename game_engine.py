import time

class GameEngine(object):

    def __init__(self, plot_map):
        self.plot = plot_map
    
    def play(self):
        current_plot = self.plot.beginning()  # opening scene of adventure game
        last_plot = self.plot.next_plot('final_chapter')    # last scene of adventure game

        while current_plot != last_plot:
            next_plot_name = current_plot.enter()      # next scene name
            print("Loading................................................................................\n")
            time.sleep(5)  # delay for 5 seconds
            current_plot = self.plot.next_plot(next_plot_name)

        # print out the last plot
        current_plot.enter()



    