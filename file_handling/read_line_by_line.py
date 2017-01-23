#!/usr/bin/python
def main():
	file_name = input("enter file name with absolute path : ")
	fd = open(file_name)
	line = "a"
	while line != '':
		line = fd.readline()
		print (line)
if __name__ == '__main__':
	main()