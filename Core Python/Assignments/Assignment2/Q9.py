####swapping of two numbers without using third variable

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
print(f"Before swapping the value of a is {a} and value of b is {b}")

a = a + b
b = a - b 
a = a - b

print(f"After swapping the value of a will be {a} and the value of b will be {b}.")