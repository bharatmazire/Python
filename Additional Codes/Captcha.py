import string as s
import random as rm


def main():
	captcha = ''.join(rm.choice(s.letters+s.letters) for i in range(10))
	print("Captcha is : {}".format(captcha))
	EnteredValue = input("Enter CAPTCHA :  ")
	if captcha == EnteredValue:
		print ("matched !!!")
	else:
		print ("not mathched !!!")

if __name__ == '__main__':
	main()