#!/usr/bin/python

def sum_of_list(l):
	s = 0
	for i in l:
		s+=i
	print ("{} is sum ".format(s))

def accept():
	list = []
	num = eval(input("enter the size of list : "))
	for i in range(num):
		elements = eval(input("input integer only :"))
		list.append(elements)
	print (list)
	return list

def min_max(list):
	mn = list[0]
	mx = list[0]

	for i in list[1:]:
		if mx < i:
			mx = i
		if mn > i:
			mn = i

	print ("{} : is min and {} : is max ".format(mn,mx))

if __name__ == '__main__':
	l = accept()
	min_max(l)
	sum_of_list(l)