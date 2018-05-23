#!/usr/bin/python
# alternate add content of array to common list 

def create_array(size):
	array = []
	for i in range(size):
		j = eval(input(" : "))
		array.append(j)
	return array

def array_appende(array1,array2):
	new = []
	i = 0
	j = 0

	while i < len(array1) or j < len(array2):
		print (i , j)
		if i < len(array1):
			new.append(array1[i])
			i+=1
		if j < len(array2):
			new.append(array2[j])
			j+=1
	return new


def main():
	size1 = eval(input("size of 1st array : "))
	size2 = eval(input("size of 2nd array : "))

	array1 = create_array(size1)
	array2 = create_array(size2)

	print (array_appende(array1,array2))

if __name__ == '__main__':
	main()
