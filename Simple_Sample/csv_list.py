import csv
import os

exampleFile = open("csv_example")
exampleReader = csv.reader(exampleFile)
print (exampleReader)
exampleData = list(exampleReader)
print (exampleData)
os.system("$exampleData > file")
fd = open("file")
file = fd.read()
fd.close()
print(file[40::])