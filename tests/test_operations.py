from unittest.mock import patch
from operations import compute, to_base


@patch('operations.plus', return_value=30)
def test_compute_plus(mock_plus):
    result = compute(10, 20, '+')
    assert result == '30'
    mock_plus.assert_called_once_with(10, 20)

def test_to_base():
    result = to_base(88*7, 33)
    assert result == 'IM'
    result = to_base(88*7, 10)
    assert result == '616'
    result = to_base(88*7, 2)
    assert result == '1001101000'


@patch('operations.minus', return_value=10)
def test_compute_minus(mock_minus):
    result = compute(20, 10, '-')
    assert result == '10'
    mock_minus.assert_called_once_with(20, 10)


@patch('operations.divide', return_value=2)
def test_compute_divide(mock_divide):
    result = compute(20, 10, '/')
    assert result == '2'
    mock_divide.assert_called_once_with(20, 10)


@patch('operations.multiply', return_value=200)
def test_compute_multiply(mock_multiply):
    result = compute(20, 10, '*')
    assert result == '200'
    mock_multiply.assert_called_once_with(20, 10)


@patch('operations.module', return_value=0)
def test_compute_module(mock_module):
    result = compute(20, 10, '%')
    assert result == '0'
    mock_module.assert_called_once_with(20, 10)


@patch('operations.pow', return_value=20**10)
def test_compute_pow(mock_pow):
    result = compute(20, 10, '^')
    assert result == str(20**10)
    mock_pow.assert_called_once_with(20, 10)

@patch('operations.pow', return_value=20**10)
def test_result_base_bin(mock_pow):
    result = compute(20, 10, '^', 2)
    assert result == '10010101000000101111100100000000000000000000'
    mock_pow.assert_called_once_with(20, 10)

@patch('operations.pow', return_value=20**10)
def test_result_base_hex(mock_pow):
    result = compute(20, 10, '^', 16)
    assert result == '9502F900000'
    mock_pow.assert_called_once_with(20, 10)

@patch('operations.pow', return_value=20**10)
def test_result_base_tree(mock_pow):
    result = compute(20, 10, '^', 3)
    assert result == '1100020221020012120110211021'
    mock_pow.assert_called_once_with(20, 10)
