# mandelbrot set in python
# scale the value of the plot and use the color map to show the iteration
import matplotlib.pyplot as plt
import numpy as np


def mandelbrot(xmin, xmax, ymin, ymax, h, w, maxit=60):
    # set the range and scale
    y, x = np.ogrid[ymin:ymax:h * 1j, xmin:xmax:w * 1j]
    c = x + y * 1j
    z = c
    # do the iteration
    divtime = maxit + np.zeros(z.shape, dtype=int)
    for i in range(maxit):
        z = z ** 2 + c
        diverge = z * np.conj(z) > 2 ** 2
        div_now = diverge & (divtime == maxit)
        divtime[div_now] = i
        z[diverge] = 2
    return divtime


plt.rc('text', usetex=True)
plt.rc('font', family='serif')
plt.figure(figsize=(10, 10), dpi=300)

plt.title(r"\textbf{Mandelbrot Set}", fontsize=20)

plt.xlabel(r"\textbf{Re}", fontsize=20)
plt.ylabel(r"\textbf{Im}", fontsize=20)

plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)

plt.imshow(mandelbrot(-2, 1, -1.5, 1.5, 1000, 1000))
plt.savefig("mandelbrot.png")
plt.show()
