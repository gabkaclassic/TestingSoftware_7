def plus(a, b):
    return a + b


def minus(a, b):
    return a - b


def divide(a, b):
    if b == 0:
        raise ArithmeticError('Второй параметр не должен быть равен 0')
    return a / b


def multiply(a, b):
    return a * b


def pow(a, b):
    return a ** b


def module(a, b):
    if b == 0:
        raise ArithmeticError('Второй параметр не должен быть равен 0')
    return a % b


def parse(parameter, base=10):
    try:
        return int(parameter, base)
    except:
        return False


def compute(first, second, operation):
    if operation == '+':
        return plus(first, second)
    elif operation == '/':
        return divide(first, second)
    elif operation == '-':
        return minus(first, second)
    elif operation == '*':
        return multiply(first, second)
    elif operation == '%':
        return module(first, second)
    elif operation == '^':
        return pow(first, second)



operations = {
    '+': plus,
    '-': minus,
    '*': multiply,
    '/': divide,
    '%': module,
    '^': pow,
}
