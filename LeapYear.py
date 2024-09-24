def CheackLeap(year):
    if((year%400==0) or

            (year%100!= 0) and
            (year%4 == 0)):
        print("Given Year is leap Year")
    else:
        print("Not Leap Year ")

year = int(input("Enter the Year : "))
CheackLeap(year)