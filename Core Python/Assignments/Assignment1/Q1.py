m1 = int(input("Enter the marks of one subject:"))
m2 = int(input("Enter the marks of two subject:"))
m3 = int(input("Enter the marks of third subject:"))
m4 = int(input("Enter the marks of fourth subject:"))
m5 = int(input("Enter the marks of fifth subject:"))

total = m1 + m2 + m3 + m4 + m5
per = (total / 500) * 100

print("The percentage of a student for his/her 5 subject marks:", per, "%")