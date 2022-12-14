import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0, 2*np.pi, 0.01)

for radius in range(0, 37, 12):
    x = radius/10 * np.cos(t)
    y = radius/10 * np.sin(t)

    plt.plot(x, y)
plt.show()