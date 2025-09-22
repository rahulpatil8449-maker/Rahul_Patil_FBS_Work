# Write a program to create a new list from existing list which contains cube of each number of list.

n = int(input("Enter no. of elements: "))
l = []

for i in range(n):
    ele = int(input("Enter the elements: "))
    l += [ele]

print("The Original List is:", l)

li = []
for i in l:
    li += [i ** 3]

print("The New List after the cube of each element in the existing list will be:", li)