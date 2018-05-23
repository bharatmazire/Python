#!/usr/bin/python


def main():
    a = []
    s = eval(input("enter the size of array : "))
    for i in range(0,s):
    	j = eval(input(">>>"))
    	a.append(j)
    print ("maximum is : ",max(a))

if __name__ == '__main__':
    main()
