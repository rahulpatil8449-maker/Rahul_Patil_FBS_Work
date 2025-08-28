cost_price = float(input("Enter the cost of the book: "))
discount = float(input("Enter the discount given on the book in percentage: "))
marked_price = float(input("Enter the marked/MRP of the book: "))

disc = discount/100 * marked_price
selling_price = marked_price - disc

print("The selling price of the book will be:", selling_price)