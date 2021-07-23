# Put your app in here.
from operations import add, sub, mult, div
from flask import Flask, request
app = Flask(__name__)


@app.route('/add')
def add_nums():
    """Returns the sum of two integers a and b"""
    a = request.args["a"]
    b = request.args["b"]
    return f"{add(int(a), int(b))}"


@app.route('/sub')
def sub_nums():
    """Returns the difference of two integers a and b"""
    a = request.args["a"]
    b = request.args["b"]
    return f"{sub(int(a), int(b))}"


@app.route('/mult')
def mult_nums():
    """Returns the product of two integers a and b"""
    a = request.args["a"]
    b = request.args["b"]
    return f"{mult(int(a), int(b))}"


@app.route('/div')
def div_nums():
    """Returns the quotient of two integers a and b if b is not zero"""
    a = request.args["a"]
    b = request.args["b"]
    if b is not "0":
        return f"{div(int(a), int(b))}"
    else:
        return "Cannot Divide By Zero!"


OPERATIONS = {
    'add': add,
    'sub': sub,
    'mult': mult,
    'div': div
}


@app.route('/math/<operation>')
def get_math(operation):
    a = request.args["a"]
    b = request.args["b"]
    operation = OPERATIONS.get(operation, "Not a Valid Operation")
    if operation is not "Not a Valid Operation":
        return f"{operation(int(a), int(b))}"
    elif operation is 'div':
        if b is not '0':
            return f"{div(int(a), int(b))}"
        else:
            return "Cannot Divide By Zero!"
    else:
        return operation
