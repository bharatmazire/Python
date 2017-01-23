#!/usr/bin/python

# WAP to accept file name , ip file will be any file. accpet any string and add that string to startr of accepted file

import os
import re

def mode(file_name,string):
	e = file_name.find('.')
	etx =  file_name[e+1:]
	if etx == 'c' or 'java' or 'cpp':
		string = "//"+string
		return file_name,string
	elif etx == 'py':
		string = "#"+string
		return file_name,string
	else:
		string = "this is comment >> "+string
		return file_name,string

	

def main():
	file_name 	= input("enter the file name to which you want to prepend string : ")
	string 		= input("enter the string (to prepend ) : ")

	file_name , string = mode(file_name,string)

	old_fd 		= open(file_name)
	file_data 	= old_fd.read()
	old_fd.close()

	new_fd 		= open("new","a+")
	
	new_fd.write(string)
	new_fd.write("\n")
	new_fd.write(file_data)
	
	new_fd.close()

	#os.system("mv $file_name old_file")
	os.system("rm -rf "+file_name)
	os.system("mv new "+file_name)

	os.system("cat "+file_name)


if __name__ == '__main__':
 	main()