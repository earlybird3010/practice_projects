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
main_menu = {1: 'Standard operations', 2: 'Advanced math operations', 3: 'Math constants', 4: 'History', 5: 'Exit'}
standard_operators_menu = {1: 'Addition', 2: 'Subtraction', 3: 'Multiplication', 4: 'Division', 5: 'Exponentiation',
6: 'Modulo', 7: 'Back'}
advanced_math_operators_menu = {1: 'sin', 2: 'cos', 3: 'tan', 4: 'cot', 5: 'asin', 6: 'acos', 7: 'atan', 8: 'Logarithm',
9: 'n-th root', 10: 'Back'}
constants_menu = {1: 'e', 2: 'pi', 3: 'Back'}
history_menu = {1: 'View', 2: 'Delete', 3: 'Back'}

########################
# Options informations #
########################
trig_funcs = ['sin', 'cos', 'tan', 'cot', 'asin', 'acos', 'atan']
math_options_infos = {'Addition': ['+', ['first summand', 'second summand']],
                 'Subtraction': ['-', ['minuend', 'subtrahend']],
                 'Multiplication': ['*', ['multiplier', 'multiplicand']],
                 'Division': ['/', ['dividend', 'divisor']],
                 'Exponentiation': ['^', ['base', 'power']],
                 'Modulo': ['%', ['dividend', 'divisor']],
                 'Logarithm': ['log', ['anti_algorithm', 'base']],
                 'n-th root': ['n-th root', ['degree', 'radicand']]
                 }
for trig_func in trig_funcs:
    math_options_infos[trig_func] = [trig_func, ['angle']]

constants_options_infos = {'pi': math.pi, 'e': math.e}

history_options_infos = {'View': ['view_history', ['number of previous computations for viewing']], 
                         'Delete': ['delete_history', ['position of a previous computation for delete']]}

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
    return print_options(history_menu)
    

############################
# Run computation sessions #
############################
def run_sessions(session_name):
    """Execute the session based on SESSION_NAME"""
    while True:
        exit_code = session_infos[session_name]['print']()
        choice = get_user_input('Please choose a number from the available options: ', 
                                lambda x: x.isnumeric() and int(x) in session_infos[session_name]['menu'], 
                                invalid_option_msg, int)
        
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

def run_math_computation(computation_choice):
    """
    Run a math computation that matches COMPUTATION_CHOICE
    """
    computation_symbol = math_options_infos[computation_choice][0]
    variables_names = math_options_infos[computation_choice][1]
    
    calc_operations(computation_symbol, variables_names)

def run_constant(choice):
    """Run the sessions that prints out constant values based on COMPUTATION_CHOICE (the symbol of the constant)"""
    print(f'{choice} = {constants_options_infos[choice]}')
                    
def run_history(choice):
    option_symbol = history_options_infos[choice][0]
    variables_names = history_options_infos[choice][1]

    calc_history(option_symbol, variables_names)

def run_main_menu(computation_choice):
    """Open the session associated with COMPUTATION_CHOICE"""
    if computation_choice == 'Standard operations':
        run_sessions('standard_operators')
    elif computation_choice == 'Advanced math operations':
        run_sessions('advanced_math_operators')
    elif computation_choice == 'Math constants':
        run_sessions('constants')
    elif computation_choice == 'History':
        run_sessions('history')

session_infos = {'standard_operators': 
                 {'print': print_standard_operators, 'menu': standard_operators_menu, 'run': run_math_computation}, 
                'advanced_math_operators': 
                {'print': print_advanced_math_operators, 'menu': advanced_math_operators_menu, 'run': run_math_computation}, 
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
        'n-th root': lambda degree, radicand: pow(radicand, 1 / degree),
        'view_history': view_history,
        'delete_history': delete_history
    }

    return opsign_operator[operator_sign]

