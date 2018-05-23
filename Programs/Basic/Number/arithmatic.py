#!/usr/bin/python

def add(num1,num2):
	return num1+num2

def sub(num1,num2):
	return num1-num2

def multiplication(num1,num2):
	return num1*num2

def division(num1,num2):
	if num2 != 0:
		return num1/num2
	else:
		error = "error"
		return error

def main():
	choice = 1

	while ( choice!=5 ):
		
		choice = eval(input("1. addition  2. subtraction  3.multiplication  4.division 5. stop : "))
		if choice > 4:
			num1 = eval(input("num1 : "))
			num2 = eval(input("num2 : "))

		if choice == 1:
			print(add(num1,num2))
		elif choice == 2:
			print(sub(num1,num2))
		elif choice == 3:
			print(multiplication(num1,num2))
		elif choice == 4:
			print(division(num1,num2))
		else:
			print("thank you")

if __name__ == '__main__':
	main()
