# sandpile model recursive, every time i add a grain i check if the threshold is reached, if it is i add a grain to the neighbors
# and i check if the threshold is reached, if it is i add a grain to the neighbors and i check if the threshold is reached, if it is i add a grain to the neighbors
# and i check if the threshold is reached, if it is i add a grain to the neighbors and i check if the threshold is reached, if it is i add a grain to the neighbors

# In[ ]:

import numpy as np
import matplotlib.pyplot as plt
import random
from matplotlib import animation

# do sandpile model for a given number of iterations every grain of sand i put i check of there is an avalanche or more than
# one avalanche, and store the number of avalanche that occur in a list and the number of grains that i put in the grid in another list
# and then i plot the number of grains vs the number of avalanche
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

# initialize the figure
fig = plt.figure()
ax = plt.axes(xlim=(0, N), ylim=(0, N))
# initialize the image
im = ax.imshow(grid, interpolation='none', vmin=0, vmax=threshold, cmap='RdPu')

# initialize the list of the number of grains
n_grains_list = []
# initialize the list of the number of topplings
n_topplings_list = []
# initialize the list of the number of avalanche
n_avalanche_list = []

# function to update the grid
def count_avalanche(*args):
    # put random grains on the grid until the threshold is reached at some point
    # choose random coordinates on the grid and put 1 grain on it
    # if the threshold is reached in a point, put the grains on the neighbors
    # and increase the number of topplings, count the number of avalanche that occur and store it in a list
    global grid, n_grains, n_topplings
    while True:
        x = random.randint(0, N - 1)
        y = random.randint(0, N - 1)
        grid[x, y] += 1
        n_grains += 1
        if grid[x, y] < threshold:
            break

        grid[x, y] = 0
        n_topplings += 1
        if x > 0:
            grid[x - 1, y] += 1
        if x < N - 1:
            grid[x + 1, y] += 1
        if y > 0:
            grid[x, y - 1] += 1
        if y < N - 1:
            grid[x, y + 1] += 1
    # update the image
    im.set_array(grid)
    # store the number of grains in a list
    n_grains_list.append(n_grains)
    # store the number of topplings in a list
    n_topplings_list.append(n_topplings)
    # store the number of avalanche in a list
    n_avalanche_list.append(n_topplings_list[0] - n_topplings_list[-1])
    return im,

# run the animation
anim = animation.FuncAnimation(fig, count_avalanche, frames=n_iter, interval=100, blit=True)
plt.show()

# plot the number of grains vs the number of avalanche
plt.plot(n_grains_list, n_avalanche_list)
plt.xlabel('Number of grains')
plt.ylabel('Number of avalanche')
plt.show()

