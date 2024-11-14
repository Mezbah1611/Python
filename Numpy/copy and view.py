import numpy as np

x = np.array([10,20,30,40,50,60,70,80,90])
print(x)
b = x[3:6].copy()
b[:] = 0
print(b)
print(x)
