#!/usr/bin/env python3

# Created By: Amara Tie

# Date: May 13, 2025

# This is a calculator program


def calculator(num1_float, num2_float, operation_str):
    if operation_str == "/":
        return num1_float / num2_float
    if operation_str == "%":
        return num1_float % num2_float
    if operation_str == "*":
        return num1_float * num2_float
    if operation_str == "+":
        return num1_float + num2_float
    if operation_str == "-":
        return num1_float - num2_float


def main():
    # Ask User for a two numbers and an operator
    num1_str = input("Enter a  number :")
    num2_str = input("Enter a second number :")
    operation_str = input("Choose an operator (/,%,*,+,-) :")
    print("")

    # Try Catch num1 & 2 as string to float
    try:
        num1_float = float(num1_str)
        num2_float = float(num2_str)
        # Check operator and calculate the answer
        if operation_str == "/":
            answer = calculator(num1_float, num2_float, operation_str)
            print("{} / {} = {}".format(num1_float, num2_float, answer))

        if operation_str == "%":
            answer = calculator(num1_float, num2_float, operation_str)
            print("{} % {} = {}".format(num1_float, num2_float, answer))

        if operation_str == "*":
            answer = calculator(num1_float, num2_float, operation_str)
            print("{} * {} = {}".format(num1_float, num2_float, answer))

        if operation_str == "+":
            answer = calculator(num1_float, num2_float, operation_str)
            print("{} + {} = {}".format(num1_float, num2_float, answer))

        if operation_str == "-":
            answer = calculator(num1_float, num2_float, operation_str)
            print("{} - {} = {}".format(num1_float, num2_float, answer))

    except Exception:
        print("This is not a number")
    finally:
        print("Thanks for playing!")


if __name__ == "__main__":
    main()
