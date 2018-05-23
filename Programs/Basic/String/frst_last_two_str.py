#!/usr/bin/python

# problem statement : accept input string and create new strirng as first and last 2 elements of accepted strig.
# eg : input string : hello
#      output string: helo

string = input("Enter the string as initial input : ")
new_string = string[0:2]+string[-2:]
print("old string was {}  and new is '{}'  ".format(string,new_string))
