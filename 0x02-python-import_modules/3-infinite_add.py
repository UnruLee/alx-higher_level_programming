#!/usr/bin/python3
if __name__ == '__main__':
    import sys

    l = len(sys.argv)
    n = l - 1
    v = (sys.argv)

    v = 0
    while n > 0:
        v = v + n
        n = n - 1
    print("{}".format(v))
