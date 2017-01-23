#!/usr/bin/python

# implement stack using list

def push(data,l,size_stack):
	if is_full(l,size_stack):
		print ("its full ")
		return l
	l.append(data)
	return l

def pop(l):
	if is_empty(l):
		print ("its empty ")
		return l
	return l.pop()

def is_full(l,size_stack):
	if len(l) < size_stack:
		return False
	return True

def is_empty(l):
	if len(l) == 0:
		return True
	return False

def peep(l):
	if is_empty(l):
		return "0"
	return l[-1:]

def main():
	l = []
	size_stack = eval(input("enter the size of stack : "))
	print (l)
	choice = 0
	while choice != 6:
		choice = eval(input("\n 1.push \n 2.pop \n 3.is_full \n 4.is_empty \n 5.peep \n 6.stop : "))
		
		if choice == 1:
			data = eval(input("enter data : "))
			print (push(data,l,size_stack))
		elif choice == 2:
			print ("poped elemment is : {}".format(pop(l)))

		elif choice == 3:
			if is_full(l,size_stack):
				print ("its  full ")
			else : 
				print("its not full ")

		elif choice == 4:
			if is_empty(l):
				print ("its empty ")
			else:
				print ("its not empty ")

		elif choice == 5:
			print(peep(l))

		else:
			print ("\n thank you ...")

if __name__ == '__main__':
	main()