import sys
from sympy import pdiv
from sympy.parsing.sympy_parser import parse_expr

def main():
    print("Enter your first Polynomial")
    print("Example: 3*x**2 + 5*x + 2*y")
    first_polynom = input()
    print("Enter your second Polynomial")
    second_polynom = input()
    
    arg = input("What you want to do? ('+','-' ,'*' ,'/' ): ")

    p1 = parse_expr(first_polynom)
    p2 = parse_expr(second_polynom)

    result = None
    if(arg == "+"):
        result = add(p1, p2)
    elif(arg == "-"):
        result = sub(p1, p2)
    elif(arg == "*"):
        result = mul(p1, p2)
    elif(arg == "/"):
        result = dev(p1, p2)
    else:
        print("Incorect input")

    if(result != None):
        print("Result: ")
        print(result)
        print("\n")
    else:
        print("Some Error\n")

def add(first, second):
    return first + second

def sub(first, second):
    return first - second

def mul(first, second):
    return first * second

def dev(first, second):
    return pdiv(first, second)


if __name__ == '__main__':
    sys.exit(main())