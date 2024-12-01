class salaryNotInRange(Exception):
    def __init__(self, salary) :
        self.salary = salary
        super().__init__("Salary is not in range")

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def checksalary(self):
        if self.salary <10000 or self.salary > 50000:
            raise salaryNotInRange(self.salary)
    def display_salary(self):
        self.checksalary()
        print("Name : ",self.name)
        print("Salary : ",self.salary)


try: 
    

    emp2 = Employee("Tonmoy",60000)  
    emp2.display_salary()     
except salaryNotInRange as e:
    print(e)
    
