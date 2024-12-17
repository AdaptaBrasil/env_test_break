from src.util.utilities import add, sub, mul, div, sqrt, pow
from src.myparser.info import print_versions

def main():
    # Import info
    print_versions()
    print("\nMath operations: ")
    print(f'add(1, 2) = {add(1, 2)}')
    print(f'sub(1, 2) = {sub(1, 2)}')
    print(f'mul(1, 2) = {mul(1, 2)}')
    print(f'div(1, 2) = {div(1, 2)}')
    print(f'sqrt(4) = {sqrt(4)}')
    print(f'pow(2, 3) = {pow(2, 3)}')


if __name__ == "__main__":
    main()