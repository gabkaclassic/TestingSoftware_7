from operations import operations, parse


def validate_all_parameters(
        first_base,
        second_base,
        result_base,
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

    if not validate_base(result_base):
        errors.append('Неизвестная СС для результата')
    else:
        result_base = parse(result_base)

    first = validate_param(first, first_base)
    second = validate_param(second, second_base)
    valid_operation = validate_operation(operation)

    if first is None:
        errors.append('Невалидный первый параметр')

    if second is None:
        errors.append('Невалидный второй параметр')

    if not valid_operation:
        errors.append('Неизвестная математике операция')

    return first, second, result_base, errors


def validate_base(base):
    return base.isdigit() and int(base) in range(2, 36)


def validate_param(param, base):
    try:
        return parse(param, base)
    except:
        return None


def validate_operation(operation):
    return operation in operations
