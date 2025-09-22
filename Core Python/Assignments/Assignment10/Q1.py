# Write a program to find sum of all elements of list

n = int(input("Enter no. of elements: "))
li = []

for i in range(n):
    ele = int(input("Enter the element: "))
    li.append(ele)

sum = 0
for i in ele:
    sum +=i

print("The Sum of the elements in the list will be:", sum)