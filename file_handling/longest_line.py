#!/usr/bin/python

# Write a function input_stats that accepts a file name as a parameter and that reports the longest line in the file.

def len_all(fd):
	length = 0
	line = "q"
	while line != '':
		line = fd.readline()
		if len(line) > length:
			length = len(line)
	return length

def show_line(fd,length):
	line = "q"
	while line != '':
		line = fd.readline()
		if len(line) == length:
			print (line)

def main():
	filename = input("enter the file name to open : ")
	fd = open(filename,"r")
	
	length = len_all(fd)
	fd.close()
	fd = open(filename,"r")
	print ("the longest line in file is/are : ")
	show_line(fd,length)


if __name__ == '__main__':
	main()