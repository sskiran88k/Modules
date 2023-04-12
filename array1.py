import numpy as np
x=np.array([1,2,3,4,7,8],dtype=int)
print(x)
print(type(x))


y=np.array([1.3, 2.4, 3.8, 4, 7, 8,"lendi", 3+4j])
print(y)
print(type(y))
print(y.view())

z=x.copy()
print(z)
