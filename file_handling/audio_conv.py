#!/usr/bin/python

# accept the file audio.conf and convert it in dict of dict

def new_dict(fd,line):
	dict1 = {}
	while not line.startswith('[') and line != '':
		if line.startswith('\n') or line.startswith('#'):
			line = fd.readline()
			continue
		k = line[0:line.index('=')]
		v = line[line.index('=')+1:-1]
		if '#' in v:
			v = line[line.index('=')+1:line.index('#')]
		dict1[k] = v
		line = fd.readline()
	if line.startswith('[') or line == '':
		return dict1, line


def first_key(line,fd):
	dic = {}
	while line != '':
		#print (line)
		key = line[1:-2]
		#print("key : ",key)
		line = fd.readline()
		value,line = new_dict(fd,line)
		dic[key] = value
		#print (dic)
		#print ('\n')
	#print (dic)
	return dic

def f_read(fd):
	line = "a"
	while line != '':
		line = fd.readline()
		if line.startswith('#') or line.startswith('\n'):
			continue
		if line.startswith('['):
			dictonary = first_key(line,fd)
	return dictonary

def main():
	filename = input("enter the file name with absolute path : ")
	fd = open(filename)

	d = f_read(fd)
	print (d)
	l = 'y'
	while l != 'no':
		choice = input("enter the key to see in file its attributes :")
		if choice in d:
			print (d[choice])
		l = input("you want for more (yes / y / Y ): ")
if __name__ == '__main__':
	main()