n = 5

for i in range(1, n + 1):
    p = 1
    for j in range(i, n):
        print(" ", end = " ")

    for j in range(i):
        print(p, end = " ")
        p += 1

    for j in range(i - 1):
        print(p, end =" ")
        p += 1

    print()