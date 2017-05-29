import sys
import os
import re
import string as s
import random as rm
from PyQt4 import QtCore , QtGui, uic
from pathlib import Path



class MyWidget(QtGui.QMainWindow):
	
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		
		self.ui = uic.loadUi('AutoTool.ui',self)	# for loading the application UI
		self.ui.setWindowTitle("Automated Tool")	# setting TITLE for UI
		self.ui.show()								# showing UI

		''' button click events call'''
		self.BtnList.clicked.connect(self.ListOfFile)	
		self.BtnObj.clicked.connect(self.Object)
		self.BtnScript.clicked.connect(self.Script)
		self.BtnPcapOp.clicked.connect(self.PcapOp)

	# defination for list of file
	def ListOfFile(self):
		EnteredPcapName = self.ui.LineEditFname.toPlainText()					# accepting input from LineEdit
		
		my_file = Path(str(EnteredPcapName))
		if not my_file.is_file():
			self.ui.textBrowser.setText("Enter valid path ")
			return 0
    
		if EnteredPcapName[-5:] != '.pcap':										# compairing and error generation
			self.ui.LabelResultMsg.setText("Wrong Input please Enter correct")
			self.ui.textBrowser.setText("Please Enter Valid Input")
			return 0
		
		self.ui.LabelResultMsg.setText("Result to be shown here ...")
		self.ui.textBrowser.setText(" ")
		
		os.system("tcpdump -qns 0 -A -r "+str(EnteredPcapName)+" >>pcap_output.txt")

		fd = open("pcap_output.txt")
		data = fd.read()
		fd.close()
		
		fd = open("ListOfExtension")
		ext = fd.read()
		fd.close()

		ext = ext.split("\n")[:-1]
		
		jn = ''
		for i in ext:
			j = i
			if j in data:
				j = j+" "
				jn += "\n\n"+j
				file = re.search(r'[\S]*'+j,data)
				a = str(type(file))
				c = a[7:-2]		
				if c != 'NoneType':
					jn += "\n"+str(file.group())
				else:
					pass

		self.ui.textBrowser.setText(jn)
		os.system("rm -rf *.txt")		
		

	def Object(self):
		EnteredPcapName = self.ui.LineEditFname.toPlainText()

		my_file = Path(str(EnteredPcapName))
		if not my_file.is_file():
			self.ui.textBrowser.setText("Enter valid path ")
			return 0

		
		if EnteredPcapName[-5:] != '.pcap':
			self.ui.LabelResultMsg.setText("Wrong Input please Enter correct")
			self.ui.textBrowser.setText("Please Enter Valid Input")
			return 0
		
		self.ui.LabelResultMsg.setText("Result to be shown here ...")
		self.ui.textBrowser.setText(" ")
		
		os.system("tcpdump -qns 0 -A -r "+str(EnteredPcapName)+" >>pcap_output.txt")
				
		fd = open("pcap_output.txt")
		data = fd.read()
		fd.close()
		
		c = ""
		o =['endobj','JavaScrip','obj','stream','endstream','xref','trailer','startxref','page','JS','OpenAction','AcroForm','JBIG2Decode','RichMedia','Launch']
		
		for i in o:
			c += "\n for "+str(i)+" object count is "+str(data.count(i))+""
		
		self.ui.textBrowser.setText(c)
		os.system("rm -rf *.txt")		

	def Script(self):
		EnteredPcapName = self.ui.LineEditFname.toPlainText()

		my_file = Path(str(EnteredPcapName))
		if not my_file.is_file():
			self.ui.textBrowser.setText("Enter valid path ")
			return 0

		
		if EnteredPcapName[-5:] != '.pcap':
			self.ui.LabelResultMsg.setText("Wrong Input please Enter correct")
			self.ui.textBrowser.setText("Please Enter Valid Input")
			return 0
		
		self.ui.LabelResultMsg.setText("Result to be shown here ...")
		self.ui.textBrowser.setText(" ")

		os.system("parse_pcap -vv "+str(EnteredPcapName)+" >> parseOut.txt")

		fd = open('parseOut.txt')
		data = fd.read()
		fd.close()

		new = data[int(data.find('<script>'))+8:(int(data.find('</script>')))]
		c = new.replace(";",";\n")

		self.ui.textBrowser.setText(c)	
		os.system("rm -rf *.txt")

	def PcapOp(self):
		EnteredPcapName = self.ui.LineEditFname.toPlainText()

		my_file = Path(str(EnteredPcapName))
		if not my_file.is_file():
			self.ui.textBrowser.setText("Enter valid path ")
			return 0

		
		if EnteredPcapName[-5:] != '.pcap':
			self.ui.LabelResultMsg.setText("Wrong Input please Enter correct")
			self.ui.textBrowser.setText("Please Enter Valid Input")
			return 0
		
		self.ui.LabelResultMsg.setText("Result to be shown here ...")
		self.ui.textBrowser.setText(" ")

		os.system("tcpdump -qns 0 -A -r "+str(EnteredPcapName)+" >>pcap_output.txt")
		
		fd = open('pcap_output.txt')
		tmp = fd.read()
		fd.close()
		
		self.ui.textBrowser.setText(tmp)
		os.system("rm -rf *.txt")

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	t = MyWidget()

	sys.exit(app.exec_())
