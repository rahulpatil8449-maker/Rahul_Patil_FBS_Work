area = int(input("The area of one wall is:"))

cost_int = int(input("Enter the interior painting cost per unit area: "))
cost_ext = int(input("Enter the exterior painting cost per unit area: "))

interior_cost = 8 * area * cost_int
print("The cost for the whole interior area of the wall is:", interior_cost)

exterior_cost = 7 * area * cost_ext
print("The cost for the whole exterior area of the wall is:", exterior_cost)

total_cost = interior_cost + exterior_cost
print("The Total cost will be:", total_cost)

