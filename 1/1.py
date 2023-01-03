import math
operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')
number_1 = float(input('Enter your first number: '))
number_2 = float(input('Enter your second number: '))

if operation == '+':
    print('{} + {} = '.format(number_1, number_2))
    print(number_1 + number_2)

elif operation == '-':
    print('{} - {} = '.format(number_1, number_2))
    print(number_1 - number_2)

elif operation == '*':
    print('{} * {} = '.format(number_1, number_2))
    print(number_1 * number_2)

elif operation == '/':
    print('{} / {} = '.format(number_1, number_2))
    print(number_1 / number_2)

elif operation == 'sqrt':
    print('{} sqrt {} = '.format(number_1, number_2))
    print(number_1 sqrt number_2)

elif operation == 'sin':
    print('{} sin {} = '.format(number_1, number_2))
    print(number_1 / number_2)

elif operation == 'cos':
    print('{} cos {} = '.format(number_1, number_2))
    print(number_1 / number_2)

elif operation == 'tan':
    print('{} tan {} = '.format(number_1, number_2))
    print(number_1 / number_2)

elif operation == 'cot':
    print('{} cot {} = '.format(number_1, number_2))
    print(number_1 / number_2)

elif operation == 'factorial':
    print('{} factorial {} = '.format(number_1, number_2))
    print(number_1 / number_2)
else:
    print('You have not typed a valid operator, please run the program again.')