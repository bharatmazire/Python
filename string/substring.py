#!/usr/bin/python

# problrm statement : accepet two string and ckk wether str2 is sub string of str1
'''
s1 = input("enter string 1 : ")
s2 = input("enter string 2 : ")

if s2 in s1:
	print("{} is substring of {} ".format(s2,s1))
else:
	print("{} is not a substring of {} ".format(s2,s1))
'''
# above is without main 
# try without using any built in methods   (like c prog )
'''modification for menu driven and call import '''
def is_sub(s1,s2):
	# s1 = input("enter str 1 : ")
	# s2 = input("enter str 2 : ")
	if s2 in s1:
		print("its a substring ")
	else:
		print("not a substring ")

'''upto this'''

if __name__ == '__main__':
	s1 = input("enter string 1 : ")
	s2 = input("enter string 2 : ")
	is_sub(s1,s2)