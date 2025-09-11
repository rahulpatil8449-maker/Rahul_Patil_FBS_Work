##  Write a program to accept an integer amount from user and tell minimum number of notes needed for representing that amount.
    
amount = int(input("Enter the amount from user: "))
notes = [500, 200, 100, 50, 20, 10, 5, 2, 1]
total = 0

for i in notes:
    total = total + amount // i
    amount %= i

print("The total number of required will be:", total)