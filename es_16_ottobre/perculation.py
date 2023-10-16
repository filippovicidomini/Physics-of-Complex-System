# doing side perculation on a 2D lattice

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import time


p = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]
L = 100
def perculation_side(p, lattice=np.zeros((100, 100))):
    for i in range(lattice[0].size):
        for j in range(lattice[0].size):
            if random.random() < p:
                lattice[i][j] = 1
    return lattice

plt.rc('text', usetex=True)
plt.rc('font', family='serif')
# 6 grafici per ogni p

fig, ax = plt.subplots(2, 3, figsize=(16, 14), dpi=300)
fig.suptitle(r"\textbf{Side Perculation}", fontsize=30)

for i in range(len(p)):
    ax[i // 3][i % 3].set_title(r"\textbf{p = " + str(p[i]) + "}", fontsize=20)
    ax[i // 3][i % 3].set_xlabel(r"\textbf{x}", fontsize=20)
    ax[i // 3][i % 3].set_ylabel(r"\textbf{y}", fontsize=20)
    ax[i // 3][i % 3].set_xticks([])
    ax[i // 3][i % 3].set_yticks([])
    ax[i // 3][i % 3].imshow(perculation_side(p[i], np.zeros((L, L))), cmap="gray")
plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
plt.savefig("perculation_side.png")
plt.show()
