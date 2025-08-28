side1 = int(input("Enter one side of the triangle: "))
side2 = int(input("Enter second side of the triangle: "))
side3 = int(input("Enter third side of the triangle: "))

if(side1 > 0 and side2 > 0 and side3 > 0):
    if(side1 == side2 == side3):
        print("This is an Equilateral Traingle.")
    elif(side1 == side2 or side2 == side3 or side1 == side3):
        print("This is an Isosceles Triangle.")
    else:
        print("This is an Scalene Triangle.")
else:
    print("This is an invalid triangle.")