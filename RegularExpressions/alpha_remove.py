#!/usr/bin/python

# WAP a program to accept alpha neumeric value and return only eumeric value from them 

import re

def main():
	value = input("enter the alpha neumeric value : ")
	new = re.sub('[a-zA-Z]','',value)
	print ("{} is value without alphabates ".format(new))

if __name__ == '__main__':
	main()