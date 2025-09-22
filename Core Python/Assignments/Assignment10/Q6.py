# Write a program to remove duplicates from the list.

n = int(input("Enter no. of elements: "))
l = []

for i in range(n):
    ele = int(input("Enter the elements: "))
    l += [ele]

print("The Original List is:", l)

new_li = []

for i in l:
    found = False

    for j in new_li:
        if(i == j):
            found = True
            break
    else:
        new_li += [i]

print("The New List with no duplicate elements in it will be:", new_li)