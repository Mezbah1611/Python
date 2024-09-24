num = int(input("Enter a number : "))
num_1 =0
num_2 = 1
count = 0

if num <= 0:
    print("Only for positive number")

else:
    print("The fibonacci series of the given number is ")
    while count < num:
        print(num_1)
        otherwise = num_1 + num_2
        num_1 = num_2
        num_2 = otherwise
        count +=1






