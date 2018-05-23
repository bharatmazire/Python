from Crypto.Random import random
from Crypto.PublicKey import DSA
from Crypto.Hash import SHA
import pickle

message = str(raw_input("Enter Your Msg : "))
key = DSA.generate(1024)
h = SHA.new(message).digest()
k = random.StrongRandom().randint(1,key.q-1)
sig = key.sign(h,k)

fd = open("key.txt",'ab')
pickle.dump(key , fd)
fd.close()

fd = open("Repo.txt","ab")
pickle.dump(message , fd)
pickle.dump(sig,fd )

fd.close()

fd.close()
