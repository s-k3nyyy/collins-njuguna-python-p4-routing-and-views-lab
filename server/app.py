#!/usr/bin/env python3
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<parameter>')
def print_text(parameter):
    print(parameter)
    return parameter

@app.route('/count/<int:parameter>')
def count(parameter):
    result = ''
    for i in range(parameter):
        result += f'{i}\n'
    return result

@app.route('/math/<num1>/<operation>/<num2>')
def math(num1, operation, num2):
    if operation == '+':
        answer =str(int(num1) + int(num2))
    elif operation == '-':
        answer =str(int(num1) - int(num2))
    elif operation == '*':
        answer =str(int(num1) * int(num2))
    elif operation == 'div':
        answer =str(int(num1) / int(num2))
    elif operation == '%':
        answer =str(int(num1) % int(num2))
    else:
        return None
    return str(answer)
    
if __name__ == '__main__':
    app.run(port=5555, debug=True)
