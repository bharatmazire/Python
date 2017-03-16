#!/usr/bin/python
from PyQt4 import QtCore, QtGui, uic

import sys

class MyWidget(QtGui.QMainWindow):
    
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = uic.loadUi('sqr_cube.ui', self)
        self.ui.setWindowTitle("This is Square and cube!!!")
        self.ui.show()
        #self.connect(self.ui.btnShowMessage, QtCore.SIGNAL("clicked()"), self.addition)
        self.sqr_btn.clicked.connect(self.square)
        self.cube_btn.clicked.connect(self.cube)

    def square(self):
        val1 = self.ui.spin_accept.value()
        #val2 = self.editCell.text()
        self.ui.result_text.setText(str(val1**2))

    def cube(self):
        val1 = self.ui.spin_accept.value()
        #val2 = self.editCell.text()
        self.ui.result_text.setText(str(val1**3))



if __name__=="__main__":
    app = QtGui.QApplication(sys.argv)
    
    t = MyWidget()
    sys.exit(app.exec_())
