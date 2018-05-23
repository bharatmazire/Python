#!/usr/bin/python
import re

def main():
	string = input("enter the string : ")
	replaceTo = input("enter replace to string part : ")
	replaceBy = input("enter replace by string part : ")

	if replaceTo in string:
		new = re.sub(replaceTo,replaceBy,string)
		print ("new replaced string is : ",new)
	else:
		print ("{} is not present in {}",format(replaceTo,string))

if __name__ == '__main__':
	main()