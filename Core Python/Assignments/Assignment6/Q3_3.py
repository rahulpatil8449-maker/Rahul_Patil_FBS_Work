#### Printing Pascal pattern using Function

def pascaltriangle_pattern(num):
    for i in range(1, num + 1):
        for j in range(i, num + 1):
            print(" ", end = "")

        val = 1                             # Taking starting value for the triangle - 1
        for j in range(1, i + 1):
            print(val, end = " ")
            val = val * (i - j) // j        # Formula to the PASCAL TRIANGLE

        print()

num = int(input("Enter the number of rows: "))
pascaltriangle_pattern(num)