# file to simulate black scholes model

import numpy as np

# parameters
S0 = 100
mu = 0.1
sigma = 0.2
T = 1
N = 1000
dt = T / N

seed = 10

# generate random numbers
np.random.seed(seed)
z = np.random.standard_normal(N)
z = np.append(0, z)

# simulate stock price
S = np.zeros(N + 1)
S[0] = S0
for i in range(1, N + 1):
    S[i] = S[i - 1] * np.exp((mu - 0.5 * sigma ** 2) * dt + sigma * np.sqrt(dt) * z[i])

# plot
import matplotlib.pyplot as plt
plt.plot(S)
plt.show()
