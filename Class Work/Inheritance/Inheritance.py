class Person:
    def __init__(self,first_name,last_name) :
        self.first_name = first_name
        self.last_name = last_name

class Student(Person):
    graduation_year = ""

    def display(self):
        pass

class Teacher(Person):
    Joinig_year = " "

    def display(self):
        pass

class Admin(Person):
    Joinig_year = " "

    def display(self):
        pass

class Alumni(Student):
    Passing_year = " "
    def display(self):
        return super().display()

class Current_student(Student):
    Current_Semister = " "

    def display(self):
        return super().display()

class Employee(Teacher,Admin):
    id = " "
    def display(self):
        return super().display()
        