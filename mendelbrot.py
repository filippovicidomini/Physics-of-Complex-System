# mandelbrot set in python
# we check and set white or black depending on the number of iterations

import matplotlib.pyplot as plt
import numpy as np

iteration = 0
max_iteration = 1000
x = np.linspace(-2, 2, 1000)
y = np.linspace(-2, 2, 1000)

# create a 2d array of complex numbers
c = x[:, None] + 1j * y[None, :]
z = np.zeros_like(c)

# do the iteration
while iteration < max_iteration:
    z = z**2 + c
    iteration += 1

# create a mask of the points that diverge
mask = (np.abs(z) < 2)

# plot the set
plt.imshow(mask.T, extent=[-2, 2, -2, 2], cmap='gray')
# using latex+mathtext
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

plt.title(r'$z_{n+1} = z_n^2 + c$')
plt.xlabel(r'$\mathrm{Re}(c)$')
plt.ylabel(r'$\mathrm{Im}(c)$')

#plt.savefig('mandelbrot.png')
plt.tight_layout()
plt.show()
