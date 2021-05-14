from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMainWindow
from main import Ui_MainWindow
from stockwindow_logic import *
from Productshow_logic import *
from modifyproducts_logic import *
from saleswindow_logic import *
from db_handler import *


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        create_sales_db()
        create_stock_db()
        self.setupUi(self)

        # Activation for searchbutton
        self.searchbutton.clicked.connect(self.searchbutton_clicked)

        # Activation for stockbutton(open new windiow)
        self.stockbutton.clicked.connect(self.stockbutton_clicked)

        # Activation for modify(open new window)
        self.modify.clicked.connect(self.modifybutton_clicked)

        #Activation for salesbutton(open new window)
        self.salesbutton.clicked.connect(self.salesbutton_clicked)


    def closeEvent(self, event):
        # Ask for confirmation
        answer = QtWidgets.QMessageBox.question(self,
        "Salir..",
        "Esta seguro que quiere salir?\nSe perdera la informacion no guardada.",
        QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if answer == QtWidgets.QMessageBox.Yes:
            app.quit()
        else:
            event.ignore()

    def searchbutton_clicked(self):
        productwindow = ProductWindow()
        productwindow.get_value(self.searchbar.text())
        productwindow.show()
        self.searchbar.clear()

    def stockbutton_clicked(self):
        stockwindow = StockWindow()
        stockwindow.show()


    def modifybutton_clicked(self):
        modifywindow= ModifyWindow()
        modifywindow.show()


    def salesbutton_clicked(self):
        saleswindow = SalesWindow()
        saleswindow.show()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())