from Crypto.Random import random
from Crypto.PublicKey import DSA
from Crypto.Hash import SHA
import pickle
import os

fd = open("key.txt",'rb')
key = pickle.load(fd)
fd.close()

fd = open("Repo.txt",'rb')
msg = pickle.load(fd)
sig = pickle.load(fd)

fd.close()
h = SHA.new(msg).digest()

os.system("rm -rf *.txt")
if key.verify(h,sig):
    print "OK"	
else:
    print "Incorrect signature"