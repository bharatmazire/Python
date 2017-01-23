#!/usr/bin/python

# problem statement : accept two strigs and swap its initial two letters with each others 

str1 = input("enter 1st string : ")
str2 = input("enter 2nd string : ")

print("new words are : {} and {}".format(str2[0:2]+str1[2:], str1[0:2]+str2[2:]))
