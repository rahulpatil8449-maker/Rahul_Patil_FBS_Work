# Write a program to find sum of following series using recursive functions:
# i. 1! + 2! + 3! + 4! +….. + n! 
# Note : For fact and sum two recursive functions

def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n - 1)

def sum_of_series(n):
    if n == 0:
        return 0
    return fact(n) + sum_of_series(n - 1)

n = int(input("Enter the value of n: "))
print("The Sum of series will be:", sum_of_series(n))
