import datetime

import numpy as np

# teacher = numpy.dtype([('name', 'S20'), ('age', 'i1'), ('salary', 'f4')])
# print(teacher)
# b = numpy.array([('yes', 33, 1133.22), ('Mike', 23, 232.69), ('Rose', 41, 2121.56)])
# print(b)
# print(b.shape)
#
# c = numpy.arange(24)
# print(c)
# print(c.ndim)
# ea = c.reshape(4, 3, 2)
#
# print(ea)
# print(ea.ndim)
# print(ea.flags)

arr = np.empty((3, 2), dtype=int)
print(arr)

long = (1, 2, 3, 4, 5)
a = np.asarray(long)
print(type(a))
print(a)

print(datetime.datetime.now())

