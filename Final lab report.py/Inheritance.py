class Employee:
    name = ""
    id = ""

    def salary(self):
        print("Your Salary is 70000")

class PermanentEmployee(Employee):
    def __init__(self,name,id):
        self.name = name
        self.id = id
        
    

    def calculate_salary(self):
        self.salary()



class ContractEmployee(Employee):

    def __init__(self,name,id):
        self.name = name
        self.id = id

    def calculate_salary(self):
        working_hour = float(input("Enter Your hour :  "))
        Salary = 300 * working_hour
        print(f"Hour : {working_hour},Salary : {Salary}")

print("Parmanent Worker")
Mezbah = PermanentEmployee("Mezbah",1611)
print(f"Name : {Mezbah.name}, ID : {Mezbah.id}")
Mezbah.calculate_salary()

print(" ")
print("Contract Employee")

Tonmoy = ContractEmployee("Tonmoy",1788)
print(f"Name : {Tonmoy.name}, ID : {Tonmoy.id}")
Tonmoy.calculate_salary()