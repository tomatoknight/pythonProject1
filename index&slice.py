import numpy as np

a = np.arange(10)
print(a)
s = slice(2, 9, 3)
print(a[s])

an = np.array([[1, 2, 3], [3, 4, 5], [4, 5, 6]])
print(an)
print(an[1:])
print('......................')
print(an[..., 1])
print(an[1, ...])
print(an[..., 1:])
