# Develop a simple calculator program that performs basic arithmetic operations (+, -, *, /) on two numbers provided by the user. The program should ask the user for the numbers and the operator. However, the program should handle the following exceptions:
# a. Invalid Number: If the user enters a number that is not valid, catch the exception and display an error message.
# b. Invalid Operator: If the user enters an operator other than "+", "-", "*", or "/", catch the exception and display an error message.
# c. Division by Zero: If the user tries to divide by zero, catch the exception and display an error message.
# Write a program that performs the requested arithmetic operation and handles the exceptions as described above.


try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    operators = input("Enter the Operator(+, -, *, /): ")

    if(operators == '+'):
        result = num1 + num2
    elif(operators == '-'):
        result = num1 - num2
    elif(operators == '*'):
        result = num1 * num2
    elif(operators == '/'):
        try:
            result = num1 / num2
        except ZeroDivisionError:
            print("Error = Division by Zero(0) is not allowed!!")
            result = None

    else:
        raise ValueError("Invalid Operator!! Use only these operators(+, -, *, /)")
    
    if(result is not None):
        print(f'Result = {num1} {operators} {num2} = {result}')

except ValueError as ve:
    print("Error:", ve)

except Exception as e:
    print("Unexpected Error:", e)