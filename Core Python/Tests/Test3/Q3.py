n = int(input("Enter the number of employees: "))

sum_total = 0

for i in range(n):
    basic_sal = int(input("Enter the basic salary of an employee: "))
    if(basic_sal < 20000):
        da = 10/100 * basic_sal
        ta = 12/100 * basic_sal
        hra = 15/100 * basic_sal

        total_sal = basic_sal + da + ta + hra
        print(f"The Total salary of an Employee will be: {total_sal}.")
        
    else:
        da = 15/100 * basic_sal
        ta = 18/100 * basic_sal
        hra = 20/100 * basic_sal
        
        total_sal = basic_sal + da + ta + hra
        print(f"The Total salary of an Employee will be: {total_sal}.")

    sum_total = sum_total + total_sal 
print(f"The total salary of all employees will be: {sum_total}.")