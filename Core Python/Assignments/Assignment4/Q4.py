num = int(input("Enter a number: "))

fact = 1

for i in range(1, num + 1):
    fact = fact * i

print(f"The Factorial of {num} will be: {fact}")
