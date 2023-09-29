# the first day doing montecarlo simulation
# try to simulate complex sistem of a paramagnetic material in a magnetic field
# the material is a 1D lattice of spins, each spin can be up or down
# the energy of the system is given by the sum of the interaction between the spins
# the interaction is given by the hamiltonian of the system
# the hamiltonian is given by the sum of the interaction between the spins
"""
import numpy as np
import matplotlib.pyplot as plt
import random
import math
import time

# define the lattice
N = 5  # number of spins
# random initial configuration
spins = np.random.randint(0, 2, N) * 2 - 1

# count numeber of up and down spins
# only for checking the distribution
up = np.count_nonzero(spins == 1)
down = np.count_nonzero(spins == -1)
print(f'up: {up/N*100}%, down: {down/N*100}%')

# define the hamiltonian
J = 0.01  # interaction constant
# using boundary condition PBC
H = -J * np.sum(spins * np.roll(spins, 1))
# the np.roll function shift the array of 1 position to the right and the last element is put in the first position
print(f'Hamiltonian: {H}')"""
import numpy as np
import itertools

# now i do for every possible configuration of the system
# i start from the initial configuration and i flip one spin at a time
# i comupute the hemiltonian and save the value in an array
J = 0.01
hem = np.zeros(2 ** 3)
# for every configuration i change 1 spin at a time and compute the hamiltonian
a = [1, -1]
b = 3  # Actually, you just need the length of the array, values do not matter
c = itertools.product(a, repeat=b)
lista = list(c)
print(lista)
# now for every configuration i compute the hamiltonian
for i in range(2 ** 3):
    for j in range(3):
        hem[i] += -J * lista[i][j] * lista[i][(j + 1) % 3]
print(hem)

Z = np.sum(np.exp(-hem*1))
print(Z)

