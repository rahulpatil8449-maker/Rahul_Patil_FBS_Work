# Create a class Product with members as pid,pname,price and quantity .Add following methods: 
# e. Constructor (Support both parameterized and parameterless) 
# f. Destructor 
# g. ShowBook 
# h. Add static member discount. 
# i. Provide methods for applying discount on price of product.

class Product:
    discount = 0

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
        print("\n")

    def cal_discount(self):
        disc = self.price * Product.discount / 100
        self.price = self.price - disc

p1 = Product(101, "Cups", 99, 60)
p1.showproduct()

p2 = Product()
p2.showproduct()

Product.discount = 10
print(f"Discount given on all Products is: {Product.discount} \n")

p1.cal_discount()
p2.cal_discount()

p1.showproduct()
p2.showproduct()

del p1
del p2