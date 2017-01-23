#!/usr/bin/python

# print the square of the elements in lower bound and upper bound 

def sqr():
	l = []
	lower = eval(input("lower bound : "))
	hight = eval(input("higher bound : "))
	for i in range(lower,hight+1):
		l.append(i*i)
	return l

def list_comprihention(lower,hight):
	return [x*x for i in range(lower,hight)]

def main():
	print (sqr())
	lower = eval(input("lower bound : "))
	hight = eval(input("higher bound : "))
	print (list_comprihention(lower,hight))

if __name__ == '__main__':
	main()