##  Write a program to check if given 3 digit number is a palindrome or not.

num = int(input('Enter the number: '))
rev = 0
temp = num

while temp > 0:
    rem = temp % 10
    rev = rev * 10 + rem
    temp = temp // 10

if(rev == num):
    print(f"{num} is palindrome.")
else:
    print(f"{num} is not palindrome.")
    