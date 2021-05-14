from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from db_handler import *
from productshow import Ui_Productshow
from stockwindow_logic import *


class ProductWindow(QtWidgets.QMainWindow, Ui_Productshow):
	def __init__(self, *args, obj=None, **kwargs):
		super(ProductWindow, self).__init__(*args, **kwargs)
		self.setupUi(self)
		self.value = QLineEdit()
		self.row_count = 0
		self.checked_list = []
		self.barcode_list = []
		self.selected_barcode = []
		self.method = 0


		# Activation for close_button
		self.close_button.clicked.connect(self.close_button_clicked)

		self.sell_button.clicked.connect(partial(self.sell_button_clicked),self.method)

		self.retired_button.clicked.connect(partial(self.sell_button_clicked),self.method + 1)



	def get_checked_products(self):
		if self.row_count == 0:
			return(0)
		else:
			for i in range(self.row_count):
				if self.show_prices.item(i,2).checkState() == Qt.Checked:
					self.checked_list.append(self.show_prices.item(i,0).text())
					self.selected_barcode.append(self.barcode_list[i])


	def sell_button_clicked(self,method):
		self.get_checked_products()
		i = 0
		status = "VENDIDA"
		if method == 1:
			status = "ENTREGADA"	
		for item in self.checked_list:
			add_sale(item,self.quantity.text(),self.selected_barcode[i],status)
			i = i + 1
		selected_barcode = []	



	def close_button_clicked(self):
		self.close()

	def send_data_to_table(self,item):
		self.barcode_list = []
		product = show_product(item,0)
		self.row_count = 0
		self.show_prices.setRowCount(0)
		for row_number, row_data, in enumerate(product):
			self.show_prices.insertRow(row_number)
			self.row_count = self.row_count + 1
			for column_number, data in enumerate(row_data):
				#print("Numero de columna es {} y data es {}".format(column_number,data))
				if column_number == 2:
					self.barcode_list.append(data)
				item = QTableWidgetItem(str(data))
				item.setTextAlignment(Qt.AlignCenter)
				font = QtGui.QFont()
				font.setPointSize(18)
				item.setFont(font)
				self.show_prices.setItem(row_number,column_number,item)
			check_box_item = QTableWidgetItem()
			check_box_item.setCheckState(Qt.Unchecked)
			check_box_item.setText("Seleccionar")
			font = QtGui.QFont()
			font.setPointSize(18)
			check_box_item.setFont(font)
			self.show_prices.setItem(row_number,2,check_box_item)
		self.show_prices.resizeColumnsToContents()
#		print(self.barcode_list)

	def get_value(self,item):
		self.send_data_to_table(item)


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	ProductWindow = ProductWindow()
	ProductWindow.show()
	sys.exit(app.exec_())
