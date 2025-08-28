num = int(input("Enter the number: "))

if(num > 0):
    if(num > 50):
        if(num > 100):
            print(f"{num} is greater than 100.")
        else:
            print(f"{num} is in between 51 to 100.")
    else:
        print(f"{num} is in between 0 to 50")
else:
    print(f"{num} is less than zero.")