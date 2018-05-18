#!/usr/bin/python

# problem statement : To check wheather given string is palindrom or not. 

s = input("Enter String")
def chk(s):
	if s == s[::-1]:
		return s+" is palindrome"
	else:
		return s+" is not palindrome"
print(chk(s))
