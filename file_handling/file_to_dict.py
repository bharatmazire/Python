#!/usr/bin/python

# accept file from user which is in form of <something_1>=<something_2>
# and convert it to dictonary form i.e. {something1 : something2 , ....} 
import io


def main():
	dict1 = {}
	filename = input("enter file name with absolute path : ")

	fd = open(filename)

	line = "a"

	while line != b'':
	
		line = fd.readline()
	
		if line == '':
			break
		i = line.index("=")
		
		key = line[0:i]
	#	print (key)
		
		value = line[i+1:-1]
	#	print (value)
		
		dict1[key] = value
	print ("dictonary is : ")
	print(dict1)

if __name__ == '__main__':
	main()