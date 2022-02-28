import numpy as np

x = np.arange(1, 10, 2)
print(x)

y = np.linspace(1, 2, 5, retstep=True)
print(y)

z = np.logspace(1, 10, num=10, base=2)
print(z)
