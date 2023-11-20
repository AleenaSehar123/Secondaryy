def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        raise ZeroDivisionError('Cannot divide by zero.')
    return n1 / n2

def calculator(n1, n2, operation):
    if operation == '+':
        return add(n1, n2)
    elif operation == '-':
        return subtract(n1, n2)
    elif operation == '*':
        return multiply(n1, n2)
    elif operation == '/':
        return divide(n1, n2)
    else:
        return "Invalid operand to perform!"

n1 = 12
n2 = 0
operation = '='

try:
    result = calculator(n1, n2, operation)
    print(result)
except ZeroDivisionError as e:
    print(e)