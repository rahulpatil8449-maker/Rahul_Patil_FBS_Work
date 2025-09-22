# Write a program to print list after removing even numbers.

n = int(input("Enter no. of elements: "))
l = []

for i in range(n):
    ele = int(input("Enter the element: "))
    l += [ele]

print("The Original List will be:", l)

li = []
for i in l:
    if (i % 2 != 0):
        li += [i]

print("The List after removing even numbers will be:", li)