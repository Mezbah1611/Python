def divide_element(values,divisor):
    results = []
    


    if not isinstance(divisor,(int,float)):
        print("Error : The divisor must be in numeric form")


    
    for value in values:
        try:
            result = value/divisor
            results.append(result)
            

        except ZeroDivisionError:
            print("Error : Divission by zero is not possible")
            return

    print("Result : ",results)
    return results


values = [10,20,30,40,50]
try:
    divisor = float(input("Enter the divisor : "))
    divide_element(values,divisor)

except ValueError:
    print("Error : Please enter numeric number")
        

