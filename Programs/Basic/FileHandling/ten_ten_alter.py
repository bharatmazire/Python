#!/usr/bin/python

# write a code for accepting the filename from user and display the alternate 10-10 byte of the file and after that print the skipped byte

import io

def main():
	filename = input("enter the file name (absolute path): ")
	
	f1 = io.FileIO(filename,"r")
	f2 = io.FileIO(filename,"r")
	#f1 = open(filename)
	#f2 = open(filename)

	print("for 1st ")
	line = "a"
	while line != b'':
		line = f1.read(10)
		print (line)
		f1.seek(10,1)

	print("for 2nd")
	line2 = "a"
	while line2 != b'':
		f2.seek(10,1)
		line2 = f2.read(10)
		print(line2)

if __name__ == '__main__':
	main()