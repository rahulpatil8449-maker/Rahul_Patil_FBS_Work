def factorial(num):
    if(num == 0 or num == 1):
        return 1
    else:
        return num * factorial(num - 1)

num = int(input("Enter the number to find factorial of: "))

result = factorial(num)
print(f"The Factorial of {num} is {result}")