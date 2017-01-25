#!/usr/bon/python

# Write a program to accept pattern and string from user & check if given
# pattern is present at the end of the string.

import re

string = input("enter the string : ")
pattern = input("enter the pattern to search at end of string : ")

pattern_1 = pattern[::-1]
string_1 = string[::-1]
if re.match(pattern_1,string_1):
	print ("present")
else:
	print ("not present ")