# Write a program to find the second largest element in the list.

n = int(input("Enter the no. of elements in the list: "))
l = []

for i in range(n):
    ele = int(input("Enter elements in the list: "))
    l += [ele]

print("Original List is:", l)

if(l[0] > l[1]):
    largest = l[0]
    second = l[1]
else:
    largest = l[1]
    second = l[0]

for i in range(n):
    if(l[i] > largest):
        second = largest
        largest = l[i]
    elif(l[i] > second and l[i] != largest):
        second = l[i]

print("The Second Largest element in the list is:", second)