side1 = int(input("Enter one side of the triangle: "))
side2 = int(input("Enter second side of the triangle: "))
side3 = int(input("Enter third side of the triangle: "))

if(side1 > 0 and side2 > 0 and side3 > 0):
    if(side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2):
        print("The Triangle is valid.")
    else:
        print("The triangle is invalid.")
else:
    print("Enter positive value for the sides of triangle.")
