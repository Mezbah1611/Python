c = [1, 3, 5, 7, 4, 2, 4, 6]
b = c.copy()
print(b)

b.sort()
print(b)

for i in b:
    print(i)
    if i == 5:
        break