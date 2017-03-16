#!/usr/bin/python
import os

def main():
	command = input("enter the command of which help you want : ")
	os.system("man "+command+"> file_one")

	fd = open("file_one")
	file = fd.read()
	fd.close()
	
	os.system ("rm -rf file_one")
	print (file)

if __name__ == '__main__':
	main()