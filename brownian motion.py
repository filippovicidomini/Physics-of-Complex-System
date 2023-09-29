# file to simulate a brounian motion
import numpy as np
import matplotlib.pyplot as plt
import random
import math
import time

T = 100  # number of steps
dt = 0.002  # time step

T = int(T/dt)

# the function goes as a normal
# the function is a random walk

f = np.zeros(T) # array of position of the particle
f[0] = 0    # initial position

for i in range(1, T):
    f[i] = f[i-1] + np.random.normal(0, np.sqrt(dt))    # the position is the sum of the previous position and a random number

difference = [(f[i] - f[i-1])**2 for i in range(1, T)]  # difference between the position of the particle in two different time step squared

sum = np.sum(difference)
# propriety for all trajectories of a brownian motion
# the sum of the square of the difference between the position of the particle in two different time is equal to the time
#
print(sum)

#plt.legend()
# using latex in title
plt.rc('text', usetex=True)     #use latex for the number axis label
plt.rc('font', family='serif')  #use serifed font

plt.figure(figsize=(10, 6), dpi=200) # set the size of the figure

plt.title(r'position of a particle in a brownian motion')
plt.xlabel('step')
plt.ylabel('position')
plt.grid()
plt.plot(f, label='position', color='red')
plt.tight_layout()
plt.show()
