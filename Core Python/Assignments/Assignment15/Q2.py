# Create a class Product with members as pid,pname,price and quantity .Add following methods: 
# d. Constructor (Support both parameterized and parameterless) 
# e. Destructor 
# f. ShowBook

class Product:

    def __init__(self, pid = 102, pname = "Phone", price = 56000, quantity = 50):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity

    def __del__(self):
        print("Destructor Called.")

    def showproduct(self):
        print("Product ID:", self.pid)
        print("Name of the Product:", self.pname)
        print("Price of the Product:", self.price)
        print("Quantity of the Product:", self.quantity)

p1 = Product(101, "Cups", 99, 60)
p1.showproduct()

p2 = Product()
p2.showproduct()

del p1
del p2