import numpy as np
a=np.array([[1, 2, 3, 4],[6, 8, 10, 12],[14, 16, 18, 20],[4, 2, 3, 5]])
b=np.array([[4, 2, 3, 5],[14, 16, 18, 20],[6, 8, 10, 12],[1, 2, 3, 4]])

print(a)
print(a.transpose())
print(a.ndim)
print(a.shape)
print(a.flatten())
print(np.sort(a))
print(np.diagonal(a))
print(a+b)
print(a*b)
