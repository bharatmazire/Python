#!/usr/bin/python

def add(num1,num2):
	print(num1+num2)

def sub(num1,num2):
	print(num1-num2)

def multiplication(num1,num2):
	print(num1*num2)

def division(num1,num2):
    while True:
        try:
            print(num1/num2)
            break
        except ZeroDivisionError:
            num2 = int(input('num2 cannot be 0, please enter new number: '))
        

def main():
	while True:
		num1 = float(input("num1 : "))
		num2 = float(input("num2 : "))
		choice = int(input("1. addition  2. subtraction  3.multiplication  4.division 5. stop : "))

		if choice == 1:
			add(num1, num2)
		elif choice == 2:
			sub(num1, num2)
		elif choice == 3:
			multiplication(num1, num2)
		elif choice == 4:
			division(num1, num2)
		elif choice == 5:
			break
		elif choice > 5:
			print('enter number less than 5')
if __name__ == '__main__':
	main()
