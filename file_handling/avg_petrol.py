#!/usr/bin/python

# write a code to read a file of petrol price maharashtra , goa , karnataka (input file "input_petrol.txt")
# output the avrrage petrol price for each state to an output file named "petrol_avg_out.txt"

def read_file(fd):
	mh = []
	ga = []
	kn = []

	line = "a"
	while line != '':
		line = fd.readline()
		mh.append(line[9:11])
		ga.append(line[12:14])
		kn.append(line[15:17])
	return mh,ga,kn

def convert(mh,ga,kn):
	for a in (mh,ga,kn):
		for i in range(len(a)-1):
			if i != '':
				a[i] = eval(a[i])
		a.pop()
	
	return mh,ga,kn

def find_value(mh,ga,kn):
	avg = []
	for a in (mh,ga,kn):
		avg.append(sum(a)/len(a))
	return avg


def main():
	filename = input("enter the file name to open the file : ")
	fd = open(filename)

	mh,ga,kn = read_file(fd)
	mh,ga,kn = convert(mh,ga,kn)
	avg = find_value(mh,ga,kn)
	print ("avg of maharashtra is :",avg[0])
	print ("avg of goa is         :",avg[1])
	print ("avg of kartanaka is   :",avg[2])

	ffd = open("petrol_avg_out.txt","w")
	for a in range(0,3):
		avg[a] = str(avg[a])
	for a in range(0,3):
		ffd.write(avg[a])
		ffd.write(" ")
	ffd.close()
	fd.close()

if __name__ == '__main__':
	main()