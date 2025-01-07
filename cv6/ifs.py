import numpy as np
import matplotlib.pyplot as plt
import random

class Transformation:
    def __init__(self, a, b, c, d, e, f, g, h, i, j, k, l, p):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
        self.g = g
        self.h = h
        self.i = i
        self.j = j
        self.k = k
        self.l = l
        self.p = p # probability

    def calculate(self, x, y, z):
        m1 = np.array([
            [self.a,self.b,self.c],
            [self.d,self.e,self.f],
            [self.g,self.h,self.i]
        ])

        m2 = np.array([
            [x],
            [y],
            [z]
        ])

        m3 = np.array([
            [self.j],
            [self.k],
            [self.l]
        ])

        return np.matmul(m1, m2) + m3



class Model:
    def __init__(self, data):
        self.transformations = data



class IFS:
    def __init__(self):
        self.model = None

    def fill_with_data(self, data):
        self.model = data

    def evaluate(self, x, y, z):
        rand = random.uniform(0,1)
        for row in self.model.transformations:
            if rand < row.p:
                return row.calculate(x, y, z)


    def solve(self, epochs):
        # starting point
        x = 0
        y = 0
        z = 0

        # history
        x_ = []
        y_ = []
        z_ = []

        for i in range(0, epochs):
            #print(f"x: {x} y: {y} z: {z}")
            x,y,z = self.evaluate(x,y,z).flatten()
            x_.append(x)
            y_.append(y)
            z_.append(z)

        return x_, y_, z_


# first model
t1 = Transformation( 0.00,  0.00,  0.01,  0.00, 0.26,  0.00, 0.00, 0.00, 0.05, 0.00, 0.00, 0.00, 0.25)
t2 = Transformation( 0.20, -0.26, -0.01,  0.23, 0.22, -0.07, 0.07, 0.00, 0.24, 0.00, 0.80, 0.00, 0.50)
t3 = Transformation(-0.25,  0.28,  0.01,  0.26, 0.24, -0.07, 0.07, 0.00, 0.24, 0.00, 0.22, 0.00, 0.75)
t4 = Transformation( 0.85,  0.04, -0.01, -0.04, 0.85,  0.09, 0.00, 0.08, 0.84, 0.00, 0.80, 0.00, 1.00)
transformations = []
transformations.append(t1)
transformations.append(t2)
transformations.append(t3)
transformations.append(t4)
model1 = Model(transformations)

# second model
t1 = Transformation(  0.05, 0.00,  0.00, 0.00, 0.60, 0.00,  0.00,  0.00,  0.05, 0.00, 0.00, 0.00, 0.25)
t2 = Transformation( 0.45, -0.22,  0.22, 0.22, 0.45, 0.22, -0.22,  0.22, -0.45, 0.00, 1.00, 0.00, 0.50)
t3 = Transformation(-0.45,  0.22, -0.22, 0.22, 0.45, 0.22,  0.22, -0.22,  0.45, 0.00, 1.25, 0.00, 0.75)
t4 = Transformation( 0.49, -0.08,  0.08, 0.08, 0.49, 0.08,  0.08, -0.08,  0.49, 0.00, 2.00, 0.00, 1.00)
transformations = []
transformations.append(t1)
transformations.append(t2)
transformations.append(t3)
transformations.append(t4)
model2 = Model(transformations)

# solve
ifs = IFS()
ifs.fill_with_data(model2)
(x_, y_, z_) = ifs.solve(1000)


# draw
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
#ax.scatter(x_, y_, z_)
ax.scatter(x_, y_, z_, color='black', alpha=1)

plt.show()
