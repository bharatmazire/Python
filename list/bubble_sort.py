#!/usr/bin/python

#bubble sort

def accept(l):
	size = eval(input("length of list : "))
	print ("enter values for list ")
	for i in range(size):
		value = eval(input(">>> "))
		l.append(value)
	return l

def bubble_sort(l):
	i = 0
	#print ("out if while ")
	while i < len(l):
		#print ("inside while 1 ")
		j = 0
		while j < len(l)-i-1:
			#print ("inside while 2")
			if l[j] > l[j+1]:
				#print ("inside if ")
				x = l[j]
				l[j] = l[j+1]
				l[j+1] = x
			j += 1
		i+= 1

	return l


def menu():
	l = []
	l = accept(l)
	print (bubble_sort(l))

if __name__ == '__main__':
	menu()