#!/usr/bin/python

# write a program to accept 3 arguments (input, output filename, number of lines(n))
# and perform follwing opearation based on value of n : 
# if n = -1 :: copy all lines from input to output file 
# if n = 0  :: copy nothing from input to output file
# if n < -1 :: give the msg to user to give proper positive int value
# if n > 1  :: print n lines from input to output file 


def copy_all(fd,ffd):
	line = "a"
	while line != '':
		line = fd.readline()
		ffd.write(line)
	ffd.close()
	fd.close()

def read():
	fd = open("output.txt")
	line = "a"
	while line != '':
		line = fd.readline()
		print (line)
	fd.close()

def copy_n(fd,ffd,n):
	count = 1
	while count <= n:
		line = fd.readline()
		ffd.write(line)
		count += 1
	fd.close()
	ffd.close()


def main():
	filename = input("enter the file name to open : ")
	choice = 0
	while choice != 1:
		choice = eval(input("\n0: start \n1 : stop \n >>>" ))
		
		fd = open(filename)

		ffd = open("output.txt","w")

		if choice == 0:
			n = eval(input("enter the value for n \n-1 for all \n 0 for nothing \n >1 for required line : "))
			if n == -1 :
				copy_all(fd,ffd)
				print ("...")
				read()
			elif n == 0 :
				print ("...")
				read()
			elif n < -1 :
				print ("please give proper positive integer value ")
			elif n >= 1 :
				copy_n(fd,ffd,n)
				print ("...")
				read()
			else:
				pass


if __name__ == '__main__':
	main()