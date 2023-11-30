from validator import validate_all_parameters, validate_param, validate_operation, validate_base


def test_valid_dec_parameters():
    first, second, result_base, errors = validate_all_parameters('10', '2', '10', '100', '10', '+')
    assert not errors
    assert first == 100
    assert second == 2

def test_valid_hex_parameters():
    first, second, result_base, errors = validate_all_parameters('16', '16', '10', '100', '10', '+')
    assert not errors
    assert first == 256
    assert second == 16


def test_valid_bin_parameters():
    first, second, result_base, errors = validate_all_parameters('2', '2', '10', '100', '10', '+')
    assert not errors
    assert first == 4
    assert second == 2


def test_valid_oct_parameters():
    first, second, result_base, errors = validate_all_parameters('8', '8', '10', '100', '10', '+')
    assert not errors
    assert first == 64
    assert second == 8


def test_invalid_first_base():
    first, second, result_base, errors = validate_all_parameters('abc', '2', '10', '100', '10', '+')
    assert 'Неизвестная СС для первого параметра' in errors
def test_invalid_base():
    assert not validate_base('1')
    assert not validate_base('adf')
    assert not validate_base('334')

def test_valid_base():
    assert validate_base('2')
    assert validate_base('16')

def test_invalid_param():
    assert not validate_param('1aa', 4)
    assert not validate_param('2', 1)
    assert not validate_param('3', 2)
    assert not validate_param('78293', 2)

def test_valid_param():
    assert validate_param('12', 3)
    assert validate_param('2', 16)
    assert validate_param('AB34', 16)
    assert validate_param('18', 9)


def test_valid_operation():
    assert validate_operation('+')
    assert validate_operation('-')
    assert validate_operation('*')
    assert validate_operation('/')
    assert validate_operation('^')
    assert validate_operation('%')
def test_invalid_operation():
    assert validate_operation('12')
    assert validate_operation('$')
    assert validate_operation('<*>')
    assert validate_operation('0')

def test_invalid_second_base():
    first, second, result_base, errors = validate_all_parameters('10', '2ыва', '10', '100', '10', '+')
    assert 'Неизвестная СС для второго параметра' in errors


def test_invalid_first_param():
    first, second, result_base, errors = validate_all_parameters('10', '2', '10', 'abc', '10', '+')
    assert 'Невалидный первый параметр' in errors

def test_invalid_second_param():
    first, second, result_base, errors = validate_all_parameters('10', '2', '10', '1', '10sdf', '+')
    assert 'Невалидный второй параметр' in errors


def test_invalid_result_base():
    first, second, result_base, errors = validate_all_parameters('10', '2', 'sdf', '1', '10sdf', '+')
    assert 'Неизвестная СС для результата' in errors


def test_invalid_operation():
    first, second, result_base, errors = validate_all_parameters('10', '2', '10', '100', '10', 'invalid')
    assert 'Неизвестная математике операция' in errors
