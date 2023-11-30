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


def to_base(number, base):
    if not isinstance(number, int) and not isinstance(number, float):
        raise ValueError("Number must be an integer or float.")
    if not isinstance(base, int) or base < 2 or base > 36:
        raise ValueError("Base must be an integer between 2 and 36.")

    integer_part = int(abs(number))
    decimal_part = abs(number) - integer_part
    integer_result = ""

    # Перевод целой части числа
    while integer_part > 0:
        remainder = integer_part % base
        if remainder < 10:
            integer_result = str(remainder) + integer_result
        else:
            integer_result = chr(remainder + 55) + integer_result
        integer_part //= base

    result = integer_result

    # Перевод десятичной части числа (если она есть)
    if decimal_part > 0:
        result += "."
        precision = 15  # Количество знаков после запятой
        while decimal_part > 0 and precision > 0:
            decimal_part *= base
            digit = int(decimal_part)
            if digit < 10:
                result += str(digit)
            else:
                result += chr(digit + 55)
            decimal_part -= digit
            precision -= 1

    if number < 1:
        result = '0' + result
    if number < 0:
        result = "-" + result

    return result

operations = {
    '+': plus,
    '-': minus,
    '*': multiply,
    '/': divide,
    '%': module,
    '^': pow,
}
