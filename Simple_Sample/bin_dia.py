#!/usr/bin/python
def search_left(values,show_list,i):
	show_list.insert(0,i)
	ind = values.index(i)
#	print (ind)
#	print (show_list)

	while ind < (len(values)//2):
		for j in range(ind+1):
			ind += 1

		if values[ind]<values[ind+1]:
			show_list.insert(0,values[ind+1])
			ind += 1
#			print (show_list)
		elif values[ind]>values[ind+1]:
			show_list.insert(0,values[ind])
#			print (show_list)
		else:
			pass
	return show_list

def search_right(values,show_list,i):
	show_list.append(i)
	ind = values.index(i)

	while ind < (len(values)//2):
		for j in range(ind+1):
			ind += 1
		if values[ind]<values[ind+1]:
			show_list.append(values[ind+1])
			ind += 1
#			print (show_list)
		elif values[ind]>values[ind+1]:
			show_list.append(values[ind])
#			print (show_list)
		else:
			pass
	return show_list


def accept():
	nodes = eval(input("enter the number of nodes : "))
	values = input("enter input with space seperate : ")
	values = values.split(" ")
	return nodes , values

def main():
	nodes , values = accept()
	show_list = ['1']
	for i in values:
		if i == values[1]:
			show_list = search_left(values,show_list,i)
			#print (show_list)
		elif i == values[2]:
			show_list = search_right(values,show_list,i)
		else:
			pass
	print ("path is : ",show_list)
	s = 0
	for i in show_list:
		i = eval(i)
		s += i
	print ("cost is : ",s)

if __name__ == '__main__':
	main()