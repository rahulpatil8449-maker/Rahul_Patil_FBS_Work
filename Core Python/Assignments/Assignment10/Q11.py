# Write a program to print all numbers which are divisible by m and n in the list.

n = int(input("Enter the no. of elements: "))
l = []

for i in range(n):
        ele = int(input("Enter the elements: "))
        l += [ele]

print("Original List will be:", l)

m = int(input("Enter the number: "))
n = int(input("Enter the number: "))

li = []
for i in l:
        if(i % m == 0 and i % n == 0):
                li += [i]

print(f"The Elements in the List which are divisible by {m} and {n} are: {li}")