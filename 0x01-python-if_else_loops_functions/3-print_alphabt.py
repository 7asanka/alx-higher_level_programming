#!/usr/bin/python3
for letter in range(97, 123):
    if "{:c}".format(letter) not in 'eq':
        print("{:c}".format(letter), end="")
