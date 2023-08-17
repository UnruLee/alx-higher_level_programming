#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    length = len(sys.argv)
    n = length - 1
    v = sys.argv

    sum = 0
    for q in range(n):
        sum = sum + int(v[q + 1])
    print("{}".format(sum))
