#!/usr/bin/python3

def encryption(msg):
	new = []
	for i in msg:
		new.append(chr(ord(i)+3))
	return ''.join(new)

def decryption(msg):
	new = []
	for i in msg:
		new.append(chr(ord(i)-3))
	return ''.join(new)

def main():
	file_name = input("Enter File Name To Encrypt :")
	fd = open(file_name)
	data_encrypt = fd.read()
	fd.close()

	encrypted_data = encryption(data_encrypt)
	fd = open('encrypted_text.txt','w')
	fd.write(encrypted_data)
	fd.close()

	fd = open('encrypted_text.txt')
	encrypted_data_formFile = fd.read()
	
	decrypted_data = decryption(encrypted_data_formFile)

	fd = open('decrypted_text.txt','w')
	fd.write(decrypted_data)
	fd.close()

if __name__ == '__main__':
	main()
