num = int(input("Enter the number: "))

sum = 0
temp = num
n = len(str(num))

while(temp > 0):
    d = temp % 10
    sum = sum + (d ** n)
    temp = temp // 10

if(sum == num):
    print(f"{num} is a Armstrong Number.")
else:
    print(f"{num} is not a Armstrong Number.")