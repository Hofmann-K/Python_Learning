'''
Milestone 1, Lesson 3: Challenge, create a simple calcultator
'''

# Prompt the user for a number until they enter a valid one
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))  # Allow decimals for flexibility
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Prompt the user for a valid operation symbol
def get_operation():
    valid_ops = ['+', '-', '*', '/']
    while True:
        op = input("Enter an operation (+, -, *, /): ")
        if op in valid_ops:
            return op
        print("Invalid operation. Try again.")

# Perform calculation based on operation
def calculate(num1, num2, op):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2

# Main
num1 = get_number("Enter the first number: ")
num2 = get_number("Enter the second number: ")
op = get_operation()

result = calculate(num1, num2, op)
print(f"\nResult: {num1} {op} {num2} = {result}")
