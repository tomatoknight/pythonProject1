import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(1, 3, figsize=(12, 4))
x = np.arange(1, 11)
axes[0].plot(x, x**3, 'g', lw=2)
axes[0].grid(True)
axes[0].grid(color='b', ls='-.', lw=0.25)
plt.show()

