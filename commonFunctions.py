import numpy as np

# a = np.arange(9).reshape(3, 3)
# print(a)
#
# print(a.ravel())
#
# b = np.array([[1], [2], [3]])
# c = np.array([5, 6, 7])
# d = np.broadcast(b, c)
#
# e = np.arange(4).reshape(1, 4)
# print(np.broadcast_to(e, (4, 4)))

a = np.arange(9).reshape(3, 1, 3)
print(a)
print(".................")
b = np.arange(9).reshape(1, 3, 3)
print(b)
print(".................")
c = np.arange(9).reshape(3, 3, 1)
print(c)
