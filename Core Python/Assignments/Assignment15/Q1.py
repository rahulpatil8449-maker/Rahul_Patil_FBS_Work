# Create a class Book with members as bid,bname,price and author.Add following methods: 
# a. Constructor (Support both parameterized and parameterless) 
# b. Destructor 
# c. ShowBook

class Book:

    def __init__(self, bid = 102, bname = "TITANIC", price = 1049, author = "Walter Lord"):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author

    def __del__(self):
        print("Destructor called.")

    def showbook(self):
        print("Bid:", self.bid)
        print("Book Name:", self.bname)
        print("Price of the Book:", self.price)
        print("Author of the Book:", self.author)

b1 = Book(101, "Romeo & Juliet", 899, "William Shakespeare")
b1.showbook()

b2 = Book()
b2.showbook()

del b1
del b2