import math

def add (x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    if y == 0:
        raise ValueError("Can't divide by zero")
    return x / y

def sqrt(x):
    if x < 0:
        raise ValueError("Can't take square root of negative number")
    return math.sqrt(x)

def pow(x, y):
    return x ** y
