
from abc import ABC,abstractclassmethod
class Shape(ABC):
    def __init__(self,dim1,dim2) :
        self.dim1=dim1
        self.dem2= dim2
    
    @abstractclassmethod

    def area(self):
        pass

class tringle(Shape):
    def area(self):
        area = 0.5 * self.dim1 * self.dem2
        print("Area of Tringle : ",area)

class Renctangle(Shape):
    def area(self):
        area = self.dim1 * self.dem2
        print("Area of Tringle : ",area)

t1 = tringle(3,5)
t1.area()

r1 = Renctangle(3,5)
r1.area()