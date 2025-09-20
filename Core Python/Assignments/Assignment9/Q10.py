# Write a program to reverse a number using recursion.

def reverse_num(num, rev=0):
    if num == 0:
        return rev
    else:
        return reverse_num(num // 10, rev * 10 + num % 10)

n = int(input("Enter number: "))
rev = reverse_num(n)

print("The Reversed number will be:", rev)