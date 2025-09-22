# Write a program to find maximum and minimum element in a list.

n = int(input("Enter no. of elements in the list: "))
li = []

for i in range(n):
    ele = int(input("Enter the elements in the list: "))
    li += [ele]

print("The Original List is:", li)

max = li[0]
min = li[0]

for i in li:
    if(i > max):
        max = i
    elif(i < min):
        min = i

print("The maximum element in the list is:", max)
print("The minimum element in the list is:", min)