#!/usr/bin/python

# problem statements : accept string and replace duplicate with * having 1 st as it  is

string = input("Enter the string : ")
print("after operation is :  {}".format(string[0]+string[1:].replace(string[0],"*")))