# Write a program to find sum of digits using recursion.

def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + sum_of_digits(n // 10)

num = int(input("Enter number: "))

if num < 0:
    print("Enter positive number.")
else:
    sum = sum_of_digits(num)
    print(f"The sum of digits of {num} is: {sum}")
