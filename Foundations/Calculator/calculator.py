import operator

def print_options():
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

def calculator():
    print('Welcome Great Master! I am Eniac, your personal assistant. Please choose a service from the options below:')
    print_options()
    choice = int(input())

    while choice != 5:
        if choice == 1:
            calc('+', ['first summand', 'second summand'])
        elif choice == 2:
            calc('-', ['minuend', 'subtrahend'])
        elif choice == 3:
            calc('*', ['multiplier', 'multiplicand'])
        elif choice == 4:
            calc('/', ['dividend', 'divisor'])
        else:
            print("Invalid option! Please try again!")
        print()
        print_options()
        choice = int(input())

def func(operator_sign):
    """Return the corresponding function of the operation"""
    if operator_sign == '+':
        return operator.add
    elif operator_sign == '-':
        return operator.sub
    elif operator_sign == '*':
        return operator.mul
    elif operator_sign == '/':
        return operator.truediv
    
def calc(operator_sign, variable_names):
    print(f'Please enter the {variable_names[0]}: ')
    first = float(input())
    print(f'Please enter the {variable_names[1]}: ')
    second = float(input())
    operator_func = func(operator_sign)
    print(f'The result of {first} {operator_sign} {second} is {operator_func(first, second)}')


calculator()