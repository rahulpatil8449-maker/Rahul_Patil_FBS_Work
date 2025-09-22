# Write a program to create three lists of numbers, their squares and cubes.

n = int(input("Enter no. of elements: "))
list = []
list_square = []
list_cube = []

for i in range(n):
    ele = int(input("Enter the elements: "))
    list += [ele]
    list_square +=[ele ** 2]
    list_cube += [ele ** 3]

print("The Original List is:", list)
print("The List of square of all elements are:", list_square)
print("The List of cube of all elements are:", list_cube)