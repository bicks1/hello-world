""" We're making a calculator!
Sophia Bick; 8/31/2022"""


# define function before main program
# this is in a different domain than main program; n1 doesn't exist in main

def plus(n1, n2):
    s = int(n1) + int(n2)
    return s


def minus(n1, n2):
    m = int(n1) - int(n2)
    return m


def multiply(n1, n2):
    u = int(n1) * int(n2)
    return u


def divide(n1, n2):
    d = int(n1) / int(n2)
    return d


if __name__ == '__main__':
    running = True
while running:
    # ask to enter the two numbers and operator
    num1 = input('Enter your first number or press q to quit:\n')
    if num1 == 'q':
        running = False
        print('You have exited the program.')
        break
    else:
        num2 = input('Enter your second number:\n')
        op = input('What is your operation [+, -, /, *]\n')
        print('Your first number = [{0}]\nYour second number = |{1}|'.format(num1, num2))
        print('Your operator is [{0}]'.format(op))

    # if operator is [+, -, /, *]
    if op == '+':
        my_sum = plus(num1, num2)
        print(my_sum)
    if op == '-':
        my_minus = minus(num1, num2)
        print(my_minus)
    if op == '/':
        my_divide = divide(num1, num2)
        print(my_divide)
    if op == '*':
        my_multiply = multiply(num1, num2)
        print(my_multiply)
