#!/usr/bin/python

# problem statements : write a function which accept int value and retur it with string


def count_of_donut(count):
	if count<10:
		print ("Number of donuts are : {}".format(count))
	else:
		print ("Number of donuts are : many")

count = eval(input("Enter the count : "))
count_of_donut(count)