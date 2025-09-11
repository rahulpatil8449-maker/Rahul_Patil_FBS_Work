##  Write a program to reverse three-digit number.

num = int(input("Enter 3-digit number: "))
rev = 0
temp = num

while temp > 0:
    rem = temp % 10
    rev = rev * 10 + rem
    temp = temp // 10

print(f"The {num} after reversing will be: {rev}.")