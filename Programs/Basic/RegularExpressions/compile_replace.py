#!/usr/bin/python

import re

def work_on_file(fd):
	line = 'a'
	
	pattern = input("enter the pattern to replace : ")
	regex_object = re.compile(pattern)
	replace = input("enter to data replace : ")
	c = eval(input("enter the count : "))
	
	count = 0

	new_to_write = ''

	while line != '' and count < c:
		line = regex_object.sub(replace,fd.readline())
		#print (line)
		new_to_write = new_to_write+line
		count +=1
	print (new_to_write)
	fd.close()
	return new_to_write

def write_to_file(new_to_write,file_name):
	fd = open(file_name,"a+")
	fd.seek(0,0)
	#print(fd.tell())

	print(fd.write(new_to_write))


	fd.close()


def main():
	file_name = input("enter the file name to open : ")
	fd = open(file_name)

	new_to_write =  work_on_file(fd)
	write_to_file(new_to_write,file_name)

if __name__ == '__main__':
	main()