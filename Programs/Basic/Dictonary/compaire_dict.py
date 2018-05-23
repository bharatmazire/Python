#!/usr/bin/python

def accept(dict1,dict2):
	no_pair_1 = eval(input("enter the number of key values pair you want : "))
	for i in range(0,no_pair_1):
		key = input("enter key : ")
		value = input("enter value : ")
		dict1[key] = value

	print ("{} is dictonary ".format(dict1))

	no_pair_2 = eval(input("enter the number of key values pair you want : "))
	for i in range(0,no_pair_2):
		key = input("enter key : ")
		value = input("enter value : ")
		dict2[key] = value

	print ("{} is dictonary ".format(dict2))


def dict_compaire(dict1,dict2):
	if len(dict1) != len(dict2):
		return False
	for key in dict1:
		if key in dict2:
			if dict1[key] == dict2[key]:
				continue
			else:
				return False
		else:
			return False
	return True



def main():
	dict1 = {}
	dict2 = {}
	accept(dict1,dict2)
	if dict_compaire(dict1,dict2):
		print ("yes")


if __name__ == '__main__':
	main()