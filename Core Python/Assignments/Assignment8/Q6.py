# Fibonacci series using Function

def fibonacci(num):
    a = 0
    b = 1

    for i in range(1 , num + 1):
        #print(a, end = " ")
        a, b = b, a + b     #0, 1 = 1, 0 + 1  1
        print(a, end = " ")     #printing the series

    #return a
num = int(input("Enter the n term: "))      #Accepting value from user
fibonacci(num)      #Function Call