#!/usr/bin/python3

if __name__ == "__main__":
    """Prints the number of and list of its arguments."""
    from sys import argv

    count = len(argv) - 1
    if count == 0:
        print("{} arguments.".format(count))
    elif count == 1:
        print("{} argument:".format(count))
        print("1: Hello")
    else:
        print("{} arguments:".format(count))
        for i in range(count):
            print("{}: {}".format(i + 1, argv[i + 1]))
