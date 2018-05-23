#/usr/bin/python
# Write a program to accept pattern and string from user & count the occurences of the given
# pattern in the string.

import re

def main():
	string = input("enter the string : ")
	pattern = input("enter the pattern : ")
	count = re.findall(pattern,string)
	print ("count of {} in {} is : {}".format(pattern,string,len(count)))

if __name__ == '__main__':
	main()