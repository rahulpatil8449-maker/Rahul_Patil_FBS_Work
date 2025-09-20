# Write a program to find factorial using recursion.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter number: "))

if num < 0:
    print("Enter positive number.")
else:
    result = factorial(num)
    print(f"The factorial of {num} is: {result}")
