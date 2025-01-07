
# saturation 255

import numpy as np
import matplotlib.pyplot as plt
import random

class TEA:

    def solve(self):
        iterations = 100
        n = 1500

        radius = 1

        center = (0, 0)



        xmin = -2.0
        xmax = 1.0

        ymin = -1.5
        ymax = 1.5

        m = 2.0

        xvals = np.linspace(xmin, xmax, n)
        yvals = np.linspace(ymin, ymax, n)

        result = np.zeros([n,n])

        for x_i, x in enumerate(xvals):
            for y_i, y in enumerate(yvals):
                z = 0
                c = complex(x,y)
                for i in range(0, iterations):
                    z = z * z + c
                    if (abs(z) > m):
                        #result[y_i, x_i] = abs(200 - (i * 4))
                        result[y_i, x_i] = i
                        break
        return result

tea = TEA()
res = tea.solve()

fig = plt.figure()
ax = fig.add_subplot()
#ax.imshow(res)
#ax.imshow(res, cmap="hsv")
#ax.imshow(res, cmap="inferno")
ax.imshow(res, cmap="twilight_shifted")
#ax.imshow(res, cmap="nipy_spectral")

plt.show()
