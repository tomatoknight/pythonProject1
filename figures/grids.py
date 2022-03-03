import matplotlib.pyplot as plt
import  matplotlib
import numpy as np
# from mpl_toolkits import mplot3d
# fig, axes = plt.subplots(1, 3, figsize=(12, 4))
# x = np.arange(1, 11)
# axes[0].plot(x, x**3, 'g', lw=2)
# axes[0].grid(True)
# axes[0].grid(color='b', ls='-.', lw=0.25)
#
# axes[0].spines['bottom'].set_color('blue')
# axes[0].spines['bottom'].set_linewidth('2')
# axes[0].set_ylim(0, 800)
# axes[0].set_xlim(0, 8)
# plt.show()

x = np.arange(0, 2 * np.pi, 0.05)

fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])

ax.set_xticks([0, 2, 4, 6])
ax.set_xticklabels(['zero', 'two', 'four', 'six'])
ax.set_title("正弦曲线")

ax.plot(x, np.sin(x), '--', color='g')
plt.show()

