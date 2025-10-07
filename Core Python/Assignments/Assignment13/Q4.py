# Python Program to Generate a Dictionary that Contains Numbers (between 1 and n) in the Form (x,x*x).

n = int(input("Enter the size of the dictionary: "))

square_dict = {}

for x in range(1, n + 1):
    square_dict[x] = x * x

print("The Squared Dictionary will be:", square_dict)