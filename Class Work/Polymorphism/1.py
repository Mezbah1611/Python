# Runtime Polymorphism example

class Person:
    name = " "
    Age = " "

    def display(self):
        print("Name : ",self.name)
        print("Age : ",self.Age)


class Mezbah(Person):
    name = "Mezbah"
    Age = "22"

    def display(self):
        super().display()


M = Mezbah()
M.display()

