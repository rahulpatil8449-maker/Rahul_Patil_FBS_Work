num = int(input("Enter the value of num: "))

for i in range(num):
    for j in range(num):
        if(i == 0 or i == num - 1 or j == num - i - 1):
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()