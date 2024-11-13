import numpy as np
arr1 = np.array([1,2,3,4,5])
print(arr1)

print(arr1[0])
print(arr1[1:3])
print("New value : ",arr1[0:10])

arr2 = np.random.randint( 1,10,size=(3,3)) # start 1,end 10 randomly number taken
print(arr2)
print(arr2[0,2])
print(arr2[0,0])
print("Slicing row and column : ",arr2[0:2,0:2])

print(" ")

arr3 = np.random.randint(1,10,size=(2,3,3))
print(arr3)
print(arr3[0,1,2])
print(arr3[1,2,1])