#!/usr/bin/python

import re

def read_file(fd):
	readed_file = fd.read()
	fd.close()
	return readed_file

def replace_pattern(readed_file):
	pattern = input("enter the pattern to replace : ")
	count = eval(input("enter the count to replace : "))
	new_replace = input("enter new replacement : ")
	if count <= len(re.findall(pattern,readed_file)):
		new_to_write = re.sub(pattern,new_replace,readed_file,count)
		print (new_to_write)
		return new_to_write
	else:
		print ("count invalid :")
		replace_pattern(readed_file)

def write_file(new_to_write,file_name):
	fd = open(file_name,"w")
	print (fd.write(new_to_write))
	fd.close()
	#fd = open(file_name)
	#print(fd.read())


def main():
	file_name = input("enter file name to open : ")

	fd = open(file_name)

	readed_file = read_file(fd)

	new_to_write = replace_pattern(readed_file)

	write_file(new_to_write,file_name)

if __name__ == '__main__':
	main()
