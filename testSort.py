import numpy as np

a = np.array([[3, 7], [9, 1]])
print(a)

print("a排序后：\n", np.sort(a))

dt = np.dtype([('name', 'S10'), ('age', int)])
b = np.array([('raju', 21), ('love', 32), ('steph', 31), ('jake', 35)], dtype=dt)
print(b)
print(np.sort(b, order='name'))

c = np.array([345, 34, 21, 432, 11])
sort_id = np.argsort(c)
print(sort_id)
for a in sort_id:
    print(c[a], end=" ")

