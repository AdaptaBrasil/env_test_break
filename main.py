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

def main():
    print(f'add(1, 2) = {add(1, 2)}')
    print(f'sub(1, 2) = {sub(1, 2)}')
    print(f'mul(1, 2) = {mul(1, 2)}')
    print(f'div(1, 2) = {div(1, 2)}')
    print(f'sqrt(4) = {sqrt(4)}')
    print(f'pow(2, 3) = {pow(2, 3)}')


if __name__ == "__main__":
    main()