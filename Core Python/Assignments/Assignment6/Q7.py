n = 6

for i in range(1, n):
    p = 65
    for j in range(i, n):
        print(" ", end =" ")

    for j in range(i):
        print(chr(p), end = " ")
        p +=1

    for j in range(i - 1):
        print(chr(p), end = " ")
        p += 1

    print()