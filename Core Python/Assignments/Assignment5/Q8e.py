####  x - x2/3 + x3/5 - x4/7 + …. to n terms

num = int(input("Enter the number till you want to print the sum of series: "))
x = int(input("Enter the value of x: "))

total = 0

for i in range(1, num + 1):
    sum = (x ** i)/(2 * i) - 1

    if(i % 2 != 0):
        total += sum
        #print("The sum of the odd series :", total)
    else:
        total -= sum
        #print("The sum of the even series:", total)

#total = odd_sum - even_sum
print("The total sum of the series will be:", total)