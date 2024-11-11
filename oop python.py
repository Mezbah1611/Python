class Student():
    ID = ""
    CGPA = ""

    def __init__(self,ID,CGPA):
        self.ID = ID
        self.CGPA = CGPA

    def display(self):
        print(f"Roll : {self.ID}, CGPA : {self.CGPA}")



Mezbah = Student(1611,3.50)
Mezbah.display()

Charu = Student(1844,3.98)
Charu.display()
        
