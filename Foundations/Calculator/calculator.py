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
            addition()
        elif choice == 2:
            subtraction()
        elif choice == 3:
            multiplication()
        elif choice == 4:
            division()
        else:
            print("Invalid option! Please try again!")
        print()
        print_options()
        choice = int(input())


def addition():
    print("Please enter the first summand: ")
    first = float(input())
    print("Please enter the second summand: ")
    second = float(input())
    print(f'The result of {first} + {second} is {first + second}')


def subtraction():
    print("Please enter the minuend: ")
    first = float(input())
    print("Please enter the subtrahend: ")
    second = float(input())
    print(f'The result of {first} - {second} is {first - second}')

def multiplication():
    print("Please enter the multiplier: ")
    first = float(input())
    print("Please enter the multiplicand: ")
    second = float(input())
    print(f'The result of {first} * {second} is {first * second}')

def division():
    print("Please enter the dividend: ")
    first = float(input())
    print("Please enter the divisor: ")
    second = float(input())
    print(f'The result of {first} / {second} is {first / second}')

calculator()