#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    argc = len(argv) - 1
    if argc != 3:
        print("Usage: {:s} <a> <operator> <b>".format(argv[0]))
        exit(1)
        a, operator, b = argv[1], argv[2], argv[3]
        a, b = int(a), int (b)
        if operator == '+':
            func = add
        elif operator == '-':
            func = sub
        elif operator == '*':
            func = mul
        elif operator == '/':
            func = div

        else:
            print("Unknown operator. Available operators: +, -, *, and /")
            exit(1)
            result = func(a, b)
            print("{:d} {:s} {:d} = {:d}".format(a, operator, b, result))
