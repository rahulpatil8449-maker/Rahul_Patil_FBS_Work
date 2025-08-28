####swapping of two number using third variable

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
print(f"Before swapping the value of a is {a} and value of b is {b}")

temp = a
a = b
b = temp

print(f"After swapping the value of a will be {a} and the value of b will be {b}.")