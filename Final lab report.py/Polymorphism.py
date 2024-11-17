class Transport:
    weight = ""
    distance = ""

    def __init__(self, weight, distance):
        self.weight = weight
        self.distance = distance

    def calculate_cost(self):
        pass  

class Truck(Transport):
    def calculate_cost(self):
        cost = (self.weight * 5) * (self.distance / 10)
        print("Truck Cost : ", cost)

class Ship(Transport):
    def calculate_cost(self):
        cost = (self.weight * 3) * (self.distance / 10)
        print("Ship Cost : ", cost)

class Plane(Transport):
    def calculate_cost(self):
        cost = (self.weight * 10) * (self.distance / 4)
        print("Plane Cost : ", cost)



truck = Truck(30, 20)
truck.calculate_cost()

ship = Ship(40, 10)
ship.calculate_cost()

plane = Plane(3, 2)
plane.calculate_cost()
