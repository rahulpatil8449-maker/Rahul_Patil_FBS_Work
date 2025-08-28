days = int(input("Enter the days: "))

yrs = days // 365
days = days % 365

weeks = days // 7

d = days % 7

print(f"The days after conversion will be {yrs} years, {weeks} weeks and {d} days")