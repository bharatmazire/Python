import string as s
import random as rm
from PyQt4 import QtCore , QtGui, uic
import sys

class MyWidget(QtGui.QMainWindow):

	captcha = ''

	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		self.ui = uic.loadUi('Captcha.ui',self)
		self.ui.setWindowTitle("CAPTCHA ")
		self.ui.show()
		MyWidget.captcha = ''.join(rm.choice(s.letters+s.letters) for i in range(10))
		self.ui.Captcha_generated.setText(MyWidget.captcha)
		self.check_btn.clicked.connect(self.capt)
	
	def capt(self,captcha):
		EnteredValue = self.ui.EnterTextEdit.toPlainText()
		print (MyWidget.captcha , str(EnteredValue))
		if MyWidget.captcha == EnteredValue:
			self.ui.result_text.setText("Mathced !!!")
		else:
			self.ui.result_text.setText("Not Matched !!!")

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
    
	t = MyWidget()
	sys.exit(app.exec_())