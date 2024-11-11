class phone:
    def call(self):
        print("You Can Call")

    def messege(self):
        print("You can messege")


class Samsung(phone):
   

    def photo(self):
        print("You can take photo")

p = phone()
p.call()
p.messege()

s=Samsung()
s.call()
s.photo()



