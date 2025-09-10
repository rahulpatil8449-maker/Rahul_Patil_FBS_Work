##  Write a program to find sum of digits of a number.

def sum_of_digits(num):
    total = 0
    while num > 0:
        rem = num % 10
        total += rem
        num = num // 10
    return total
num = int(input("Enter the number: "))
print("The Sum of the Digits will be:")
print(sum_of_digits(num))