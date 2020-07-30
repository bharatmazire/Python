#!/usr/bin/python


def divi_by_8(x):
    if x % 8 == 0:
        print(x)
    else:
        pass

def menu():
	#lb , hb = accept()
	low = eval(input("enter low no : "))
	high = eval(input("enter high bound : "))

	return [x for x in range (low , high ) if divi_by_8(x) ]

if __name__ == '__main__':
	menu()
