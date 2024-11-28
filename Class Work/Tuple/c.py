a = (1,3,5,7,4)

odd_count = 0
even_count = 0

for i in a: 
    if i % 2 !=0: 
        odd_count +=1
    else:
        even_count +=1

print("Odd Number : ",odd_count)
print("Even Number : ",even_count)