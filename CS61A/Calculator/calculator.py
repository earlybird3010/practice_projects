import operator, math

invalid_option_msg = 'Invalid option! Please choose a valid option.'
invalid_input_msg = 'Invalid input! Please choose a valid number.'
invalid_args_msg = 'Invalid arguments! Please try again.'
invalid_save_options = 'Invalid option! Please choose Y or N.'
exit_to_menu_msg = 'Going back to main menu!'

prev_calc_results = []

goodbye_frames = [
    """
     GGGGG   OOOOO   OOOOO   DDDDDD    BBBBB   Y   Y   EEEEE
    G        O   O   O   O   D     D   B    B    Y Y    E
    G  GG    O   O   O   O   D     D   BBBBB      Y     EEEE
    G   G    O   O   O   O   D     D   B    B     Y     E
     GGGG    OOOOO   OOOOO   DDDDDD    BBBBB     Y     EEEEE
    """
]


#################
# Options_dicts #
#################
main_menu = {1: 'Standard operations', 2: 'Advanced math operations', 3: 'Math constants', 4: 'Exit'}
standard_operators_menu = {1: 'Addition', 2: 'Subtraction', 3: 'Multiplication', 4: 'Division', 5: 'Exponentiation',
6: 'Modulo', 7: 'Back'}
advanced_math_operators_menu = {1: 'sin', 2: 'cos', 3: 'tan', 4: 'cot', 5: 'asin', 6: 'acos', 7: 'atan', 8: 'Logarithm',
9: 'n-th root', 10: 'Back'}
constants_menu = {1: 'e', 2: 'pi', 3: 'Back'}
history_menu = {1: 'View', 2: 'Edit', 3: 'Back'}


####################
# Printing options #
####################
def print_options(options): 
    """Print a list of options from OPTIONS dictionary and return the exit code, i.e, the key of Exit or Back"""
    exit_code = None
    for option_num in options:
        print(f'{option_num}. {options[option_num]}')
        if options[option_num] == 'Exit' or options[option_num] == 'Back':
            exit_code = option_num
    
    return exit_code

def print_main_menu():
    """Print the a list of categories of computations and return the exit code"""
    return print_options(main_menu)

def print_standard_operators():
    """Print a list of standard operations and return the exit code"""
    return print_options(standard_operators_menu)

def print_advanced_math_operators():
    """Print a list of mathematical functions and return the exit code"""
    return print_options(advanced_math_operators_menu)

def print_constants():
    """Print a list of mathematical constants and return the exit code"""
    return print_options(constants_menu)

def print_history():
    """Print a list of options to manage the previous computational results"""
    return print_history(history_menu)
    

############################
# Run computation sessions #
############################
def run_sessions(session_name):
    """Execute the session based on SESSION_NAME"""
    while True:
        exit_code = session_infos[session_name]['print']()
        choice = int(get_user_input('Please choose a number from the available options: ', 
                                lambda x: x.isnumeric() and int(x) in session_infos[session_name]['menu'], 
                                invalid_option_msg))
        
        print()
        if choice == exit_code and session_name == 'main':
            print('Goodbye Great Master! Your humble servanr, Eniac, awaits for your next requests.')
            for frame in goodbye_frames:
                print(frame)
            break
        elif choice == exit_code:
            print(exit_to_menu_msg)
            break
        else:
            computation_choice = session_infos[session_name]['menu'][choice]
            session_infos[session_name]['run'](computation_choice)
        
        print()
        

def run_standard_computation(computation_choice):
    """Run a standard computation"""
    if computation_choice == 'Addition':
        calc_operations('+', ['first summand', 'second summand'])
    elif computation_choice == 'Subtraction':
        calc_operations('-', ['minuend', 'subtrahend'])
    elif computation_choice == 'Multiplication':
        calc_operations('*', ['multiplier', 'multiplicand'])
    elif computation_choice == 'Division':
        calc_operations('/', ['dividend', 'divisor'])
    elif computation_choice == 'Exponentiation':
        calc_operations('^', ['base', 'power'])
    elif computation_choice == 'Modulo':
        calc_operations('%', ['dividend', 'divisor'])

