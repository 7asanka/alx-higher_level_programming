#!/usr/bin/python3
if __name__ == "__main__":
    import add_0

    add = add_0.add
    a = 1
    b = 2
    print("{} + {} = {res}".format(a, b, res=add(a, b)))
