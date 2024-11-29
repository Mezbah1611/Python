class Shape:
    def __init__(self, name):
        self._name = name  
    def setName(self, name):
        
        self._name = name
    
    def getName(self):
        
        return self._name
    
    def display_info(self):
        
        print("Name:", self._name)


class Rectangle(Shape):
    def __init__(self, name, length, width):
        
        super().__init__(name)
        self.__length = float(length)
        self.__width = float(width)
    
    def Area(self):
        
        return self.__length * self.__width
    
    def Perimeter(self):
        
        return 2 * (self.__length + self.__width)
    
    def display_info(self):
        
        super().display_info()  
        print("Area:", self.Area())  
        print("Perimeter:", self.Perimeter())  


r = Rectangle("Mezbah", 5, 6)  
r.display_info()  
