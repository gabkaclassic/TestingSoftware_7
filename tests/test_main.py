import pytest
from flask import Flask
from main import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_home_redirect(client):
    response = client.get('/')
    assert response.status_code == 302

def test_calculator_page(client):
    response = client.get('/calculator')
    assert response.status_code == 200

def test_compute_valid_input(client):
    data = {
        "first": "10",
        "second": "20",
        "operation": "+"
    }
    response = client.post('/calculator', json=data)
    assert response.status_code == 200
    assert response.json['result'] == '30'


def test_compute_invalid_first(client):
    data = {
        "first": "abc",
        "second": "20",
        "operation": "+",
    }
    response = client.post('/calculator', json=data)
    assert response.status_code == 400
    assert 'errors' in response.json
    assert 'Невалидный первый параметр' in response.json['errors']


def test_compute_invalid_second(client):
    data = {
        "first": "2",
        "second": "ss",
        "operation": "+"
    }
    response = client.post('/calculator', json=data)
    assert response.status_code == 400
    assert 'errors' in response.json
    assert 'Невалидный второй параметр' in response.json['errors']
    
def test_compute_invalid_operation(client):
    data = {
        "first": "1",
        "second": "20",
        "operation": "+-"
    }
    response = client.post('/calculator', json=data)
    assert response.status_code == 400
    assert 'errors' in response.json
    assert 'Неизвестная математике операция' in response.json['errors']

    
def test_compute_invalid_first_base(client):
    data = {
        "first": "1",
        "second": "20",
        "operation": "+",
        'firstBase': '3e'
    }
    response = client.post('/calculator', json=data)
    assert response.status_code == 400
    assert 'errors' in response.json
    assert 'Неизвестная СС для первого параметра' in response.json['errors']

    
def test_compute_invalid_second_base(client):
    data = {
        "first": "1",
        "second": "20",
        "operation": "+",
        'secondBase': '3e'
    }
    response = client.post('/calculator', json=data)
    assert response.status_code == 400
    assert 'errors' in response.json
    assert 'Неизвестная СС для второго параметра' in response.json['errors']


def test_compute_invalid_params_amount_first(client):
    data = {
        "second": "20",
        "operation": "+",
    }
    response = client.post('/calculator', json=data)
    assert response.status_code == 400
    assert 'errors' in response.json
    assert 'Отсутствуют необходимые параметры' in response.json['errors']

def test_compute_invalid_params_amount_second(client):
    data = {
        "first": "20",
        "operation": "+",
    }
    response = client.post('/calculator', json=data)
    assert response.status_code == 400
    assert 'errors' in response.json
    assert 'Отсутствуют необходимые параметры' in response.json['errors']

def test_compute_invalid_params_amount_operation(client):
    data = {
        "first": "20",
        "second": "11",
    }
    response = client.post('/calculator', json=data)
    assert response.status_code == 400
    assert 'errors' in response.json
    assert 'Отсутствуют необходимые параметры' in response.json['errors']
def test_compute_invalid_result_base(client):
    data = {
        "first": "20",
        "second": "11",
        'operation': '+',
        'resultBase': 'asdfs',
    }
    response = client.post('/calculator', json=data)
    assert response.status_code == 400
    assert 'errors' in response.json
    assert 'Неизвестная СС для результата' in response.json['errors']

def test_compute_valid_result_base(client):
    data = {
        "first": "20",
        "second": "11",
        'operation': '+',
        'resultBase': '11',
    }
    response = client.post('/calculator', json=data)
    assert response.status_code == 200
    assert response.json['result'] == '29'



