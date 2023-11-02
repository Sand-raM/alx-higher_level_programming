#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    Leng = len(sys.argv)

    if Leng == 1:
        print("{} arguments.".format(Leng - 1))
    elif Leng == 2:
        print("{} argument:".format(Leng - 1))
    else:
        print("{} arguments:".format(Leng - 1))
        for i in range(1, Leng):
            print("{}: {}".format(i, sys.argv[i]))
