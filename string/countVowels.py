#!/usr/bin/python

# problem statement : write a program which will accept the input from the user + print it and then it count the vowels and consequents from it
'''
choice = "y"

while choice == "y":
	string = input("enter the string : ")
	count = 0
	xcount = 0
	total = 0
	for i in string:
		if i in ('a','e','i','o','u','A','E','I','O','U'):
			count+=1
			total+=1
		else:
			xcount+=1
			total+=1
	print("total count of alphabates are {} ".format(total))
	print("count of vowels is {} ".format(count))
	print("count of non vowels is %d "%xcount)
	
	choice = input("do you want to check it again? press y to yes : ")
'''
# above is whitout function call
'''for menu import '''
def cnt_vowel(s):
	cnt_v = 0
	cnt_c = 0
	for i in s:
		if i in "aeiouAEIOU":
			cnt_v += 1
		else:
			cnt_c += 1
	print ("{} no. of vowels and {} no. of consonels ".format(cnt_v,cnt_c))
'''for menu'''

if __name__ == '__main__':
	s1 = input("enter string 1 : ")
	cnt_vowel(s1)