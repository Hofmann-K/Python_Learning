'''
Milestone 1, Lesson 3: Challenge, create a simple calcultator
'''

is_valid = False

while is_valid == False:
    try:
        user_num_1 = int(input("Please enter a number to perform a math operation on: "))
        is_valid = True
    except ValueError:
        print("Please enter a valid number (any non decimal integer)")

is_valid = False
while is_valid == False:
    try:
        user_num_2 = int(input("Please enter a second number to perform a math operation on: "))
        is_valid = True
    except ValueError:
        print("Please enter a valid number (any non decimal integer)")

is_valid = False
while is_valid == False:
    user_operation = input("Enter the symbol of the math operation you would like to perform (+, -, *, /): ")

    if (user_operation == '+' or '-' or '*' or '/'):
        is_valid = True
    else:
        user_operation = input("Operation not valid. Please enter a different one: ")

if user_operation == '+':
    output = user_num_1 + user_num_2
elif user_operation == '-':
    output = user_num_1 - user_num_2
elif user_operation == '*':
    output = user_num_1 * user_num_2
else:
    output = user_num_1 / user_num_2

print("Result:", output)