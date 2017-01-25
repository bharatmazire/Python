#!/usr/bin/python

# problem statement : write a program which will give menu driven approach for calculator program . ++ ask it for multiple times.
#term use : if , elif , eval , while , format 



no1 = eval(input("enter the number 1 : "))
no2 = eval(input("enter the number 2 : "))

operation = eval(input("1.addition   2.subtraction   3.mutiplication   4.division    5.mod    6.compaire   7.exit : "))

while operation != 7 :
	if operation == 1:
		print ("addition is {} ".format(no1+no2))
	elif operation == 2:
		print ("subtraction is {} ".format(no1-no2))
	elif operation == 3:
		print ("multiplication is {} ".format(no1*no2))
	elif operation == 4:
		if no2 != 0:
			print ("division is {} ".format(no1/no2))
		else:
			print ("{} is zero so multiplication is errorisum ".format(no2))
	elif operation == 5:
		print ("mod value is {} ".format(no1%no2))
	elif operation == 6:
		if no1 < no2:
			print ("{} is less than {} ".format(no1,no2))
		elif no1 > no2:
			print ("{} is greater than {} ".format(no1,no2))
		else:
			print ("{} is equal to {} ".format(no1,no2))
	else:
		print ("please check the input ....")

	operation = eval(input("0.accept new numbers 1.addition   2.subtraction   3.mutiplication   4.division    5.mod    6.compaire   7.exit : "))

	if operation == 0:
		no1 = eval(input("enter the number 1 : "))
		no2 = eval(input("enter the number 2 : "))
		operation = eval(input("1.addition   2.subtraction   3.mutiplication   4.division    5.mod    6.compaire   7.exit : "))