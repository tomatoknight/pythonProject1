import numpy as np
from matplotlib import pyplot as plt
from pylab import *
import math


# x = np.arange(1, 11)
# y = 2 * x + 5
# plt.title("Line Demo")
# plt.xlabel("x axis")
# plt.ylabel("y axis")
# plt.plot(x, y, "-.b")
# plt.show()

# x = np.arange(0, 3 * np.pi, 0.1)
# y_sub1 = np.sin(x)
# y_sub2 = np.cos(x)
#
# plt.subplot(2, 1, 1)
# plt.plot(x, y_sub1)
#
# plt.subplot(2, 1, 2)
# plt.plot(x, y_sub2)
#
# plt.show()

# y = [1, 4, 9, 16, 25,36,49, 64]
# x1 = [1, 16, 30, 42,55, 68, 77,88]
# x2 = [1,6,12,18,28, 40, 52, 65]
# fig = plt.figure()
# ax = fig.add_axes([0,0,1,1])
# #使用简写的形式color/标记符/线型
# l1 = ax.plot(x1,y,'ys-')
# l2 = ax.plot(x2,y,'go--')
# ax.legend(labels = ('tv', 'Smartphone'), loc = 'lower right') # legend placed at lower right
# ax.set_title("Advertisement effect on sales")
# ax.set_xlabel('medium')
# ax.set_ylabel('sales')
# plt.show()

plt.plot([1,2,3])
#现在创建一个子图，它表示一个有2行1列的网格的顶部图。
#因为这个子图将与第一个重叠，所以之前创建的图将被删除
plt.subplot(211)
plt.plot(range(12))
#创建带有黄色背景的第二个子图
plt.subplot(212, facecolor='y')
plt.plot(range(12))
plt.show()
