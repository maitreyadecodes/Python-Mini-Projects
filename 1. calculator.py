# This code is a simple calculator that takes two numbers and an operator as input,
# performs the specified operation, and prints the result. It handles addition, subtraction,
# multiplication, and division, including error handling for division by zero and invalid operators.

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter an operator (+, -, *, /): ")

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2   
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."
else:
    result = "Error! Invalid operator."
print(f"The result is: {result}")
