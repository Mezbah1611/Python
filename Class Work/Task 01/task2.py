from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand):
        self.brand = brand

    @abstractmethod
    def start_engine(self):
        pass  

    def description(self):
        print(f"This is a vehicle from {self.brand}.")


class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def start_engine(self):
        print(f"The engine of {self.brand} {self.model} has started.")


car = Car("Toyota", "Corolla")
car.start_engine()  
car.description()   
