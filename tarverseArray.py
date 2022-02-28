import numpy as np

a = np.arange(0, 60, 5)

a = a.reshape(3, 4)
print(a)
for x in np.nditer(a):
    print(x)

for x in np.nditer(a, order='F'):
    print(x)

for x in np.nditer(a, op_flags=['readwrite']):
    x[...] = 2*x
print(a)

for x in np.nditer(a, flags=['external_loop'], order='F'):
    print(x)

b = np.arange(0, 60, 5)
b = b.reshape(3, 4)
print(b)

c = np.array([1, 2, 3, 4], dtype=int)
print(c)
for x, y in np.nditer([b, c]):
    print("%d:%d" % (x, y), end=",")


