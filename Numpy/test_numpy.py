import numpy as np  # 1 D array or vector
a = np.array([1, 2, 3])
print(a)
print(type(a))
print(a.shape)
print(a.ndim) # dimension


b = np.array([[1,2,3],[4,5,6]])
print(type(b))
print(b.shape)
print(b.ndim)


c = np.array([[[1.0,2,3],[4,5,6],[7,8,9]]])
print(type(c))
print(c.shape)
print(c.ndim)
print("")
print(c)
print("")
print(b)
print("")
print(a)

print(a.dtype) # data type
print(b.dtype)
print(c.dtype)

print(c.size) # how many element 
print(a.size)
print(b.size)

print(a.nbytes) # determine how many bytes consumed in memory
print(b.nbytes)
print(c.nbytes)