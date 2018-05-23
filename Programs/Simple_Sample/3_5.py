#!/usr/bin/python

def chk(x):
    if x % 3 == 0 and x % 5 == 0:
        print ("xy")
    elif x % 3 == 0:
        print ("x")
    elif x % 5 == 0:
        print ("y")
    else:
        print (x)

ran = eval(input("enter range : "))
[x for x in range(ran) if (chk(x))]