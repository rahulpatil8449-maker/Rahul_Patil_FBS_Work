l = 50
b = 40
r = 20
cost_per_meter = 35

perimeter = 50 + 40 + 50 + 3.14 * 20    ##for 1 round of fencing
total_perimeter = 5 * perimeter         ##for 5 rounds of fencing
total_cost = 35 * total_perimeter

print("The perimeter of thte field is:", perimeter)
print("The total cost for fencing 5 times in the field will be:", total_cost)