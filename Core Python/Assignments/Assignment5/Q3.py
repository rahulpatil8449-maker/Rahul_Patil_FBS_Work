num = int(input("Enter the number of passengers: "))
ticket_price = float(input("Enter the price of the ticket: "))

total = 0

for i in range(1, num + 1):
    age = int(input(f"Enter the age of the passenger {i}: "))

    if(age < 12):
        fare_price = ticket_price * 30 / 100
    elif(age > 59):
        fare_price = ticket_price * 50 / 100
    else:
        fare_price = ticket_price

    print(f"The Price of the ticket of the passenger {i} will be: {fare_price}.")
    total = total + fare_price

print(f"The Total cost of all the passengers will be: {total}.")