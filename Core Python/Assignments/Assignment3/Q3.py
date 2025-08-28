a1 = int(input("Enter the value of angle1: "))
a2 = int(input("Enter the value of angle2: "))
a3 = int(input("Enter the value of angle3: "))

sum = a1 + a2 + a3

if(sum == 180):
    print("The triangle is valid.")
else:
    print("The triangle is invalid.")