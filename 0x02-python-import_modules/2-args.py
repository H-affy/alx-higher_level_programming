#!/usr/bin/python3

if __name__ == '__main__':
    import sys

    count = len(sys.argv) - 1
    if count == 0:
        print("0 aarguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))
    for i in range(count):
        print("{}: {}".format(i + 1, sus.argv[i + 1]))