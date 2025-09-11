##  WAP to check if given number Strong Number.
## Strong Number is a number in which the sum of factorial of digits = the number itself
## Example - 145=1!+4!+5!=1+24+120=145

num = int(input("Enter the number: "))
sum = 0
temp = num

while temp > 0:
    rem = temp % 10
    fact = 1

    for i in range(1, rem + 1):
        fact *= i

    sum += fact
    temp = temp // 10

if(sum == num):
    print(f"{num} is a Strong Number.")
else:
    print(f"{num} is not a Strong Number.")