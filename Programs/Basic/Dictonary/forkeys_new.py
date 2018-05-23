#!/usr/bin/python

def accept(dict1):
	no_pair_1 = eval(input("enter the number of key values pair you want : "))
	for i in range(0,no_pair_1):
		key = input("enter key : ")
		value = input("enter value : ")
		dict1[key] = value
	return dict1
	print ("{} is dictonary ".format(dict1))

def from_keys(dict1,values):
	if not isinstance(dict1,dict):
		return False
	result = {}

	if isinstance(values,list) and (values,tuple):
		i = 0
		for key in dict1:
			if i<len(values):
				result[key] = values[i]
				i+=1
			else:
				result[key] = None
		return result

	else:
		for key in dict1:
			result[key] = values
		return result

def main():
	dict1 = {}
	dict1 = accept(dict1)
	values = eval(input("enter the values : "))
	print(from_keys(dict1,values))

if __name__ == '__main__':
	main()