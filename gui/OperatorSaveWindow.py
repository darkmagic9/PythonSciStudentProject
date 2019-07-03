import sys
from PyQt5.QtWidgets import QApplication , QWidget, QPushButton, QTableWidgetItem
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QHBoxLayout, QGroupBox , QDialog, QVBoxLayout, QGridLayout
from PyQt5.QtWidgets import QLabel, QTextEdit
from PyQt5.QtWidgets import QMessageBox, QComboBox
from PyQt5.QtWidgets import QFormLayout, QLineEdit

from PyQt5.QtWidgets import QSizePolicy, QMainWindow
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from PyQt5.QtCore import Qt

from validator.OperatorValidator import OperatorValidator
from dao.OperatorDAOPymysqlImpl import OperatorDAOPymysqlImpl
from model.Operator import Operator



class OperatorSaveWindow(QDialog):
    """
    With this class QDialog for adding new model.Operator into database is shown.
     
    """
    def __init__(self, tableWidget):
        """
        constructor 
        
        :param tableWidget: QTableWidget 
        """
        super().__init__()
        self.tableWidget = tableWidget
        self.title = "Save New Operator"
        self.left , self.top , self.width , self.height = 50, 50, 500, 500
        self.validator = OperatorValidator()
        self.dao = OperatorDAOPymysqlImpl()
        self.initGUI()



    def initGUI(self):
        """
        initializes GUI
        :return: 
        """
        self.setWindowTitle(self.title)
        self.setGeometry(self.left*2 , self.top*2, self.width , self.height/2.2)
        self.setWindowModality(Qt.ApplicationModal)
        self.addComponents()
        self.registerEvents()




    def addComponents(self):
        """
        sets the mainLayout for this class and adds components into it.
        :return: 
        """
        self.mainLayout = QFormLayout()
        self.setLayout(self.mainLayout)
        # title
        self.lblTitle = QLabel("Save New Operator")
        self.lblEmpty = QLabel()

        # code
        self.lblCode = QLabel("Code: ")
        self.editCode = QLineEdit()
        self.editCode.setPlaceholderText("Code")
        self.editCode.setInputMask('99999')


        # name
        self.lblName = QLabel("Name: ")
        self.editName = QLineEdit()
        self.editName.setPlaceholderText("Name")

        # validation
        self.lblValidation = QLabel("Validation: ")
        self.editValidation = QComboBox()
        self.editValidation.addItem("N")
        self.editValidation.addItem("Y")

        # remark
        self.lblRemark = QLabel("Remark: ")
        self.editRemark = QLineEdit()
        self.editRemark.setPlaceholderText("Remark")

        # buttons
        self.btnSave = QPushButton("Save")
        self.btnCancel = QPushButton("Cancel")

        # add all rows to mainLayout
        self.mainLayout.addRow(self.lblEmpty, self.lblTitle)
        self.mainLayout.addRow(self.lblCode, self.editCode)
        self.mainLayout.addRow(self.lblName, self.editName)
        self.mainLayout.addRow(self.lblValidation, self.editValidation)
        self.mainLayout.addRow(self.lblRemark, self.editRemark)
        self.mainLayout.addRow(self.btnSave, self.btnCancel)

    def registerEvents(self):
        """
        registers events
        :return: 
        """
        self.btnSave.clicked.connect(self.onBtnSaveClicked)
        self.btnCancel.clicked.connect(self.onBtnCancelClicked)




    @pyqtSlot()
    def onBtnSaveClicked(self):
        """
        Slot for signal-slot handling .
        Gets invoked when btnSave is clicked.
        :return: 
        """
        try:
            errors = []
            code = self.editCode.text()
            name = self.editName.text()
            validation = self.editValidation.itemText(self.editValidation.currentIndex())
            remark = self.editRemark.text()

            if not self.validator.validateCode(code):
                errors.append("code is incorrect.")

            if not self.validator.validateName(name):
                errors.append("name is incorrect.")

            if not self.validator.validateValidation(validation):
                errors.append("Validation is incorrect.")

            if not self.validator.validateRemark(remark):
                errors.append("Remark is incorrect.")

            if len(errors) > 0 :
                raise Exception("\n".join(errors))


            ret = self.dao.save(Operator(0, "", "", "", "", "", "", "", "", code, name,
                                  validation, remark))

            if ret :
                raise Exception(ret)


            rowPosition = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)
            self.tableWidget.setItem(rowPosition, 10, QTableWidgetItem(code))
            self.tableWidget.setItem(rowPosition, 11, QTableWidgetItem(name))
            self.tableWidget.setItem(rowPosition, 12, QTableWidgetItem(validation))
            self.tableWidget.setItem(rowPosition, 13, QTableWidgetItem(remark))

            self.close()

        except Exception as err:

            QMessageBox.critical(self, "<<Error>>", str(err))





    @pyqtSlot()
    def onBtnCancelClicked(self):
        """
        Slot for signal-slot handling .
        Gets invoked when btnCancel is clicked.
        :return: 
        """
        self.close()