def run_advanced_math_computation(computation_choice):
    """Run an advanced math computation"""
    trig_names = ['sin', 'cos', 'tan', 'cot', 'asin', 'acos', 'atan']
    if computation_choice in trig_names:
            calc_operations(computation_choice, ['angle'])
    elif computation_choice == 'Logarithm':
            calc_operations('log', ['anti-algorithm', 'base'])
    elif computation_choice == 'n-th root':
            calc_operations('n-th root', ['degree', 'radicand'])

def run_constant(computation_choice):
    """Run the sessions that prints out constant values"""
    print(f'{computation_choice} = {constant(computation_choice)}')
                    
def run_history():
    return

def run_main_menu(computation_choice):
    """Open the session associated with COMPUTATION_CHOICE"""
    if computation_choice == 'Standard operations':
        run_sessions('standard_operators')
    elif computation_choice == 'Advanced math operations':
        run_sessions('advanced_math_operators')
    elif computation_choice == 'Math constants':
        run_sessions('constants')

session_infos = {'standard_operators': 
                 {'print': print_standard_operators, 'menu': standard_operators_menu, 'run': run_standard_computation}, 
                'advanced_math_operators': 
                {'print': print_advanced_math_operators, 'menu': advanced_math_operators_menu, 'run': run_advanced_math_computation}, 
                'constants': {'print': print_constants, 'menu': constants_menu, 'run': run_constant},
                'main': {'print': print_main_menu, 'menu': main_menu, 'run': run_main_menu},
                'history': {'print': print_history, 'menu': history_menu, 'run': run_history}
                   }

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
def get_user_input(msg, condition, error_msg):
    """Keep asking a user for input using MSG until CONDITION is met"""
    usr_input = input(msg)

    while not condition(usr_input):
        print(error_msg)
        usr_input = input(msg)
    
    return usr_input


def get_var_input(variable_name):
    """Get a variable's value in float from the user for VARIABLE_NAME"""
    def is_number(s):
        """Return True if string S can be converted to a float or int, False otherwise"""
        try:
            return float(s)
        except ValueError:
            return False
        
    msg = f'Please enter the {variable_name}: '
    usr_input = get_user_input(msg, is_number, invalid_input_msg)
    return float(usr_input)

###############
# Computation #
###############
    
def calc_operations(operator_sign, variable_names):
    """Present calculation of standard and advanced 
     math operations based on OPERATOR_SIGN and VARIABLE_NAMES using the inputs from the
     users"""
    
    variables = [get_var_input(variable_name) for variable_name in variable_names]

    correspondence_func = operators_func(operator_sign)

    if is_invalid_arguments(operator_sign)(*variables):
        print(invalid_args_msg)
        return

    computation_result = correspondence_func(*variables)
    output_msg = None

    if len(variable_names) == 1:
        output_msg = f'{operator_sign}({variables[0]}) = {computation_result}'
    elif operator_sign == 'log':
        output_msg = f'The logarithm of {variables[0]} with respect to base {variables[1]} is {computation_result}'
    elif operator_sign == 'n-th root':
        output_msg = f'The {variables[0]}-th root of {variables[1]} is {computation_result}'
    elif len(variable_names) == 2:
        output_msg = f'{variables[0]} {operator_sign} {variables[1]} = {computation_result}'
    
    print(output_msg)
    #save(output_msg)

##########
# Saving #
##########

def save(result):
    """
    Prompt the user whether to save RESULT
    """
    usr_input = get_user_input('Do you want to save this result? (Y/N)', lambda x: x == 'Y' or x == 'N', invalid_save_options)
    if usr_input == 'Y':
        prev_calc_results = [result] + prev_calc_results
    
##############
# Calculator #
##############
def calculator():
    print('Welcome Great Master! I am Eniac, your personal assistant. Please choose an option below for your computation!')
    print()
    run_sessions('main')

calculator()