import copy as cp
import multiprocessing as mp
import time as tm
nodes = int(raw_input("Enter the number of nodes you want : "))
array = []
check = []
cost = []
count = 0

for i in range(0 , nodes):
	array.append([])
	for j in range(0 , nodes):
		number = int(raw_input("Enter the number : "))
		array[i].append(number)
print "Entered value are : ",array
row = cp.deepcopy(array)

def tsp(check,visited_node,cost,array,count):
	check.append(visited_node)
	cost.append(min(array[visited_node]))

	for i in range(0 , nodes):
		array[i][visited_node] = 99

	minimum = array[visited_node].index(min(array[visited_node]))

	count += 1

	if count < nodes:
		tsp(check,minimum,cost,array,count)

	return check,cost

def run(node):
	path,value = tsp(cp.copy(check),node,cp.copy(cost),cp.copy(array),0)
	value.append(row[path[-1]][node])
	path_to_check = cp.deepcopy(path)
	if len(path) == len(set(path_to_check)):
		path.append(node)
	else:
		path = [0]
		value = [0]

	print "for noded : %s  minimum path is : %s  with the cost of : %s  "%(node,path,sum(value)-99)

for i in range(0 , nodes):
	p = mp.Process(target = run,args = (i,))
	print "starting time of node %s is : %s"%(i,tm.time())
	p.start()	
