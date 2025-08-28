m1 = int(input("Enter the marks of subject1: "))
m2 = int(input("Enter the marks of subject2: "))
m3 = int(input("Enter the marks of subject3: "))
m4 = int(input("Enter the marks of subject4: "))
m5 = int(input("Enter the marks of subject5: "))

percentage = (m1 + m2 + m3 + m4 + m5)/500 * 100
print("The percentage scored is:", percentage)

if(percentage >=90):
    print("Student scored Grade A+")
elif(percentage >= 80):
    print("Student scored Grade A")
elif(percentage >= 70):
    print("Student scored Grade C")
elif(percentage >= 50):
    print("Student scored grade D")
else:
    print("Student got F.")
    