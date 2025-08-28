basic_sal = int(input("Enter the basic salary: "))

hra = 10/100 * basic_sal
ta = 12/100 * basic_sal
da = 15/100 * basic_sal

total_sal = basic_sal + hra + ta + da

print("The total salary will be: ",total_sal)