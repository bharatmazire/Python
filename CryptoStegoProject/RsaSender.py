#!/usr/bin/python

# function to encrypt data
def encryption(P,e,n):
	C = []
	new = []
	for i in P:
		new.append(ord(i))
	for i in new:
		C.append((int(int(i) ** e))%n)
	return C

def main():
	#FileName = input("Enter File name of Publik key distribution ")
	FileName = 'Repository.txt'
	fd = open(FileName)
	n = int(fd.readline())
	e = int(fd.readline())
	fd.close()

	P = input("Enter Message : ")
	data1 = encryption(P,e,n)
	EncryptedData = []
	for i in data1:
		EncryptedData.append(chr(i))

	fd = open("Messege.txt","w")
	fd.write(str(EncryptedData).replace(',','')[1:-1])
	fd.close()



if __name__ == '__main__':
	main()
