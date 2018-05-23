#!/usr/bin/python

# preblem statement : write a program to open pcap file and then cheack in that file whether (user input ) required file 
#					  present in .pcap file or not

import os

def main():
	file_name = input("enter the .pcap file ")
	os.system('tcpick -C -yP -r '+file_name+' > a')
	
	fd = open("a")
	rd = fd.read()

	key_Word = input("enter the input to cheack wheter is present in file or not : ")

	if key_Word in rd:
		print ("given string present in file")
	else:
		print ("not present")

	fd.close()
	
if __name__ == '__main__':
	main()
