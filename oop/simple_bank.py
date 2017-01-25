#!/usr/bin/python
	
# Write a program with class Bank having various bank fuction

class Bank(object):
	'''
		obj.Bank(<name> , <age>)
		it will create object of bank class which will allow to perform deposite , withdraw and cheack operation
		account nnumber will be generated automatically along with object
	'''
	account_number = 0

	def __init__(self,name,age):
		'''
			Inital constructor
			It will initialise initial balance with 500
			and automatic next account number will assigned to account number

		'''
		Bank.account_number += 1
		self.b_acc = Bank.account_number
		self.amount = 500
		self.name = name
		self.age = age

	def deposite(self,amount):
		'''
			It use to deposite the amount in account 
		'''
		self.amount += amount
		return self.amount

	def withdraw(self,amount):
		'''
			It is used to withdraw amount from account 
			probably sufficient amount should present in account
		'''
		if self.amount >= (amount + 500):
			self.amount -= amount
			return self.amount
		else:
			return "not possible "

	def cheak(self):
		'''
			Used to return the current balance and account number of account 
		'''
		return self.amount , self.b_acc
#.....................................................................................................

def object_creation(obj):
	'''
		This function is not under class Bank
		It use to perdform various operations on account
	'''
	operation = 0
	while operation != 4:

		print("enter operation to perform !!")
		operation = eval(input("1.deposite 2.withdraw 3.cheack 4.exit : "))

		if operation == 1:
			amount = eval(input("enter amount to deposite : "))
			
			print ("total amount in account is : {}".format(obj.deposite(amount)))

		elif operation == 2:
			amount = eval(input("enter amount to withdraw : "))
			
			print("total amount in account is : {}".format(obj.withdraw(amount)))

		elif operation == 3:
			amt , num = obj.cheak()
			print ("total amount in account is :{} with account number : {}".format(amt , num))

		else:
			print ("thank you !!!")


if __name__ == '__main__':

	choice = 0
	obj = []
	while choice != 2:
		name = input("enter name of user : ")                                                     	# name of user
		age = eval(input("enter age of user : "))													# age of user

		obj_temp = Bank(name,age)																		# object of that same name as of user name
		
		object_creation(obj_temp)
		obj.append(obj_temp)

		choice = eval(input("enter choice 1.again 2.stop : "))

		
	while True:
		op_c = input("enter name of user on whome you want to perform operation : ")

		
		if op_c in [x.name for x in obj]:
			for i in obj:
				if op_c == i.name:
					object_creation(i)
					break
				
