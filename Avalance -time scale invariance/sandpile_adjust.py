# in this file we adjust the sandpile model
# we need to count how many avalance accours for each number of grains that we put on the grid

import random

import matplotlib.pyplot as plt
import numpy as np

# size of the grid
N = 50
# number of iterations
n_iter = 10000
# threshold for the avalanche
threshold = 4

# initialize the grid
grid = np.zeros((N, N))
# initialize the number of grains
n_grains = 0
# initialize the number of topplings
n_topplings = 0
tops = []

for i in range(n_iter):
    x = np.random.randint(0, N)
    y = np.random.randint(0, N)
    grid[x, y] += 1
    n_grains += 1
    # check is the threshold is reached and if yes, start the avalanche process then recontroll the grid for the threshold
    while np.any(grid > threshold):
        n_topplings += 1
        # find the position of the toppling
        x, y = np.where(grid > threshold)
        # remove the grains from the toppling
        grid[x, y] -= 4
        # add the grains to the neighbors
        if x > 0:
            grid[x - 1, y] += 1
        if x < N - 1:
            grid[x + 1, y] += 1
        if y > 0:
            grid[x, y - 1] += 1
        if y < N - 1:
            grid[x, y + 1] += 1
            
    tops.append(n_topplings)
    n_topplings = 0

# plot the grid
plt.imshow(grid, cmap='hot')
plt.show()

# plot the number of topplings in log scale
plt.plot(np.log(tops))
plt.show()
