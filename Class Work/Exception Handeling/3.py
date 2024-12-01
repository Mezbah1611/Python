arr = [10,5,15,20]
try:
    divisor = int(input("Enter a divisor : "))
    results = []
    for i in arr:
        results.append(i/divisor)

except ZeroDivisionError:
    print("Division by zero is not allowed")
except ValueError:
    print("Please enter a valid integer")
except TypeError:
    print("Invalid data type")
except IndexError:
    print("Array Index out of bounds")
except AttributeError:
    print("Invalid Attribute")
except FileNotFoundError:
    print("File not Found")
except NameError:
    print("Name is not Found")

else:
    print("Divivssion Succesful ",results)
finally:
    print("Execution Completed")


