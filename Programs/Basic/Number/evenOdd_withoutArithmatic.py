#!/usr/bin/python

# PYTHON3
# mr.india : 23/10/2016
# problem statement : write a program to accept the number from usr and check wether it is even or odd WITHOUT USING ARITHMATIC OPERATOR .

# so here we are not using arithmatic operator , insted of that we ll go with BITWISE operator.
# we know that for all odd numbers LSb is always "1" eg. 1 = 0001 , 3 = 0011 and even numbers LSb is always "0" eg. 2 = 0010 , 4 = 0110 etc.
# so we will use this thing ...



def check_odd_even(number):
	if number & 1 == 1:											 # eg number = 5 = 0101     so 0101 & 0001 == 0001 coz 1 & 1 is 1    so its odd
		print (number," is odd number ")
		print ("{} is odd number ".format(number))				 # {} will represent the space to print and by this method we ll  not need to write data type
	else:
		print ("%d is even number "%number)
		print ("{0} is even number ".format(number))			 # here 0 is index in format array content (its an index of number )

choice = 'N'
while (choice == 'N'):
	number = input("Enter the number :")
	check_odd_even(number)								
	choice = ("you want to cheack more Y for yes N for no ")	



# having problem with python 3
# having problem at while i.e. its not working as per requirements means its not working in while form..
