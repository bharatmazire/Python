#!/usr/bin/python

# finding prime number using list comperhwnsion

def is_prime(x):
	for i in range(2,x//2+1):
		if x%i == 0:
			return False
	else:
		return True

def main():
	lb = eval(input("enter lower bound : "))
	hb = eval(input("enter higher bound : "))
	print ([x for x in range (lb,hb) if is_prime(x) ])

if __name__ == '__main__':
	main()