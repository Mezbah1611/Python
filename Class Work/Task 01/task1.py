
class Vehicle:
    def start(self):
        print("Vehicle started.")

    def stop(self):
        print("Vehicle stopped.")

class Car(Vehicle):
    def drive(self):
        print("Car is being driven.")


class Motorcycle(Vehicle):
    def ride(self):
        print("Motorcycle is being ridden.")

car = Car()
motorcycle = Motorcycle()

car.start()         
car.drive()          
car.stop()          

motorcycle.start()  
motorcycle.ride()    
motorcycle.stop()    
