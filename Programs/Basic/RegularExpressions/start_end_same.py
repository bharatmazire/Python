#!/usr/bin/python


# WAP where 1st word of line present at end

import re

def main():
	sentence = input("enter your sentence : ")
	sent = re.split(" ",sentence)
	first = sent[0]
	first = first + "$"
	#print (first)
	if re.search(first,sentence):
		print ("1st and last same")
	else:
		print("1st and last not same")

if __name__ == '__main__s':
	main()