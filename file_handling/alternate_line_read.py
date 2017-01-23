#!/usr/bin/python
# read alternate lines of file
def main():
	file_name = input("enter absolute path file name : ")
	fd = open(file_name)
	line = "a"
	while line != '':
		line = fd.readline()
		print (line)
		line = fd.readline() 
if __name__ == '__main__':
	main()