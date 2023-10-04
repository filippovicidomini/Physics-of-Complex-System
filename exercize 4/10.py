# calculate and compute the numericalli an equation from landou theory of phase transition
# m = tanh(beta*J*m + *H)
# m1 = np.tanh(beta*J*m0 + H)
# m2 = np.tanh(beta*J*m1 + H) # m1 is the m0 of the next step
# beta = 1/T

# graph of f(m) respect to m

import matplotlib.pyplot as plt
import numpy as np

T = 273.15  # temperature
beta = 1 / T  # inverse temperature
J = 10 ** 3  # interaction constant

H = 0  # magnetic field

m = np.arange(-1.5, 1.5, 0.01)



f = np.tanh(beta * J * m + H)

plt.figure(figsize=(12, 10), dpi=200)

# using latex
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

plt.xlabel(r'$m$', fontsize=40, labelpad=10)
plt.ylabel(r'$f(m)$', fontsize=40, labelpad=10)
plt.title(r'Graph of $f(m)$ respect to $m$', fontsize=25)

# font size of the ticks of the axis
plt.xticks(fontsize=25)
plt.yticks(fontsize=25)

plt.grid(True, linewidth=1, linestyle='--')

plt.plot(m, f, label=r'$f(m)$', linewidth=3)
plt.plot(m, m, label=r'$m$', linewidth=3)

plt.legend(loc='best', fontsize=40)

plt.tight_layout()

plt.savefig('graph_of_f(m)_respect_to_m.png')
plt.show()

# find a numerical solution for the equation m = tanh(beta*J*m + *H)

def fixed_point(f, x0, tol, max_iter):
    x = x0
    for i in range(max_iter):
        x = f(x)
        if abs(x - x0) < tol:
            return x
        x0 = x
    return x

def fixed_point_iteration(m0):
    return np.tanh(beta * J * m0 + H)

m0 = 0
tol = 1e-10
max_iter = 1000

m1 = fixed_point(fixed_point_iteration, m0, tol, max_iter)
print(m1)

