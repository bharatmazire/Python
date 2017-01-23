#!/usr/bin/python

# problem various menu driven approch using list

'''                                                                              '''
def accept():
	list = []
	num = eval(input("enter the size of list : "))
	print ("enter values of list")
	for i in range(num):
		elements = eval(input(" >>> "))
		list.append(elements)
	return list
'''                                                                              '''

def min_max(list):
	mn = list[0]
	mx = list[0]

	for i in list[1:]:
		if mx < i:
			mx = i
		if mn > i:
			mn = i
	
	return mn , mx
'''                                                                              '''

def sqaure_list(low,high):
	return [x*x for x in range(low,high)]

'''                                                                              '''

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

'''                                                                                        '''

def intersection(list1,list2):
	list1 = set(list1)
	list2 = set(list2)
	list = list1.intersection(list2)
	return list

'''                                                                                        '''

def union(list1,list2):
	list1 = set(list1)
	list2 = set(list2)
	list = list1.union(list2)
	return list

'''                                                                                        '''

def sum_of_list_count(list,a=0,count=0):
	for i in list:
		a += i
		count +=1
	return a,count

'''                                                                                        '''
def main():
	choice = 0
	while choice != 8 :
		choice = eval(input("\n1.min_max \n2.sqaure_list \n3.sort_n_merge \n4.intersection \n5.union \n6.sum_of_list \n7.length \n8.end : "))

		if choice == 1:
			list = accept()
			mn , mx = min_max(list)
			print ("{} : is min and {} : is max ".format(mn,mx))

		elif choice == 2:
			low = eval(input("low limit : "))
			high = eval(input("high limit : "))
			print (sqaure_list(low,high))
		
		elif choice == 3:
			list1 = accept()
			list2 = accept()
			list1.sort()
			list2.sort()
			print (merge(list1,list2))
		
		elif choice == 4:
			list1 = accept()
			list2 = accept()
			print (intersection(list1,list2))

		elif choice == 5:
			list1 = accept()
			list2 = accept()
			print (union(list1,list2))

		elif choice == 6:
			list = accept()
			s , count = sum_of_list_count(list)
			print (s)

		elif choice == 7:
			list = accept()
			s , count = sum_of_list_count(list)
			print (count)

		else : 
			count = 0
			for i in "thank you ...":
				print (" "* count + i)
				count +=1
				for j in range(10000000):
					pass

'''                                                                              '''

if __name__ == '__main__' :
	main()