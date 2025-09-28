# Create a class Shirt with members as sid,sname,type(formal etc), price and size(small,large etc) .Add following methods: 
# g. Constructor (Support both parameterized and parameterless) 
# h. Destructor 
# i. ShowBook

class Shirt:

    def __init__(self, sid = 102, sname = "Shacket", type = "Casual", price = 549, size = "XL"):
        self.sid = sid
        self.sname = sname
        self.type = type
        self.price = price
        self.size = size

    def __del__(self):
        print("Destructor Called.")

    def showshirt(self):
        print("Shirt ID:", self.sid)
        print("Name of the Shirt:", self.sname)
        print("Type(Formal,Informal,Casual,etc.) of the Shirt:", self.type)
        print("Price of the Shirt:", self.price)
        print("Size of the Shirt:", self.size)

s1 = Shirt(101, "Denim", "Casual", 699, "XL")
s1.showshirt()

s2 = Shirt()
s2.showshirt()

del s1
del s2