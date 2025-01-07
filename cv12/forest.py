import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib import animation
import random
import time
import copy

# empty  0
# tree   1
# fire   2

custom_colors = ['gray', 'green', 'red']
cmap = colors.ListedColormap(custom_colors)


class ForestFire:

    def __init__(self):
        self.history = []

        self.forest_dims = (100, 100)
        # init
        self.forest = np.zeros(self.forest_dims)
        for x_ in range(0, self.forest_dims[0]):
            for y_ in range(0, self.forest_dims[1]):
                rndm = random.randint(0, 100)
                if rndm >= 30: self.forest[x_][y_] = 1
                else: self.forest[x_][y_] = 0
        self.history.append(self.forest)
        # other defines
        self.p = 0.05
        self.f = 0.0001
        self.density = 0.7

        # start fire
        self.forest[30, 30] = 2



    def iterate(self):
        new_forest = copy.deepcopy(self.forest)
        for x in range(0, self.forest_dims[0]):
            for y in range(0, self.forest_dims[1]):
                _random = random.uniform(0, 1)
                _type = self.forest[x][y]
                if _type == 0 and _random < self.p:
                    new_forest[x][y] = 1
                if _type == 1:
                    if x == 0 or y == 0 or x == self.forest_dims[0]-1 or y == self.forest_dims[1]-1: continue
                    else:
                        if _random > self.density: continue

                        if self.forest[x-1][y] == 2: new_forest[x][y] = 2
                        if self.forest[x+1][y] == 2: new_forest[x][y] = 2
                        if self.forest[x][y+1] == 2: new_forest[x][y] = 2
                        if self.forest[x][y-1] == 2: new_forest[x][y] = 2
                        if _random < self.f: new_forest[x][y] = 2
                if _type == 2:
                    new_forest[x][y] = 0
        self.forest = copy.deepcopy(new_forest)
        self.history.append(self.forest)

    def print_matrix(self):
        ax.clear()
        ax.matshow(self.forest, cmap=cmap)
        plt.show()


    def solve(self, iterations):
        for i in range(0, iterations):
            self.iterate()
        self.animate()



        #while True:
        #    self.print_matrix()
        #    self.iterate()



    def animate(self):
        def update_animation(i):
            _anim_data.set_array(self.history[i])

        fig, ax = plt.subplots()
        _anim_data = ax.matshow(self.history[0], cmap=cmap)
        a = animation.FuncAnimation(fig, update_animation, interval=100)
        plt.show()




solver = ForestFire()
solver.solve(1000)
