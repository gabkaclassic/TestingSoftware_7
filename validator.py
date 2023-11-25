from operations import operations, parse


def validate_all_parameters(
        first_base,
        second_base,
        first,
        second,
        operation
):
    errors = []

    if not validate_base(first_base):
        errors.append('Неизвестная СС для первого параметра')
    else:
        first_base = parse(first_base)

    if not validate_base(second_base):
        errors.append('Неизвестная СС для второго параметра')
    else:
        second_base = parse(second_base)

    first = validate_param(first, first_base)
    second = validate_param(second, second_base)
    valid_operation = validate_operation(operation)

    if not first:
        errors.append('Невалидный первый параметр')

    if not second:
        errors.append('Невалидный второй параметр')

    if not valid_operation:
        errors.append('Неизвестная математике операция')

    return first, second, errors


def validate_base(base):
    return base.isdigit()


def validate_param(param, base):
    return parse(param, base)


def validate_operation(operation):
    return operation in operations
