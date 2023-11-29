from flask import Flask, send_from_directory as static, jsonify, request, make_response as response, redirect, url_for
from operations import compute as calculate
from validator import validate_all_parameters as validate

app = Flask(__name__)


@app.route('/')
def home():
    return redirect(url_for('calculator'))


@app.route('/calculator', methods=['GET'])
def calculator():
    return static('pages', 'calculator.html')


@app.route('/calculator', methods=['POST'])
def compute():
    try:
        data = request.json
        first = data['first']
        second = data['second']
        first_base = data.get('firstBase', '10')
        second_base = data.get('secondBase', '10')
        result_base = data.get('resultBase', '10')
        operation = data['operation']
    except:
        return response(jsonify({'errors': ['Отсутствуют необходимые параметры']}), 400)

    first, second, result_base, errors = validate(
        first_base, second_base, result_base, first, second, operation
    )
    if errors:
        return response(jsonify({'errors': errors}), 400)

    try:
        result = calculate(first, second, operation, result_base)
    except Exception as e:
        return response(jsonify({'errors': [str(e)]}), 400)

    return response(jsonify({'result': result}), 200)


if __name__ == '__main__':
    app.run(debug=True)
