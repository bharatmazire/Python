#!/usr/bin/python

import RsaPublicKeyDist as RSA1
import RsaSender as RSA2
import RsaReceiver as RSA3
import PIL.Image as pimg
import Histo as h
import multiprocessing as mp

#function for generating RGB value from given int value

def getRGBfromI(RGBint):
	blue =  RGBint & 255
	green = (RGBint >> 8) & 255
	red =   (RGBint >> 16) & 255
	return red, green, blue

#function for generating int value from given RGB value

def getIfromRGB(rgb):
	red = rgb[0]
	green = rgb[1]
	blue = rgb[2]
	RGBint = (red<<16) + (green<<8) + blue
	return RGBint

def main():
	RSA1.main()

	FileName = 'Repository.txt'
	fd = open(FileName)
	n = int(fd.readline())
	e = int(fd.readline())
	fd.close()

	length = 0
	while length != 16:
		P = input("Enter user name size of 8 characters : ")
		P += input("Enter password size of 8 characters : ")
		length = len(P)

	data1 = RSA2.encryption(P,e,n)
	print("Encrypted data is  : ",data1)
	
	ImageToOpen = str(input("Enter Image to process : "))
	Image = pimg.open(ImageToOpen)
	ImageToProcess = Image.load()

	for j in range(16):
		#i in data1:
		r,g,b = getRGBfromI(data1[j])			# generate RGB value for each entry in cipher text
		#print(r,g,b)
		ImageToProcess[0,j] = (r,g,b)			# hiding data behind pixel (overriding values)
		#print(ImageToProcess[0,j])

	Image.save("s2.png")
	
	#-----> upto this part data encrypted and stored behind image 

	print("for decryption")
	ImageToOpen1 = str(input("Enter Image to process : "))
	Image1 = pimg.open(ImageToOpen1)
	ImageToProcess1 = Image1.load()

	data1 = []
	for j in range(16):
		#print(ImageToProcess1[0,j])
		a = getIfromRGB(ImageToProcess1[0,j])		# geting value of cipher text from image
		data1.append(a)

	FileName = 'Repository.txt'
	fd = open(FileName)
	n = int(fd.readline())
	fd.close()
	#print(data1)

	C = data1
	d = int(input("Enter Private Key : "))
	P = RSA3.decryption(C,d,n)
	#print(P)
	print("username is : ",str(P).replace(',','').replace("'",'').replace(" ","")[1:-9])
	print("passowrd is : ",str(P).replace(',','').replace("'",'').replace(" ","")[-9:-1])


	print ("histogram comparision")
	p1 = mp.Process(target = h.draw , args=("s1.jpg",))
	p2 = mp.Process(target = h.draw , args=("s2.png",))
	p1.start()
	p2.start()
	

if __name__ == '__main__':
	main()
