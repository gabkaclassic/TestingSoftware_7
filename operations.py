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
    except Exception as e:
        print(e)
        raise e


def compute(first, second, operation, result_base=10):
    result = 0

    if operation == '+':
        result = plus(first, second)
    elif operation == '/':
        result = divide(first, second)
    elif operation == '-':
        result = minus(first, second)
    elif operation == '*':
        result = multiply(first, second)
    elif operation == '%':
        result = module(first, second)
    elif operation == '^':
        result = pow(first, second)

    return to_base(result, result_base) or '0'


def to_base(digit, base):
    result = ''

    while digit > 0:
        result += str(digit % base)
        digit //= base

    return result[::-1]


operations = {
    '+': plus,
    '-': minus,
    '*': multiply,
    '/': divide,
    '%': module,
    '^': pow,
}
