#!/usr/bin/python

# WAP to accept complex number and perform required operation

class Complex():
	'''
		This script is for accepting the compelx number and perform various arithmatic operation on it
	'''
	def __init__(self):
		'''
			This is constructor 
			It set default value as 0
		'''
		# self.real 		= 0
		# self.imaginary 	= 0j
		self.number 		= 0

	def accept_values(self,r):
		'''
			This method is use for accepting value.
			Value must be complex number with some real and imaginary part (imaginary must given as 'j')
		'''
		# r = eval(input("enter real value : "))
		# i = eval(input("enter imaginary value : "))
		# self.real 		= r
		# self.imaginary 	= i
		#r = eval(input("enter  value : "))
		self.number = r

	def show_number(self):
		'''
			This method is use to display the accepted (complex )value
		'''
		#print("{}".format(self.number))
		#print(type(self.number))
		return self.number

	def addition(self,num):
		'''
			This method is for addition of two number of whose one number must be complex number which is accepted before
			and another number is either simple integer or complex number
		'''

		#num = eval(input("enter value for addition : "))
		#print("addition is : {}".format(self.number + num))
		return self.number + num

	def subtraction(self,num):
		'''
			This method is for subtraction of two number of whose one number must be complex number which is accepted before
			and another number is either simple integer or complex number
		'''

		#num = eval(input("enter value for subtration : "))
		#print("subtraction is : {}".format(self.number - num))
		return self.number - num

	def multiplication(self,num):
		'''
			This method is for multiplication of two number of whose one number must be complex number which is accepted before
			and another number is either simple integer or complex number
		'''

		#num = eval(input("enter value for multiplication : "))
		#print("multiplication is : {}".format(self.number * num))
		return self.number * num

if __name__ == '__main__':
	'''
		Code execution start from here
		First we create an object of class Complex and the apply various methods according to use
	'''
	obj1 = Complex()

	choice = 0
	while choice != 5:
		choice = eval(input("1. accept \n2. addition \n3. subtraction \n4. multiplication \n5. Stop : "))
		
		if choice == 1:	
			r = eval(input("enter  value : "))
			obj1.accept_values(r)
			
			print("after accepting value ")
			print(obj1.show_number())

		elif choice == 2:
			num = eval(input("enter value for addition : "))
			print(obj1.addition(num))

		elif choice == 3:
			num = eval(input("enter value for subtraction : "))
			print(obj1.subtraction(num))

		elif choice == 4:
			num = eval(input("enter value for multiplication : "))
			print(obj1.multiplication(num))
		else:
			print ("thank you !!!")	