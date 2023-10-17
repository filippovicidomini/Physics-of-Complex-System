# simulation of eden's model with a single cell

import random

import matplotlib.pyplot as plt
import numpy as np


def single_neighbour(lattice, neighbour, cell):
    # give a cell that is just occupied and return the neighbour of that cell that are free and add to the list of
    # neighbours, then remove the double neighbours
    if lattice[cell[0] - 1][cell[1]] == 0:
        neighbour.append([cell[0] - 1, cell[1]])

    if lattice[cell[0] + 1][cell[1]] == 0:
        neighbour.append([cell[0] + 1, cell[1]])

    if lattice[cell[0]][cell[1] - 1] == 0:
        neighbour.append([cell[0], cell[1] - 1])

    if lattice[cell[0]][cell[1] + 1] == 0:
        neighbour.append([cell[0], cell[1] + 1])

    return neighbour


def eden_model(lattice=np.zeros((100, 100)), occupided=[], p=0.5, steps=10000, photo=4, candidate=[]):
    global neighbour
    if occupided == []:
        occupided.append([lattice[0].size // 2, lattice[0].size // 2])
        lattice[lattice[0].size // 2][lattice[0].size // 2] = 1
        neighbour = single_neighbour(lattice, [], occupided[0])
    # print(lattice)
    # print(neighbour)

    for i in range(steps):
        if random.random() < p:
            # print(neighbour[0])
            new = random.choice(neighbour)
            lattice[new[0]][new[1]] = 1
            neighbour.remove(new)
            occupided.append(new)
            neighbour += single_neighbour(lattice, [], new)
            # print(neighbour)

    plt.imshow(lattice, cmap="gray")
    # print the neighbours in different color to see if the algorithm works
    for i in range(len(neighbour)):
        plt.scatter(neighbour[i][1], neighbour[i][0], color="red", s=3)


    plt.xticks([])
    plt.yticks([])
    plt.figure(figsize=(16, 14), dpi=300)
    plt.tight_layout()
    plt.show()

    return lattice


print(eden_model())
