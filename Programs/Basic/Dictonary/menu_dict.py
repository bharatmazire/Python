#!/usr/bin/python

def accept():
	dict1 = {}
	no_pair_1 = eval(input("enter the number of key values pair you want : "))
	for i in range(0,no_pair_1):
		key = input("enter key : ")
		value = input("enter value : ")
		dict1[key] = value
	return dict1


def compaire_dict(dict1,dict2):
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
	choice = 0
	while choice != 3:
		choice = eval(input("\n1:compaire_dict \n2.from_keys \n3.exit : "))
		if choice == 1:
			dict1 = accept()
			dict2 = accept()
			if compaire_dict(dict1,dict2):
				print ("its same")
			else:
				print ("its not same")
		elif choice == 2:
			dict1 = accept()
			value = eval(input("ennter values : "))
			print (from_keys(dict1,values))
		else:
			print ("thank you >>>")




if __name__ == '__main__':
	main()