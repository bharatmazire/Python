#!/usr/bin/python

# problem statement : write a program to accept a character and cheeack whether it is vowel or not .

choice = 1

while choice == 1:
	ch = input("enter character to check : ")
	vowel = {'a','e','i','o','u'}

	if ch in vowel:					# [or if ch in "aeiou": ] it will check in the list whether that perticular element is present or not
		print ("{} is vowel ".format(ch))
	else:
		print (ch," is not vowel ")

	choice = eval(input("enter the choice 1.yes  2.no : "))
