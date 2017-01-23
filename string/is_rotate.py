#!/usr/bin/python

# problem statement : enter two strings and chk whether 2nd str is circular string of 1st string
# abcde     ...   deabc
''' old logic was this'''
# str1 = input("enter string 1 : ")
# str2 = input("enter string 2 : ")

# if len(str1) == len(str2):
# 	str2_hl = str2[str2.find(str1[0]):]                # with example stated above   ..   find abc in deabc
# 	if str2_hl in str1:									# if it present in str1
# 		str1_hl = str1[len(str2_hl):]					# find de i.e. remaining part than abc
# 		if str1_hl == str2[:str2.find(str1[0]):]:		# if de in str1 is eqal to part before abc
# 			print("its circular substring ")			# we found what we want ...
# 		else:
# 			print("not circular ")
# 	else:
# 		print("not cirularrr")
# else:
# 	print("plz ch both str ")
''' old logic upto this '''

def is_rotate(s1,s2):
	s1 += s1
	# if s2 in s1:
	# 	return "true "
	# else:
	# 	return "false "
	return s2 in s1

#print(is_ratate(s1,s2))
#is_rotate(s1,s2)
# if __name__ == '__main__':
# 	s1 = input("str 1")
# 	s2 = input("str 2")
# 	if is_rotate(s1,s2):
# 		print("{} is rotation of {}".format(s2,s1))
# 	else:
# 		print("{} is not rotation of {}".format(s2,s1))

# try for import '

# s1 = input("str 1 : ")
# s2 = input("str 2 : ")
# if is_rotate(s1,s2):
# 	print("{} is rotation of {}".format(s2,s1))
# else:
# 	print("{} is not rotation of {}".format(s2,s1))

def main():
	s1 = input("str 1")
	s2 = input("str 2")
	if is_rotate(s1,s2):
		print("{} is rotation of {}".format(s2,s1))
	else:
		print("{} is not rotation of {}".format(s2,s1))

if __name__ == '__main__':
	main()