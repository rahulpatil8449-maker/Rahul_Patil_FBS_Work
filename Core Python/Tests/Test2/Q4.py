l = int(input("Enter the length of the wall: "))
b = int(input("Enter the breadth of the wall: "))
cost_area = float(input("Enter the cost for per square meter area: "))

area = l * b

total_area = 4 * area
total_cost = total_area * cost_area

print(f"The total area of four wall will be {total_area} square meters.")
print("The total cost of interior wall painting will be:", total_cost)