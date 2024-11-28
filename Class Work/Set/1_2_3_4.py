
import sys
a = {1,3,5,8,3,7}
b = {0,False,1,5}

print(a)
print(b)

print(len(a))
print(len(b))

print(sys.getsizeof(a))
print(sys.getsizeof(b))

a.add(10)
print(a)

a.remove(8)
print(a)