import numpy as np
import matplotlib.pyplot as plt


# 8
pattern1 = np.array([
    [0, 1, 1, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 1, 1, 0]
])

# 2
pattern2 = np.array([
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 1, 1, 0]
])

# X
pattern3 = np.array([
    [1, 0, 0, 0, 1],
    [0, 1, 0, 1, 0],
    [0, 0, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [1, 0, 0, 0, 1]
])

def show_matrix(data, title):
    fig, ax = plt.subplots()
    ax.matshow(data, cmap="binary")
    ax.set_title(title)
    plt.waitforbuttonpress()


class Hopfield:
    def __init__(self):
        self.dim = 5
        self.W = np.zeros((self.dim**2, self.dim**2))

    def train(self, image):
        image[image==0] = -1
        image_ = image.flatten()
        image_[image_==0] = -1
        image_T = image_.T


        for x in range(0, self.dim**2):
            for y in range(0, self.dim**2):
                self.W[x, y] += image_[x] * image_[y]


        #self.W += np.outer(image_, image_T)
        np.fill_diagonal(self.W, 0)

    def test_async(self, image):
        image[image==0] = -1
        res = image.flatten()
        V = image.flatten()
        for i in range(0, self.dim**2):
            res[i] = np.sign(np.matmul(self.W[i], V))
        res = np.reshape(res, (self.dim,self.dim))
        return res

    def test_sync(self, image):
        image[image==0] = -1
        image_ = image.flatten()
        res = np.sign(np.matmul(self.W, image_))
        res = np.reshape(res, (self.dim,self.dim))
        return res


# damaged 8
damaged_pattern1 = np.array([
    [0, 1, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0]
])

# damaged 2
damaged_pattern2 = np.array([
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 1, 1, 0]
])

# damaged X
damaged_pattern3 = np.array([
    [1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [1, 0, 0, 0, 0]
])

# train
h = Hopfield()
h.train(pattern1)
h.train(pattern2)
h.train(pattern3)

# draw (+ test)

# default
show_matrix(pattern1, "pattern1")
show_matrix(pattern2, "pattern2")
show_matrix(pattern3, "pattern3")

# damaged patterns
show_matrix(damaged_pattern1, "damaged 1")
show_matrix(damaged_pattern2, "damaged 2")
show_matrix(damaged_pattern3, "damaged 3")

# async
res = h.test_async(damaged_pattern1)
show_matrix(res, "damaged 1 - async")
res = h.test_async(damaged_pattern2)
show_matrix(res, "damaged 2 - asnyc")
res = h.test_async(damaged_pattern3)
show_matrix(res, "damaged 3 - asnyc")

# sync
res = h.test_sync(damaged_pattern1)
show_matrix(res, "damaged 1 - sync")
res = h.test_sync(damaged_pattern2)
show_matrix(res, "damaged 2 - snyc")
res = h.test_sync(damaged_pattern3)
show_matrix(res, "damaged 3 - snyc")



plt.show()
