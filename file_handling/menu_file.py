#!/usr/bin/python

#menu driven approach to file program
import io

import read_line_by_line as rlbl
# '''
# #!/usr/bin/python
# def main():
# 	file_name = input("enter file name with absolute path : ")
# 	fd = open(file_name)
# 	line = "a"
# 	while line != '':
# 		line = fd.readline()
# 		print (line)
# if __name__ == '__main__':
# 	main()

# '''


import alternate_line_read as alr
# '''
# #!/usr/bin/python
# # read alternate lines of file
# def main():
# 	file_name = input("enter absolute path file name : ")
# 	fd = open(file_name)
# 	line = "a"
# 	while line != '':
# 		line = fd.readline()
# 		print (line)
# 		line = fd.readline() 
# if __name__ == '__main__':
# 	main()
# '''


def ten_alter():
	filename = input("enter the file name (absolute path): ")
	
	f1 = io.FileIO(filename,"r")
	#f2 = io.FileIO(filename,"r")
	#f1 = open(filename)
	#f2 = open(filename)

	print("for 1st ")
	line = "a"
	while line != b'':
		line = f1.read(10)
		print (line)
		f1.seek(10,1)
	#f1.close()

	print("for 2nd")
	line2 = "a"
	#f1 = io.FileIO(filename,"r")
	f1.seek(0,0)
	while line2 != b'':
		f1.seek(10,1)
		line2 = f1.read(10)
		print(line2)
	f1.close()
	''' use this logic and complete the function 
def alt_ten():
	x = fd.read(10)
	while x != b'':
		print (x)
		fd.seek(10,1)
		x = fd.read(10)

'''

def f_to_d():
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

def main():
	choice = 0
	while choice != 6:
		choice = eval(input("\n1.read line by line \n2.read alternate line \n3.play with file number \n4.ten_alter \n5.file_to_dict \n6.end : "))
		if choice == 1:
			rlbl.main()
		elif choice == 2:
			alr.main()
		elif choice == 3:
			fd = open("menu_file.py")
			print ("no. of menu_file.py when file is open process is {}".format(fd.fileno()))
			fd = open("read_line_by_line.py")
			print (fd.fileno())
			fd.close()
		elif choice == 4:
			ten_alter()
		elif choice == 5:
			f_to_d()
		else:
			for i in "thank you !!!":
				print (i)
				for j in range(100000):
					pass


if __name__ == '__main__':
	main()