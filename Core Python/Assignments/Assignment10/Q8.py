# Write a program to create a duplicate of an existing list. It should not point to same list.

n = int(input("Enter no. of elements: "))
list = []

for i in range(n):
    ele = int(input("Enter the elements: "))
    list += [ele]

print("The Original List is:", list)

duplicate_list = []

for i in range(n):
    duplicate_list += [list[i]]

print("The Duplicate List will be:", duplicate_list)

list[0] = -1

print("After changing [0] index value -")
print("The Original List is:", list)
print("The Duplicate List is:", duplicate_list)