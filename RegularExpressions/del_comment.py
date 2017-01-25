#!/usr/bin/python
import re
# this is comment

def main():
	file_name = input("enter the file_name : ")
	fd = open(file_name)
	readed_file = fd.read()
	new = re.sub('#.*',"",readed_file)
	fd.close()
	print (new)									# again commrnt

if __name__ == '__main__':
	main()
#this is also comment