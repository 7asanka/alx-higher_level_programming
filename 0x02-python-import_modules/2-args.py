#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) == 2:
        arguments = "argument"
    else:
        arguments = "arguments"

    if len(argv) <= 1:
        print("0 arguments.")
    else:
        print(f"{len(argv) - 1} {arguments}:")
        for index in range(1, len(argv)):
            print(f"{index}: {argv[index]}")
