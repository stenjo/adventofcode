import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from AoC13_classes import ArcadeCabinet, Compute


result = []
i = 0
class AnimatedScatter(object):
    """An animated scatter plot using matplotlib.animations.FuncAnimation."""
    def __init__(self, numpoints=10):
        self.numpoints = numpoints
        self.stream = self.data_stream()
        self.index = 0
        # Setup the figure and axes...
        self.fig, self.ax = plt.subplots()
        # Then setup FuncAnimation.
        self.ani = FuncAnimation(self.fig, self.update, interval=1, 
                                          init_func=self.setup_plot, blit=True)

    def setup_plot(self):
        """Initial drawing of the scatter plot."""
        x, y, s, c = next(self.stream).T

        self.scat = self.ax.scatter(x, y, c=c, s=s, vmin=0, vmax=1, cmap="jet", edgecolor="k")
        self.ax.axis([-1, 45, -1, 25])
        # For FuncAnimation's sake, we need to return the artist we'll be using
        # Note that it expects a sequence of artists, thus the trailing comma.
        return self.scat,

    def data_stream(self):
        dt = result[self.index]
        x = [d['pos'][0]    for d in dt]
        y = [d['pos'][1]    for d in dt]
        s, c = np.random.random((self.numpoints, 2)).T
        while True:
            dt = result[self.index]
            self.index += 1
            x = [d['pos'][0]    for d in dt]
            y = [d['pos'][1]    for d in dt]
            c = [d['tile']*10   for d in dt]
            yield np.c_[x, y, 's', c]


    def update(self, i):
        """Update the scatter plot."""
        data = next(self.stream)

        # Set x and y data...
        self.scat.set_offsets(data[:, :2])
        # Set sizes...
        self.scat.set_sizes(300 * abs(data[:, 2])**1.5 + 100)
        # Set colors..
        self.scat.set_array(data[:, 3])

        # We need to return the updated artist for FuncAnimation to draw..
        # Note that it expects a sequence of artists, thus the trailing comma.
        return self.scat,

def CreatePlot():
        infile = open('data/input_13.txt','r')
        program = infile.readline().strip().split(',')
        # program[0] = 2
        a = ArcadeCabinet(program)

        # act
        a.comp.LoadInput([2,0])
        for i in range(10):
            a.WriteTiles()
            result.append(a.tiles)
            a.tiles = []


if __name__ == '__main__':
    CreatePlot()
    a = AnimatedScatter()
    plt.show()
