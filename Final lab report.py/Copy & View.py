import numpy as np

a = np.array([
    [1,2,3,4,5],
    [4,5,6,7,8],
    [8,9,0,1,2],
    [6,7,8,9,0]
])

print(a)
print("\nCreate a view of third row")
print(a[2,:])
print("\nCreate a copy of third column")
print(a[:,2].copy())

print("\n Modify the array")
b = a[2,:]
b[:] = 0
print(b)
print("After Modify Orginal array")
print(a)

print("\n Copy of third column and modify")
c =a[:,2].copy()
c[:] = 0
print(c)
print("After Modify Orginal Array")
print(a)