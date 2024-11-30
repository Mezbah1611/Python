class vehicle:
    def __init__(self,color):
        self.color = color

    def vehicle_info(self):
        print("Model : ",self.color)

class Taxi(vehicle):
        def __init__(self, color,model,capacity,variant):
             super().__init__(color)
             self.__model = model
             self.__capacity = capacity
             self.__variant = variant
        
        #def setModel(self,model):
           #  self.__model = model
        
        def getModel(self):
             return self.__model
        
        def setCapacity(self,capacity):
             self.__capacity = capacity
        def getCapacity(self):
             return self.__capacity
        def setVariant(self,variant):
             self.__variant = variant
        def getVariant(self):
             return self.__variant
        
        def vehicle_info(self):
             super().vehicle_info()
             print("Model : ",self.__model)
             print("Capacity : ",self.__capacity)
             print("Variant : ",self.__variant)

t = Taxi("Black ","E232","3 person","Horse")
t.vehicle_info()
print("\t\n Anoter Car\t\n")
t2 = Taxi("White", "X500", "4 person", "Diesel")
t2.vehicle_info()