#!/usr/bin/python

# merge two sorted list

def accept_list(l1,l2):
	size_l1 = eval(input("length of l1 : "))
	print ("enter values for list 1")
	for i in range(size_l1):
		value = eval(input(">>> "))
		l1.append(value)
	
	size_l2 = eval(input("lenght of l2 : "))
	print ("enter values for list 2")
	for i in range(size_l2):
		value = eval(input(">>> "))
		l2.append(value)

	l1.sort()										# l1.sort() method return change on list   original list get affected.
	l2.sort()										# list changes reflects on original 
	
	return l1,l2

def merge(l1,l2):
	l3 = []
	i , j = 0 , 0

	while (i < len(l1)) and (j < len(l2)):
		if l1[i] < l2[j]:
			l3.append(l1[i])
			i+=1
		elif l1[i] > l2[j]:
			l3.append(l2[j])
			j+=1
		else:
			l3.append(l1[i])
			l3.append(l2[j])
			i+=1
			j+=1
	if i < len(l1):
		l3.extend(l1[i:])
	if j < len(l2):
		l3.extend(l2[j:])
	return l3

def main():
	l1 = []
	l2 = []
	l1 , l2 = accept_list(l1,l2)
	print (merge(l1,l2))

if __name__ == '__main__':
	main()