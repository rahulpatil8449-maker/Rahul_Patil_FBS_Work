# Write a program to reverse the list.

n = int(input("Enter no. of elements in the list: "))
li = []

for i in range(n):
    ele = int(input("Enter the elements in the list: "))
    li.append(ele)

print("The Original List is:", li)

rev = []
for i in range(len(li) - 1, -1, -1):
    rev.append(li[i])

print("The Reversed List is:", rev)