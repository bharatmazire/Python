#!/usr/bin/python

# problem statement : write a program to accept upper and lower bound  from user and display the prime number in between them.


choice = "y"

while choice == "y":
	lower_bound = eval(input("enter the lower bound : "))
	upper_bound = eval(input("enter the upper bound : "))

	for i in range (lower_bound,upper_bound+1):
		flag = False
		for j in range(2,i//2):
			if i % j == 0:
				flag = True
		if i == 1:
			print("%d is a prime number "%i)
		elif i == 2:
			print("%d is a prime number "%i)
		elif i == 3:
			print("%d is a prime number "%i)
		elif i == 4:
			print("%d is not a prime number "%i)
		elif flag == True:
			print("{} is not a prime number".format(i))
		else:
			print("%d is a prime number "%i)
	choice = input("do you want to check it for more ?  press y to yes : ")