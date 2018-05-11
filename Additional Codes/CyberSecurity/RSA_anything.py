#!/usr/bin/python

import math as m
import random as rm

def BigSmall(num1,num2):
	if num1 > num2:
		return num1,num2
	else:
		return num2,num1

def gcd(big,small):
	for i in range(small,1,-1):
		if big % i == 0 and small % i == 0:
			return i
	else:
		return 1

def isPrime(num):
	if num == 1 or num == 2 or num == 3:
		return True
	for i in range(2 , int(m.sqrt(num)) + 1):
		if num % i == 0:
			return False
	else:
		return True

def nmGenerate(p , q):
	n = p * q
	m = (p - 1) * (q - 1)
	return n , m

def edGenerator(p,q,n,m):
	e_arr = []
	for i in range(1,10):
		if gcd(i,m) == 1:
			e_arr.append(i)

	while True:
		e = rm.choice(e_arr)
		if e > 1 and e < m:
			break
	''' for value of d by naives method'''
	ee = e % m
	for i in range(m):
		if (ee * i )% m== 1:
			print (i)
			d = i
			break

	return e , d


def encryption(P,e,n):
	C = []
	new = []
	for i in P:
		new.append(ord(i))
	for i in new:
		C.append((int(int(i) ** e))%n)
	return C

def decryption(C,d,n):
	P = []
	new = []
	for i in C:
	    new.append((int(int(i)**d))%n)
	for i in new:
		P.append(chr(i))
	return P

def main():
	P = input("Enter msg: ")

	print([x for x in range(200) if isPrime(x)])

	p = int(input("enter p (prime number : ): "))
	q = int(input("enter q (prime number : ): "))

	if isPrime(p) and isPrime(q):
		print ("accepted : ")
		n , m = nmGenerate(p , q)
		print (n , m)
		e , d = edGenerator(p,q,n,m)
		print (e , d)

		print("Entered Text is : ",P)
		eData = encryption(P,e,n)
		# fd = open('EncryptedMsg.txt','w')
		# fd.write(str(eData).replace(',','')[1:-1])
		# fd.close()
		print("Encrypted Text is : ",str(eData).replace(',','')[1:-1])
		

		# fd = open("EncryptedMsg.txt")
		# eData = fd.read()
		# for i in eData:
		# 	print (i)
		# 	print (type(i))
		# 	print(chr(int(i)))
		dData = decryption(eData,d,n)
		print ("Decrypted Text is :",str(dData).replace(',','')[1:-1])

if __name__ == '__main__':
	main()
