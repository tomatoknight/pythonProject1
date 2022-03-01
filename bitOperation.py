import numpy as np

a = 10
b = 12
print("a的二进制表示：", bin(a))
print("b的二进制表示：", bin(b))
print("a和b按位与操作：", np.bitwise_and(a, b))

arr = np.array([20], dtype=np.uint8)
print(arr)

print(np.right_shift(40, 2))