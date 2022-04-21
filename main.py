import sys
from sympy import pdiv
from sympy.parsing.sympy_parser import parse_expr

def main():
    print("Enter your first Polynomial")
    print("Example: 3*x**2 + 5*x + 2*y")
    firstPolynom = input()
    print("Enter your second Polynomial")
    secondPolynom = input()
    
    arg = input("What you want to do? ('+','-' ,'*' ,'/' ): ")

    p1 = parse_expr(firstPolynom)
    p2 = parse_expr(secondPolynom)

    result = None
    if(arg == "+"):
        result = Add(p1, p2)
    elif(arg == "-"):
        result = Sub(p1, p2)
    elif(arg == "*"):
        result = Sub(p1, p2)
    elif(arg == "/"):
        result = Sub(p1, p2)
    else:
        print("Incorect input")

    if(result != None):
        print("Result: ")
        print(result)
        print("\n")
    else:
        print("Some Error\n")

def Add(first, second):
    return first + second

def Sub(first, second):
    return first - second

def Mul(first, second):
    return first * second

def Dev(first, second):
    return pdiv(first, second)


if __name__ == '__main__':
    sys.exit(main())