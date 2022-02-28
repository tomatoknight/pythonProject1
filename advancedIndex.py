import numpy as np

x = np.array([[1, 2], [3, 4], [5, 6]])
print(x)
print(x[[0, 1, 2], [0, 1, 0]])

b = np.array([
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [9, 10, 11]])
r = np.array([[0, 0], [3, 3]])
c = np.array([[0, 2], [0, 2]])
m = b[r, c]
print(m)

e = b[1:4, 1:3]
print(e)

a = np.array([1, 2+6j, 5, 3.5+5j])
print(a[np.iscomplex(a)])
