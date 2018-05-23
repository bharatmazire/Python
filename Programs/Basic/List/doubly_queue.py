#!/usr/bin/python

def insert_left(l,value,size):
	if is_full(l,size):
		print ("its full ")
		return l
	l.insert(0,value)
	return l

def insert_right(l,value,size):
	if is_full(l,size):
		print ("its full ")
		return l
	l.append(value)
	return l

def pop_left(l):
	if is_empty(l):
		print ("list already empty")
		return l
	l_p = l.pop(0)
	print ("poped element is :{}".format(l_p))
	return l

def pop_right(l):
	if is_empty(l):
		print ("list already empty")
		return l	
	l_p = l.pop()
	print ("poped element is :{}".format(l_p))
	return l

def is_empty(l):
	if len(l) == 0:
		return True
	return False

def is_full(l,size):
	if len(l) == size:
		return True
	return False

def main():
	l = []
	size = eval(input("Enter the size of list : "))
	choice = 0
	while choice != 8:
		choice = eval(input("\n1.insert_left \n2.insert_right \n3.pop_left \n4.pop_right \n5.is_empty \n6.is_full \n7.show \n8.end : "))

		if choice == 1:
			value = eval(input("enter value to insert at left : "))
			print (insert_left(l,value,size))

		elif choice == 2:
			value = eval(input("enter value to insert at right : "))
			print (insert_right(l,value,size))

		elif choice == 3:
			print (pop_left(l))


		elif choice == 4:
			print (pop_right(l))

		elif choice == 5:
			if is_empty(l):
				print ("its empty ")
			else:
				print ("its not empty ")

		elif choice == 6:
			if is_full(l,size):
				print ("its full ")
			else:
				print ("its not full ")
		
		elif choice == 7:
			print (l)

		else:
			print ("thank you !!!")

if __name__ == '__main__':
	main()