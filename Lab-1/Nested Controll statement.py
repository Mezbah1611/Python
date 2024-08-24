passes = 0
failure = 0

for student in range(10):
    result = int(input('Enter result (1=pass, 2=fail) :'))
    if result ==1:
        passes = passes +1
    else:
        failure = failure +1

print("Passed : ",passes)
print("Failure : ",failure)
if passes>8:
    print("Bonus to Instructor")
















