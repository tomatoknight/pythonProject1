import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
print(a)

#b = np.resize(a, (3, 2))
#print(b)

#print(a.resize(1, 6))

print(np.append(a, [7, 8, 9]))
print(np.append(a, [[7, 8, 9]], axis=0))

print(np.insert(a, 3, [11, 12]))
print("The third commit")
