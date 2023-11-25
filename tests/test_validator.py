from validator import validate_all_parameters


def test_valid_dec_parameters():
    first, second, errors = validate_all_parameters('10', '2', '100', '10', '+')
    assert not errors
    assert first == 100
    assert second == 2

def test_valid_hex_parameters():
    first, second, errors = validate_all_parameters('16', '16', '100', '10', '+')
    assert not errors
    assert first == 256
    assert second == 16


def test_valid_bin_parameters():
    first, second, errors = validate_all_parameters('2', '2', '100', '10', '+')
    assert not errors
    assert first == 4
    assert second == 2


def test_valid_oct_parameters():
    first, second, errors = validate_all_parameters('8', '8', '100', '10', '+')
    assert not errors
    assert first == 64
    assert second == 8


def test_invalid_first_base():
    first, second, errors = validate_all_parameters('abc', '2', '100', '10', '+')
    assert 'Неизвестная СС для первого параметра' in errors

def test_invalid_second_base():
    first, second, errors = validate_all_parameters('10', '2ыва', '100', '10', '+')
    assert 'Неизвестная СС для второго параметра' in errors


def test_invalid_first_param():
    first, second, errors = validate_all_parameters('10', '2', 'abc', '10', '+')
    assert 'Невалидный первый параметр' in errors

def test_invalid_second_param():
    first, second, errors = validate_all_parameters('10', '2', '1', '10sdf', '+')
    assert 'Невалидный второй параметр' in errors


def test_invalid_operation():
    first, second, errors = validate_all_parameters('10', '2', '100', '10', 'invalid')
    assert 'Неизвестная математике операция' in errors
