p = int(input("Enter the principle amount: "))
r = int(input("Enter the rate of interest: "))
t = int(input("Enter the time taken: "))

A = p * (1 + r/100) ** t
CI = A - p

print("The Compound interest will be:", CI)