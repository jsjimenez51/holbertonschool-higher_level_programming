#!/usr/bin/python3.4
if __name__ == "__main__":
    from hidden_4 import *
    for names in dir():
        if names[:2] != "__":
            print("{}".format(names))
