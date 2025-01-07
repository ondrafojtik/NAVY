import numpy as np
import matplotlib.pyplot as plt
#from matplotlib.colors import ListedColorMap
from matplotlib.colors import LinearSegmentedColormap
import random

def show_matrix(data, title):
    fig, ax = plt.subplots()
    ax.matshow(data)
    ax.set_title(title)
    plt.waitforbuttonpress()

# 1 = trap
# 2 = path
# 3 = cheese

map = np.array([
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0],
    [3, 0, 0, 1, 0],
    [0, 0, 0, 0, 0]
])


def inside_map(action, data):
    inside = 0
    if action[0] < 0: inside += 1
    if action[0] >= data.shape[0]: inside += 1
    if action[1] < 0: inside += 1
    if action[1] >= data.shape[1]: inside += 1

    if inside == 0:
        return True
    else:
        return False


def convert_map_to_R(data):
    R = np.full((data.shape[0]**2,data.shape[0]**2), -1)

    for x, row in enumerate(data):
        for y, _ in enumerate(row):
            # 4 actions
            bot =   (x+1, y)
            top =   (x-1, y)
            left =  (x,   y-1)
            right = (x,   y+1)

            actions = [bot, top, left, right]
            for action in actions:
                if inside_map(action, data):
                    x_coord = x * data.shape[0] + y
                    y_coord = action[0] * data.shape[1] + action[1]
                    if data[action] == 0:
                        R[x_coord, y_coord] = 0
                    if data[action] == 1:
                        R[x_coord, y_coord] = -10
                    if data[action] == 3:
                        R[x_coord, y_coord] = 100
                    #print(f"a: {action}")
    return R


class QLearning:
    def __init__(self):
        self.data = map
        self.Q = np.zeros((self.data.shape[0]**2, self.data.shape[1]**2))
        self.R = convert_map_to_R(self.data)


    def train(self, epochs):
        for i in range(0, epochs):
            self.train2()

    def train2(self):
        learning_rate = 0.8

        curr_pos = np.random.randint(0, self.R.shape[0])

        # to move
        possible_moves = []
        for i in range(0, self.R.shape[0]):
            if self.R[curr_pos][i] >= 0: possible_moves.append(i)
        to_move = np.random.randint(0, len(possible_moves))
        to_move = possible_moves[to_move]

        line_max = max(self.Q[to_move])

        # eval
        self.Q[curr_pos, to_move] = self.R[curr_pos, to_move] + learning_rate * line_max


    def test(self, position):
        curr_pos = position
        cheese = ()

        # find cheese
        for x, row in enumerate(map):
            for y, value in enumerate(row):
                if value == 3:
                    cheese = (x,y)
                    break

        path = []
        while True:
            if curr_pos == cheese:
                break

            path.append(curr_pos)

            x = curr_pos[0]
            y = curr_pos[1]

            row = self.Q[x * self.data.shape[0] + y]
            max_row = 0 # to move (index)
            for i in range(0, len(row)):
                if row[i] >= row[max_row]: max_row = i

            next_y = np.mod(max_row, np.size(map, axis=1))
            next_x = int((max_row - next_y) / np.size(map, axis=0))
            curr_pos = (next_x, next_y)


        return path








ql = QLearning()
ql.train(10000)
path = ql.test((0,0))
print(path)

# visualize
map_ = ql.data

for p in path:
    pass
    map_[p] = 2

show_matrix(map_, "QLearning")



# 6                                                              0 _
# rotace vzdy "doprava" (kdyz prictu uhel, tak zatacim doprava =>  | 1 == F+F
# [ == aktualni pozice + rotace
# ] == vratit se k posledni [ -> pokracuju dal od toho
# nejdriv generovat axiom, az potom vykreslovat
