#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import *
    from sys import argv

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    operator = argv[2]


    if operator == "+":
        op = add(a, b)
    elif operator == "-":
        op = sub(a, b)
    elif operator == "*":
        op = mul(a, b)
    elif operator == "/":
        op = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{} {} {} = {}".format(a, operator, b, op))
