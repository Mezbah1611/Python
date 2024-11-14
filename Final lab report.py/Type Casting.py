import numpy as np

data = np.array([
    ["Mezbah",1611,200.30],
    ["Charu",1844,100.50],
    ["Tonmoy",1788,150.78],
    ["Sazzad",1756,20.50]
])


print(data)
print(data.dtype)

id = data[:,1].astype(int)
print(id)
print(id.dtype)

salary = data[:,2].astype(float)
print(salary)
print(salary.dtype)