
#Basic calculator program in python
#This program performs basic arithmetic operations: addition, subtraction, multiplication, and division.
#It takes two numbers and an operator as input from the user and returns the result of the operation.

user_input = input("Enter two numbers and an operator (e.g., 2 3 +): ")
print(user_input)  # Print the user input for debugging purposes
num1, num2, operator = user_input.split()
num1 = float(num1)  # Convert the first number to float
num2 = float(num2)  # Convert the second number to float
supported_operators = ['+', '-', '*', '/']  # List of supported operators
result = None  # Initialize result variable
print("Supported operators: +, -, *, /")  # Print supported operators
if operator not in supported_operators:  # Check if the operator is supported
    print("Error: Unsupported operator. Please use one of the following: +, -, *, /")
else:
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
    if result is not None:
        print(f"The result of {num1} {operator} {num2} is: {result}")
