# Write a program to find sum of n numbers using recursion.

def sum_of_numbers(n):
    if n == 1:
        return 1
    else:
        return n + sum_of_numbers(n - 1)

n = int(input("Enter number: "))

if n <= 0:
    print("Enter a positive number.")
else:
    sum = sum_of_numbers(n)
    print("The sum of n numbers will be:", sum)
