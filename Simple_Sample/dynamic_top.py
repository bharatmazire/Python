#!/usr/bin/python

# WAP to give system update 

import os
import time
import re

def main():
	count = 0
	while count < 2:						# for number of times you want system updates
		os.system("top -n 1 > top.txt")
		fr = open("top.txt")
		fw = open("info.txt","a+")
		top = fr.read()
		top = top[5:top.find("PID")]
		# time = "at time "+ re.search(r'[0-9]{2}:[0-9]{2}:[0-9]{2}',top).group()
		# span =re.search(r"[\d]{0,4} total,[ ]+[\d]{0,2} running,[ ]+[\d]{0,4} sleeping,[ ]+[\d]{0,3} stopped,[ ]+[\d]{0,3} zombie",top).group()
		# total = span[0:3]
		# running = span[13:14]
		# sleeping = span[24:27]
		# stopped = span[40:41]
		# zombie = span[-8:-7]
		# new = time +"\ntotal task are : "+total+"\nrunnig are : "+running+"\nsleepting are : "+sleeping+"\nstopped are : "+stopped+"\nzombied are : "+zombie
		# fw.write("-----------------------------------------------------------")
		# fw.write(new)
		fw.write(top)
		fw.close()
		fr.close()
		count+=1
		time.sleep(10)
	# ffrw = open("info.txt")
	# file_to_show = ffrw.read()
	# ffrw.close()
	# os.system("rm -rf info.txt")
	# file_to_show = re.sub(r'[\n] +','',file_to_show)
	# ffrw = open("info.txt","w")
	# ffrw.write(file_to_show)
	# ffrw.close()
	os.system("cat info.txt")


if __name__ == '__main__' :
    main()
