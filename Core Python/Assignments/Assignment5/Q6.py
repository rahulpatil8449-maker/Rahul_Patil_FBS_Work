print("The Prime Numbers from 1 to 100 are: ")

for num in range(2, 101):   # numbers from 2 to 100
    is_prime = True

    for i in range(2, num):   # check divisibility
        if num % i == 0:
            is_prime = False
            break

    else:
        print(num, end=" ")
