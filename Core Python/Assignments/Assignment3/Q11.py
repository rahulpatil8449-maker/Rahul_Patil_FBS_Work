## Accept age of five people and also per person ticket amount and then calculate total 
## amount to ticket to travel for all of them based on following condition :
## a. Children below 12 = 30% discount
## b. Senior citizen (above 59) = 50% discount
## c. Others need to pay full.


ticket_price = float(input("Enter the price of the ticket: "))
amount = 0

for i in range(5):
    age = int(input(f"Enter the age of {i} person: "))

    if(age < 12):
        fare = ticket_price * 30/100
    elif(age > 59):
        fare = ticket_price * 50/100
    else:
        fare = ticket_price

    amount = amount + fare

print("The total amount of ticket to travel all persons will be:", amount)