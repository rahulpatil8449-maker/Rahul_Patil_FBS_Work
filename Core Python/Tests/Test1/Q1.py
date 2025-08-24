l= int(input("Enter the length of rectangle:"))
b= int(input("Enter the breadth of rectangle:"))
r= float(input("Enter the radius of the circle:"))

rect_area= l * b
circle_area= (3.14 * r * r)/2

rect_peri= 2 * l + b
circle_peri= 3.14 * r

print("Area of the Rectangle is:", rect_area)
print("Area of the Circle is:", circle_area)

print("Perimeter of the Rectangle is:", rect_peri)
print("Perimeter of the Circle is:", circle_peri)

fig_area = rect_area + circle_area
fig_peri = rect_peri + circle_peri

print("The Area of the given figure is:", fig_area)

print("The Perimeter of the given figure is:", fig_peri)
