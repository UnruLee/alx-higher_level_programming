#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    l = len(sys.argv)
    n = l - 1
    v = (sys.argv)

    if n == 0:
        print("{} arguments".format(n), end='.\n')
    elif n == 1:
        print("{} argument".format(n), end=':\n')
        print("{}:".format(n), v[n])
    else:
        print("{} arguments".format(n), end=':\n')
        for q in range(n):
                print("{}: {}".format(q + 1, v[q + 1]))
