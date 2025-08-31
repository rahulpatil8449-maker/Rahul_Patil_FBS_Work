# Program to check special condition on a 3-digit number

num = int(input("Enter a 3-digit number: "))

# Extract digits
first = num // 100           # First digit
second = (num // 10) % 10    # Second digit
third = num % 10             # Third digit

# Check the condition
if (first == 2 * second) and (first * 2 == third):
    print("You have done it")
else:
    print("Condition not satisfied")
#