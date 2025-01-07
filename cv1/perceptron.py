import numpy as np
import matplotlib.pyplot as plt
import random

"""
Consider a line given by the following equation:

 y = 3x + 2

Task:

Generate the set of 100 points and use a perceptron to find out whether the
points lie above, below, or on the line.

Instructions:

Visualize the line and the points (use different colors for points lying above, below, and on the line)

"""

# activation functions

def Signum1(x):
    if x < 0: return -1
    if x > 0: return 1
    if x == 0: return 0

def Signum(x):
    return np.sign(x)

def Sigmoid(x):
    return (np.exp(x)) / (np.exp(x) + 1)

def RelU(x):
    return max(0, x)

class Perceptron:
    def __init__(self):
        # weights
        self.w1 = np.random.uniform(0,1)
        self.w2 = np.random.uniform(0,1)

        # bias
        self.b = np.random.uniform(0,1)

        self.activation_function = Signum1

    # output calculation
    def guess(self, x, y, activation_fn):
        sum_ = (self.w1 * x) + (self.w2 * y) + self.b
        yguess = activation_fn(sum_)
        return yguess

    # train
    def train(self, data):
        learning_rate = 0.1

        for point in data:
            x = point[0]
            y = point[1]
            y_ = point[2]

            yguess = self.guess(x, y, self.activation_function)

            error = (y_ - yguess)
            self.w1 += error * x * learning_rate
            self.w2 += error * y * learning_rate
            self.b += error * learning_rate


    def train_e(self, data, epochs):
        for e in range(0, epochs):
            self.train(data)


    #test
    def test(self, data):
        result = []
        for point in data:
            x = point[0]
            y = point[1]
            y_ = point[2]

            yguess = self.guess(x, y, self.activation_function)
            result.append((x, y, yguess))
        return result


#y = 3x + 2
def calculate_y_(x, y):
    y_ = 3 * x + 2

    if y == y_: return 0
    if y > y_: return 1
    if y < y_: return -1

# generate
train_data = []
for i in range(0, 100):
    x = random.randint(-50, 50)
    y = random.randint(-50, 50)
    y_ = calculate_y_(x, y)
    train_data.append((x, y, y_))


p = Perceptron()
p.train_e(train_data, 200)
#p.train(train_data)
#print(p.w1)
#print(p.w2)
#print(p.b)

# test
test_data = []
for i in range(0, 100):
    x = random.randint(-50, 50)
    y = random.randint(-50, 50)
    y_ = calculate_y_(x, y)
    test_data.append((x, y, y_))


result = p.test(test_data)


# draw
redx = []
redy = []
greenx = []
greeny = []
bluex = []
bluey = []


for point in result:
    x = point[0]
    y = point[1]
    yguess = point[2]

    if yguess == 0:
        redx.append(x)
        redy.append(y)
    if yguess > 0:
        greenx.append(x)
        greeny.append(y)
    if yguess < 0:
        bluex.append(x)
        bluey.append(y)


# draw points

plt.scatter(redx, redy, c='red', label="on line")
plt.scatter(greenx, greeny, c='green', label="above")
plt.scatter(bluex, bluey, c='blue', label="below")


# draw line | y = 3 * x + 2

plt.axline((-17, -51), (16, 50), label="y=3x+2")


plt.xlim = (-50, 50)
plt.ylim = (-50, 50)

plt.legend()

plt.show()
