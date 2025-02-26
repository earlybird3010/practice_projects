import operator

def print_options():
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

def calculator():
    print('Welcome Great Master! I am Eniac, your personal assistant. Please choose a service from the options below:')
    print()
    while True:
        print_options()
        try:
            choice = int(input())

            if choice == 1:
                calc('+', ['first summand', 'second summand'])
            elif choice == 2:
                calc('-', ['minuend', 'subtrahend'])
            elif choice == 3:
                calc('*', ['multiplier', 'multiplicand'])
            elif choice == 4:
                calc('/', ['dividend', 'divisor'])
            elif choice == 5:
                print("Goodbye Master! Your humble servant, Eniac, awaits to serve you next time.")
                break
            else:
                print("Invalid input option! Please try again.")
        except ValueError:
            print("Invalid option! Please choose again")
        print()

def func(operator_sign):
    """Return the corresponding function of the operator_sign"""
    opsign_operator = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }

    return opsign_operator[operator_sign]

def get_var_input(input):
    """Get a variable's value from the input"""
    while True:
        try: 
            result = float(input)
            break
        except ValueError:
            print('Invalid input! Please try again.')
    
    return result
    
def calc(operator_sign, variable_names):
    """Prompting and present calculation based on OPERATOR_SIGN and VARIABLE_NAMES"""

    print(f'Please enter the {variable_names[0]}: ')
    first = get_var_input(input())
    print(f'Please enter the {variable_names[1]}: ')
    second = get_var_input(input())
    
    operator_func = func(operator_sign)

    #Division by 0 handling
    if operator_sign == '/' and second == 0:
        print('Invalid input! You cannot divide a number by 0. Please try again.')
    else:
        print(f'The result of {first} {operator_sign} {second} is {operator_func(first, second)}')
    
calculator()