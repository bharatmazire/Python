#!/usr/bin/python

def main():
    decimal = input("enter the decimal value : ")
    decimal = int(decimal)
    print ("binary value of {} is : {}".format(decimal,bin(decimal)[2::]))

if __name__ == '__main__':
    main()
