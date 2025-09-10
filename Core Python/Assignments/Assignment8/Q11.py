##Armstrong Numbers are:- 153, 370, 371, 1634 and 1 to 9(all are armstrong numbers)

def digit_count(num):
    cnt = 0
    while(num > 0):
        num = num // 10
        cnt = cnt + 1
    
    return cnt

def sum_of_power(num, cnt):
    sum = 0
    while(num > 0):
        rem = num % 10
        sum = sum + (rem ** cnt)
        num = num // 10

    return sum

def is_armstrong(num):
    cnt = digit_count(num)
    sum = sum_of_power(num, cnt)
    if(sum == num):
        print(f"{num} is an Armstrong Number.")
    else:
        print(f"{num} is not an Armstrong Number.")

num = int(input("Enter the number: "))

is_armstrong(num)