import numpy as np

array1 = np.array([1,2,3],dtype='int')
print(array1)


zerors = np.zeros((3,3),dtype= 'int')  # for zero
print(zerors)  

Ones = np.ones((3,3),dtype='int')  # for one
print(Ones)


full = np.full((2,3),5) # ful for any number
print(full)


identity = np.identity(3,dtype= 'int')  # for identity matrix
print(identity)


eye = np.eye(3,3,-2) # shift right(for + number),shift down(for - number)
print(eye)
print(" ")

arrange = np.arange(2,10,2) # start 2,upto 10, gap 2
print(arrange)

print("  ")

linspace = np.linspace(1,10,5,dtype= 'int') #  start 1, end 10,how many value 5
print(linspace)
print(linspace.size)


print(" " )
empty = np.empty((1,5))
print(empty)

for i in range(5):
    empty[:,i] = i

print(empty)
