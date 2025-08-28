num = int(input("Enter a three digit number: "))

n1 = num // 100
n2 = (num // 10) % 10
n3 = num % 10

sum = n1 + n2 + n3

print("The sum of the three digit number will be:", sum)