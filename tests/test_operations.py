# В тесте test_operations.py

from unittest.mock import patch
from operations import compute, operations


@patch('operations.plus', return_value=30)
def test_compute_plus(mock_plus):
    result = compute(10, 20, '+')
    assert result == 30
    mock_plus.assert_called_once_with(10, 20)


@patch('operations.minus', return_value=10)
def test_compute_minus(mock_minus):
    result = compute(20, 10, '-')
    assert result == 10
    mock_minus.assert_called_once_with(20, 10)


@patch('operations.divide', return_value=2)
def test_compute_divide(mock_divide):
    result = compute(20, 10, '/')
    assert result == 2
    mock_divide.assert_called_once_with(20, 10)


@patch('operations.multiply', return_value=200)
def test_compute_multiply(mock_multiply):
    result = compute(20, 10, '*')
    assert result == 200
    mock_multiply.assert_called_once_with(20, 10)


@patch('operations.module', return_value=0)
def test_compute_module(mock_module):
    result = compute(20, 10, '%')
    assert result == 0
    mock_module.assert_called_once_with(20, 10)


@patch('operations.pow', return_value=20**10)
def test_compute_pow(mock_pow):
    result = compute(20, 10, '^')
    assert result == 20**10
    mock_pow.assert_called_once_with(20, 10)
