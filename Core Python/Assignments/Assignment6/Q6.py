num = 5

for i in range(1, num + 1):
    for j in range(i, num + 1):
        print(" ", end = " ")

    for j in range(1, i+1):
        print(j, end = " ")
        
    for j in range(1, i):
        print(i + j, end = " ")

    print()