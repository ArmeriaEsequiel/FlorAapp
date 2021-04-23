from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class MyWindow(QMainWindow):
	def __init__(self):
		super(MyWindow,self).__init__()
		self.setGeometry(200, 200, 1000, 1000)
		self.setWindowTitle("Mi Stock")
		self.initUI()

	def initUI(self):
		self.label = QtWidgets.QLabel(self)
		self.label.setText("TEST2")
		self.label.move(300,300)		













def window():
	app = QApplication(sys.argv)
	win =  MyWindow()
	win.show()
	sys.exit(app.exec_())

window()