class Product:
    def __init__(self,name,price) :
        self.price  = float(price)
        self.name = name
        
    def desplay_details(self):
        print("Name : ",self.name)
        print("Price : ",self.price)
    

class Electronic_Product(Product):
    def __init__(self, name, price,warrenty):
        super().__init__(name, price)
        self.warrenty = warrenty
    
    def desplay_details(self):

        super().desplay_details()
        print("Warrenty : ",self.warrenty)


e1 = Electronic_Product("Mobile",12500.00,"2 Year")
e1.desplay_details()
    