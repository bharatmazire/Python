#!/usr/bin/python

# internal implementation of finditer

import re

def find_iter(stri,pattern):
	 i = 0
	 while patt in stri[i::]:
	 	a = re.search(pattern,stri[i::])
	 	print (a.start()+i , a.end()+i)
	 	i = a.end()+i

def main():
	stri = input("enter the string input : ")
	pattern = input("enter the pattern to match : ")

	find_iter(stri , pattern)

if __name__ == '__main__':
	main()