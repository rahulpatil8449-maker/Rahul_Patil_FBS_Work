cost_price = float(input("Enter the cost price: "))
selling_price = float(input("Enter the selling price: "))

if(selling_price > cost_price):
    print("It's Profit.")
elif(cost_price > selling_price):
    print("It's Loss.")
else:
    print("It's no profit no loss.")