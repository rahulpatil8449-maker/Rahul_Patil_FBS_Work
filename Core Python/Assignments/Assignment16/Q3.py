# Create a class Shirt with members as sid,sname,type(formal etc), price and size(small,large etc) .Add following methods: 
# j. Constructor (Support both parameterized and parameterless) 
# k. Destructor 
# l. ShowBook 
# m. For each size of shirt price should change by 10%.
# (eg. If 1000 is price then small price = 1000, medium = 1100,large=1200 and xlarge=1300) Use static concept.

class Shirt:

    def __init__(self, sid = 102, sname = "Shacket", type = "Casual", price = 500, size = "XL"):
        self.sid = sid
        self.sname = sname
        self.type = type
        self.price = price
        self.size = size

        # self.final_price = Shirt.calculate(price, size)

    def calculate(real_price, size):
        if(size == "Small"):
            return real_price
        elif(size == "Medium"):
            return real_price * 1.1
        elif(size == "Large"):
            return real_price * 1.2
        elif(size == "XLarge"):
            return real_price * 1.3
        else:
            return real_price 
        
    def __del__(self):
        print("Destructor Called.")

    def showshirt(self):
        self.final_price = Shirt.calculate(self.price, self.size)
        print("Shirt ID:", self.sid)
        print("Name of the Shirt:", self.sname)
        print("Type(Formal,Informal,Casual,etc.) of the Shirt:", self.type)
        print("Price of the Shirt:", self.price)
        print("Final Price of the Shirt is:", self.final_price)
        print("Size of the Shirt:", self.size)
        print("\n")

s1 = Shirt(101, "Denim", "Casual", 1000, "XLarge")
s1.showshirt()

s2 = Shirt()
s2.showshirt()

del s1
del s2