#!/usr/bin/python3
def print_last_digit(number):
    lastdig = number % 10
    if number < 0:
        lastdig = 10 - lastdig
    print(lastdig, end="")
    return lastdig
