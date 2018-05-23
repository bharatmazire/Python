import os
import time

for i in range(8):
    fd = open('ip.json','w')
    fd.write('{"start" :'+str(i)+'}')
    fd.close()
    os.system("python2 queen.py > result.txt")
    os.system("cat result.txt")
    time.sleep(2)
