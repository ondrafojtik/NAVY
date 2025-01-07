import numpy as np
import matplotlib.pyplot as plt
import random
import math

data_to_draw = 4

def rotate_vector(vector, angle):
    x = vector[0] * math.cos(angle) - vector[1] * math.sin(angle)
    y = vector[0] * math.sin(angle) + vector[1] * math.cos(angle)
    return [x, y]

def rotate(vector, angle):
    # base
    base = -45
    base += angle

    res = rotate_vector(vector, math.radians(base))
    norm = np.linalg.norm(res)
    res = res / norm

    return res


# test data
test_data = []

anxiom = "F+F+F+F"
rule = "F+F-F-FF+F+F-F"
angle = 90
depth = 3
test_data.append((anxiom, rule, angle, depth))

anxiom = "F++F++F"
rule = "F+F--F+F"
angle = 60
depth = 3
test_data.append((anxiom, rule, angle, depth))

anxiom = "F"
rule = "F[+F]F[-F]F"
angle = np.pi / 7
depth = 3
test_data.append((anxiom, rule, angle, depth))

anxiom = "F"
rule = "F[+FF][-FF]F[-F][+F]F"
angle = np.pi / 5
depth = 4
test_data.append((anxiom, rule, angle, depth))


anxiom = test_data[data_to_draw][0]
rule = test_data[data_to_draw][1]
angle = test_data[data_to_draw][2]
depth = test_data[data_to_draw][3]

# create anxiom
for i in range(0, depth):
    new_anx = ""
    for letter in anxiom:
        if letter == "F":
            new_anx += rule
        else:
            new_anx += letter
    anxiom = new_anx

x__ = []
y__ = []

# starting point
x__.append(0)
y__.append(0)

curr_angle = 0
curr_pos = (0, 0)
tmp_pos = []
tmp_angle = []

# iter through anxiom
for letter in anxiom:
    trgt_pos = (1,1)
    if letter == "F":
        x__.append(curr_pos[0])
        y__.append(curr_pos[1])
        trgt_pos = rotate(trgt_pos, curr_angle)
        trgt_pos = (curr_pos[0] + trgt_pos[0], curr_pos[1] + trgt_pos[1])
        x__.append(trgt_pos[0])
        y__.append(trgt_pos[1])
        curr_pos = trgt_pos
    if letter == "+":
        curr_angle -= angle
    if letter == "-":
        curr_angle += angle
    if letter == "[":
        tmp_pos.append(curr_pos)
        tmp_angle.append(curr_angle)
    if letter == "]":
        curr_pos = tmp_pos.pop()
        curr_angle = tmp_angle.pop()


# draw
plt.plot(x__, y__)
plt.show()
