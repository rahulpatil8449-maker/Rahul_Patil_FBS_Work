##  Write a program find reverse of a number

def count_digit(num):
    count = 0
    while num > 0:
        num = num // 10
        count += 1

    return count

def sum_of_power(num, digits):
    rev = 0
    for i in range(digits):
        rem = num % 10
        num = num // 10
        rev = (rev * 10) + rem

    return rev

def reverse_digit(num):
    digits = count_digit(num)
    rev = sum_of_power(num, digits)

    return rev

num = int(input("Enter the number: "))
print(reverse_digit(num))
