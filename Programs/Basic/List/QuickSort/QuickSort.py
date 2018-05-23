import threading as th
from xml.etree import ElementTree as T

class quick:
	def __init__(self):
		self.list = []
	
	def accept(self):
		doc = T.parse('ip.xml')
		
		for i in doc.findall('roll'):
			self.list.append(i.attrib['value'])
		
		for i in self.list:
			print i
	
	def quicksort(self,l,r):
		print "complete list is : ",self.list
		
		if (l < r):
			p = self.partition(l,r)
			
			p1 = th.Thread(target = self.quicksort , args = (l , p-1 ,))
			p2 = th.Thread(target = self.quicksort , args = (p+1 ,r ,))
			
			p1.start()
			p2.start()
			p1.join()
			p2.join()
			
	def partition(self,l,r):
		pval = l
		ll = l
		rr = r
		
		while (ll < rr):
			if(pval == ll):
				if(self.list[pval] >= self.list[rr]):
					t = self.list[pval]
					self.list[pval] = self.list[rr]
					self.list[rr] = t
					pval = rr
				else:
					rr -=1
			else:
				if(self.list[pval] < self.list[ll]):
					t = self.list[pval]
					self.list[pval] = self.list[ll]
					self.list[ll] = t
					pval = ll
				else:
					ll +=1
			
			return pval
			
	def display(self):
		for i in self.list:
			print i
			
q = quick()
q.accept()
q.quicksort(0 , len(q.list)-1)
print "sorted list "
q.display()
