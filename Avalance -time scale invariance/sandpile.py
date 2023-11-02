# compute the sanpile model for a given number of iterations
# and plot the results

import random

import matplotlib.pyplot as plt
import numpy as np
# animation
from matplotlib import animation

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


# function to update the grid
def updatefig(*args):
    # put random grains on the grid until the threshold is reached at some point
    # choose random coordinates on the grid and put 1 grain on it
    # if the threshold is reached in a point, put the grains on the neighbors
    # and increase the number of topplings
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
    return im,


# run the animation
anim = animation.FuncAnimation(fig, updatefig, frames=n_iter, interval=1, blit=True)
# save the animation
anim.save('sandpile.mp4', fps=60, extra_args=['-vcodec', 'libx264'])

# need to plot in logaritm scale to see the power law the number of time that i put a grain and an avalance accours
# plot the number of grains vs the number of topplings
plt.figure()
# in log scale
plt.scatter(n_grains, n_topplings)
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Number of grains')
plt.ylabel('Number of topplings')
plt.title('Number of topplings vs number of grains')

plt.show()
