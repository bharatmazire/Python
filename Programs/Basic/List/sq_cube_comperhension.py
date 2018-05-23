#!/bin/usr/python

#finding square and cube of element in list using list comperhension 

def main():
	length = eval(input("enter the length of list to find square andd cube : "))
	print ([[x ,  x*x , x**3] for x in range(length) if x > 0 ])

if __name__ == '__main__':
	main()