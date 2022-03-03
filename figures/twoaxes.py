import matplotlib.pyplot as plt
import numpy as np

# show two axes in one figure.
# fig = plt.figure()
# a1 = fig.add_axes([0, 0, 1, 1])
# x = np.arange(1, 11)
# a1.plot(x, np.exp(x))
# a1.set_ylabel('exp')
#
# a2 = a1.twinx()
#
# a2.plot(x, np.log(x), 'ro-')
# a2.set_ylabel('log')
#
# fig.legend(labels=('exp', 'log'), loc='upper left')
# plt.show()

# show bar figure demo.

# fig = plt.figure()
#
# axes = fig.add_axes([0, 0, 1, 1])
# nations = ['China', 'India', 'United States', 'Japan']
# population = [140, 110, 45, 23]
#
# plt.bar(nations, population)
# plt.show()

# data = [[30, 25, 50, 20],
#         [40, 23, 51, 17],
#         [35, 22, 45, 19]]
#
# X = np.arange(1999, 2003)
# fig = plt.figure()
# #添加子图区域
# ax = fig.add_axes([0.1, 0.1,1,1])
# #绘制柱状图
# ax.bar(X + 0.00, data[0], color = 'b', width = 0.25)
# ax.bar(X + 0.25, data[1], color = 'g', width = 0.25)
# ax.bar(X + 0.50, data[2], color = 'r', width = 0.25)
# plt.show()

# # 绘制堆叠图
# countries = ['USA', 'India', 'China', 'Russia', 'Germany']
# bronzes = np.array([38, 17, 26, 19, 15])
# silvers = np.array([37, 23, 18, 18, 10])
# golds = np.array([46, 27, 26, 19, 17])
# # 此处的 _ 下划线表示将循环取到的值放弃，只得到[0,1,2,3,4]
# ind = [x for x, _ in enumerate(countries)]
#
# plt.bar(ind, golds, width=0.5, label='golds', color='gold', bottom=silvers+bronzes)
# plt.bar(ind, silvers, width=0.5, label='silvers', color='silver', bottom=bronzes)
# plt.bar(ind, bronzes, width=0.5, label='bronzes', color='#CD853F')
#
# plt.xticks(ind, countries)
# plt.ylabel("Medals")
# plt.xlabel("Countries")
# plt.legend(loc="upper right")
# plt.title("2019 Olympics Top Scorers")
# plt.show()

fig, ax = plt.subplots(1, 1)

data = np.array([22, 87, 5, 43, 56, 73, 55, 54, 11, 20, 51, 5, 79, 31, 27])

plt.hist(data, bins=[0, 25, 50, 75, 100])

ax.set_title("直方图式")
ax.set_xticks([0, 25, 50, 75, 100])
ax.set_xlabel('marks')

plt.show()
