f1 = input("enter file 1 name of which plagiarism is to check : ")
f2 = input("enter file 2 name : ")

fd = open(f1)
f1 = set((fd.read() ).split(" ") )
fd.close()

fd = open(f2)
f2 = set((fd.read() ).split(" ") )
fd.close()

CF1 = len(f1)

c = 0
for i in f1:
	if i in f2:
		c+=1
		
print ("plagiarism is {}% ".format( (100*c)/CF1 ) )
