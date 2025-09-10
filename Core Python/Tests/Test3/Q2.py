num = int(input("Enter the value for num: "))

fact = 1
sum = 0

for i in range(1, num + 1):
    fact *= i          
    sum += i / fact      

print("The Sum of series will be:", sum)