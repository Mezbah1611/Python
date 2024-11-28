employee = {
    "Name": "A",
    "Age": "40",
    "Type": {"developer": ["ios", "android"]},  
    "Permanent": True, 
    "Salary": 30000,  
    100: (1, 2, 3),
    4.5: {5.6, True, 7, 1}
}

x = employee.keys()
print("Keys : ",x)

y = employee.values()
print("Values : ",y)

z = employee.items()
print("Items : ",z)