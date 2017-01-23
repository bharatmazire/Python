#!/usr/bin/python

# problem statement : accept input string and create new strirng as first and last 2 eleme=nts of accepted strig.

string = input("Enter the string as initial input : ")

new_string = string[0:2]+string[-2:]
print("old string was {}  and new is '{}'  ".format(string,new_string))