#!/usr/bin/python


def divi_by_8():
	


def menu():
	#lb , hb = accept()
	low = eval(input("enter low no : "))
	high = eval(input("enter high bound : "))

	return [x for x in range (low , high ) if divi_by_8() ]

if __name__ == '__main__':
	print(menu())