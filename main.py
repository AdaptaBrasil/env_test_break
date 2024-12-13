import math

add = lambda x, y: x + y
sub = lambda x, y: x - y
mul = lambda x, y: x * y
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
    print(add(1, 2))
    print(sub(1, 2))
    print(mul(1, 2))
    print(div(1, 2))
    print(sqrt(4))
    print(pow(2, 3))

if __name__ == "__main__":
    main()