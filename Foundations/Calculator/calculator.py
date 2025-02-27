import operator, math

invalid_option_msg = 'Invalid option! Please choose a valid option.'
invalid_input_msg = 'Invalid input! Please choose a valid number.'
invalid_args_msg = 'Invalid arguments! Please try again.'
exit_to_menu_msg = 'Going back to main menu!'
####################
# Printing options #
####################

def print_main_menu():
    """Print the a list of categories of computations and return the exit code"""
    print("1. Standard operations")
    print("2. Advanced math operations")
    print("3. Math constants")
    print("4. Exit")
    return 4

def print_standard_operators():
    """Print a list of standard operations and return the exit code"""
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponentiation")
    print("6. Modulo")
    print("7. Back to the main menu")
    return 7

def print_advanced_math_operators():
    """Print a list of mathematical functions and return the exit code"""
    print("1. sin")
    print("2. cos")
    print("3. tan")
    print("4. cot")
    print("5. asin")
    print("6. acos")
    print("7. atan")
    print("8. Logarithmic")
    print("9. nth root")
    print("10. Back to the main menu")
    return 10

def print_math_constants():
    """Print a list of mathematical constants and return the exit code"""
    print("1. e")
    print("2. pi")
    print("3. Back to the main menu")
    return 3

############################
# Run computation sessions #
############################

def run_standard_operators():
    """Run the sessions that perform standard operations"""
    while True:
        exit_code = print_standard_operators()
        try:
            choice = int(input())
            print()

            if choice == 1:
                calc_operations('+', ['first summand', 'second summand'])
            elif choice == 2:
                calc_operations('-', ['minuend', 'subtrahend'])
            elif choice == 3:
                calc_operations('*', ['multiplier', 'multiplicand'])
            elif choice == 4:
                calc_operations('/', ['dividend', 'divisor'])
            elif choice == 5:
                calc_operations('^', ['base', 'power'])
            elif choice == 6:
                calc_operations('%', ['dividend', 'divisor'])
            elif choice == exit_code:
                print(exit_to_menu_msg)
                break
            else:
                print(invalid_option_msg)
        except ValueError:
            print(invalid_option_msg)
        print()

def run_advanced_math_operators():
    """Run the sessions that perform standard operations"""
    while True:
        exit_code = print_advanced_math_operators()
        try:
            choice = int(input())
            print()

            if choice == 1:
                calc_operations('sin', ['angle'])
            elif choice == 2:
                calc_operations('cos', ['angle'])
            elif choice == 3:
                calc_operations('tan', ['angle'])
            elif choice == 4:
                calc_operations('cot', ['angle'])
            elif choice == 5:
                calc_operations('asin', ['angle'])
            elif choice == 6:
                calc_operations('acos', ['angle'])
            elif choice == 7:
                calc_operations('atan', ['angle'])
            elif choice == 8:
                calc_operations('log', ['anti-algorithm', 'base'])
            elif choice == 9:
                calc_operations('n-th root', ['degree', 'radicand'])
            elif choice == exit_code:
                print(exit_to_menu_msg)
                break
            else:
                print(invalid_option_msg)
        except ValueError:
            print(invalid_option_msg)
        print()

def run_constants():
    """Run the sessions that perform standard operations"""
    while True:
        exit_code = print_math_constants()
        try:
            choice = int(input())
            print()

            if choice == 1:
                print(f'e = {math.e}')
            elif choice == 2:
                print(f'pi = {math.pi}')
            elif choice == exit_code:
                print(exit_to_menu_msg)
                break
            else:
                print(invalid_option_msg)
        except ValueError:
            print(invalid_option_msg)
        print()

def calculator():
    print('Welcome Great Master! I am Eniac, your personal assistant. Please choose an option below for your computation!')
    print()
    while True:
        exit_code = print_main_menu()
        try:
            choice = int(input())
            print()

            if choice == 1:
                run_standard_operators()
            elif choice == 2:
                run_advanced_math_operators()
            elif choice == 3:
                run_constants()
            elif choice == exit_code:
                print("Goodbye Master! Your humble servant, Eniac, awaits to serve you next time.")
                break
            else:
                print(invalid_option_msg)
        except ValueError:
            print(invalid_option_msg)
        print()

###########################
# Operators and constants #
###########################
def operators_func(operator_sign):
    """Return the corresponding function of the operator_sign"""
    opsign_operator = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '^': math.pow,
        '%': operator.mod,
        'sin': math.sin,
        'cos': math.cos,
        'tan': math.tan,
        'cot': lambda x: 1 / math.tan(x),
        'asin': math.asin,
        'acos': math.acos,
        'atan': math.atan,
        'log': math.log,
        'n-th root': lambda degree, radicand: pow(radicand, 1 / degree)
    }

    return opsign_operator[operator_sign]

def is_invalid_arguments(operator_sign):
    """Return a function that returns True if some arguments for an operator
    corresponding to OPERATOR_SIGN is invalid"""
    invalid_args = {
        '/': lambda x, y: y == 0,
        '%': lambda x, y: y == 0,
        'tan': lambda x: math.isclose((x - math.pi / 2) % (2 * math.pi), 0) or math.isclose((x + math.pi / 2) % (2 * math.pi), 0),
        'cot': lambda x: x % math.pi == 0, 
        'asin': lambda x: -1 > x or x > 1,
        'acos': lambda x: -1 > x or x > 1,
        'log': lambda antilogarithm, base: base <= 0 or base == 1 or antilogarithm <= 0,
        'n-th root': lambda degree, radicand: degree == 0
    }
    
    if operator_sign not in invalid_args:
        return lambda *variables : False
    
    return invalid_args[operator_sign]


def constant(symbol):
    symbol_constant = {
        'pi': math.pi,
        'e': math.e
    }

    return symbol_constant[symbol]

###########################################
# Handling users' inputs for computation  #
###########################################
def get_var_input(variable_name):
    """Get a variable's value in float from the user for VARIABLE_NAME"""
    while True:
        print(f'Please enter the {variable_name}:')
        try:
            return float(input())
        except ValueError:
            print(invalid_input_msg)

    
def calc_operations(operator_sign, variable_names):
    """Present calculation of standard and advanced 
     math operations based on OPERATOR_SIGN and VARIABLE_NAMES using the inputs from the
     users"""
    
    variables = [get_var_input(variable_name) for variable_name in variable_names]

    correspondence_func = operators_func(operator_sign)

    if is_invalid_arguments(operator_sign)(*variables):
        print(invalid_args_msg)
    elif len(variable_names) == 1:
        print(f'{operator_sign}({variables[0]}) = {correspondence_func(*variables)}')
    elif operator_sign == 'log':
        print(f'The logarithm of {variables[0]} with respect to base {variables[1]} is {correspondence_func(*variables)}')
    elif operator_sign == 'n-th root':
        print(f'The {variables[0]}-th root of {variables[1]} is {correspondence_func(*variables)}')
    elif len(variable_names) == 2:
        print(f'{variables[0]} {operator_sign} {variables[1]} = {correspondence_func(*variables)}')
        
calculator()