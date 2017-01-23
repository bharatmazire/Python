#!/usr/bin/python

# implement queue using list
# function nqueue dqueue is_empty is_full

def nqueue(l,data,length):
	if is_full(l,length):
		print ("its full ")
		return l
	l.append(data)
	return l

def dqueue(l):
	if is_empty(l):
		print ("its empty ")
		return "0"
	print(l.pop(0))
	return l 

def is_empty(l):
	if len(l) == 0:
		return True
	return False

def is_full(l,length):
	if len(l)<length:
		return False
	return True


def main():
	choice = 0
	l = []
	length = eval(input("enter length of queue : "))

	while choice != 5:

		choice = eval(input("\n 1.add \n 2.show \n 3.is_empty \n 4.is_full \n 5.stop  : "))

		if choice == 1:
			data = eval(input("enter data : "))
			print (nqueue(l,data,length))
		elif choice == 2:
			print (dqueue(l))
		elif choice == 3:
			if is_empty(l):
				print ("its empty ")
			else:
				print ("its not empty ")
		elif choice == 4:
			if is_full(l,length):
				print ("its full ")
			else:
				print ("its not full ")
		else:
			print ("thank you")

if __name__ == '__main__':
	main()