def view_history(prev_calculations_no):
    """
    Print the last PREV_CALCULATIONS_NO calculation, assuming PREV_CALCULATIONS_NO is a valid input
    """
    for i in range(prev_calculations_no):
        print(prev_calc_results[i])

def delete_history(pos):
    """
    Delete the POS-th most recent computation result from history, assuming POS is valid 
    """
    prev_calc_results.pop(pos - 1)


def is_invalid_arguments(operator_sign):
    """Return a function that returns True if some arguments for an operator
    corresponding to OPERATOR_SIGN is invalid"""
    invalid_args = {
        '/': lambda x, y: y == 0,
        '%': lambda x, y: y == 0,
        '^': lambda x, y: x == 0 and y == 0,
        'tan': lambda x: math.isclose((x - math.pi / 2) % (2 * math.pi), 0) or math.isclose((x + math.pi / 2) % (2 * math.pi), 0),
        'cot': lambda x: x % math.pi == 0, 
        'asin': lambda x: -1 > x or x > 1,
        'acos': lambda x: -1 > x or x > 1,
        'log': lambda antilogarithm, base: base <= 0 or base == 1 or antilogarithm <= 0,
        'n-th root': lambda degree, radicand: degree == 0,
        'view_history': lambda n: n < 0 or n > len(prev_calc_results),
        'delete_history': lambda pos: pos < 1 or pos > len(prev_calc_results)
    }
    
    if operator_sign not in invalid_args:
        return lambda *variables : False
    
    return invalid_args[operator_sign]

###########################################
# Handling users' inputs for computation  #
###########################################
def get_user_input(msg, condition, error_msg, return_form=str):
    """
    Keep asking a user for input using MSG until CONDITION is met, printing ERROR_MSG for invalid input on the way.
    Return the input in RETURN_FORM
    """
    usr_input = input(msg)

    while condition(usr_input) is False:
        print(error_msg)
        usr_input = input(msg)
    
    return return_form(usr_input)

#Verifying user's input functions
def is_float(s):
        """Return the number version of S if string S can be converted to a float or int, False otherwise"""
        try:
            return float(s)
        except ValueError:
            return False

def is_int(s):
    try:
        return int(s)
    except ValueError:
        return False
    
# Get different kinds of inputs
def get_float_input(variable_name):
    """Get a variable's value in float from the user for VARIABLE_NAME"""
    usr_input = get_user_input(f'Please enter the {variable_name}: ', is_float, invalid_input_msg, float)
    return usr_input

def get_int_input(variable_name):
    """Get a variable's value in int from the user for VARIABLE_NAME"""
    usr_input = get_user_input(f'Please enter the {variable_name}: ', is_int, invalid_input_msg, int)
    return usr_input

###############
# Computation #
###############
    
def calc_operations(operator_sign, variable_names):
    """Present calculation of standard and advanced 
     math operations based on OPERATOR_SIGN and VARIABLE_NAMES using the inputs from the
     users"""
    
    variables = [get_float_input(variable_name) for variable_name in variable_names]

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
    save(output_msg)

def calc_history(operator_sign, variables_names):
    """
    View or delete some previous calculations
    """
    variables = [get_int_input(variable_name) for variable_name in variables_names]

    correspondence_func = operators_func(operator_sign)

    if is_invalid_arguments(operator_sign)(*variables):
        print(invalid_args_msg)
        return
    
    correspondence_func(*variables)

##########
# Saving #
##########

def save(result):
    """
    Prompt the user whether to save RESULT
    """
    usr_input = get_user_input('Do you want to save this result? (Y/N)', lambda x: x == 'Y' or x == 'N', invalid_save_options)
    if usr_input == 'Y':
        global prev_calc_results #all names must refer to a same frame
        prev_calc_results = [result] + prev_calc_results
    
##############
# Calculator #
##############
def calculator():
    print('Welcome Great Master! I am Eniac, your personal assistant. Please choose an option below for your computation!')
    print()
    run_sessions('main')

calculator()