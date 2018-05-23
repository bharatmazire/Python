#!/usr/bin/python

#Write a program to accept pattern and string from user & check if given pattern is present at the begining of the string.

import re

def main():
	string = input("enter the string : ")
	pattern = input("enter the pattern to search at start of string : ")

	if re.match(pattern,string):
		print ("{} present at starting of {}".format(pattern,string))
	else:
		print ("pattern not present at starting ... ")
	
if __name__ == '__main__':
	main()
