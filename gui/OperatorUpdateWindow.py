import sys
from PyQt5.QtWidgets import QApplication , QWidget, QPushButton
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



class OperatorUpdateWindow(QDialog):
    """
    With this class QDialog for updating the selected model.Operator into database 
    is shown.

    """

    def __init__(self, selectedItems):
        """
        constructor 
        
        :param selectedItems:list of QTableWidget-s  
        """
        super().__init__()
        self.selectedItems = selectedItems
        self.title = "Update The Selected Operator"
        self.left , self.top , self.width , self.height = 50, 50, 500, 500
        self.validator = OperatorValidator()
        self.dao = OperatorDAOPymysqlImpl()
        self.initGUI()
        self.setWindowModality(Qt.ApplicationModal)


    def initGUI(self):
        """
        initializes GUI
        :return: 
        """
        self.setWindowTitle(self.title)
        self.setGeometry(self.left , self.top, self.width , self.height)
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
        self.lblTitle = QLabel("Update The Selected Operator")
        self.lblEmpty = QLabel()

        # id
        self.lblId = QLabel("Id: ")
        self.editId = QLineEdit()

        # code
        self.lblCode = QLabel("Code: ")
        self.editCode = QLineEdit()


        # name
        self.lblName = QLabel("Name: ")
        self.editName = QLineEdit()

        # validation
        self.lblValidation = QLabel("Validation: ")
        self.editValidation = QComboBox()
        self.editValidation.addItem("N")
        self.editValidation.addItem("Y")

        # remark
        self.lblRemark = QLabel("Remark: ")
        self.editRemark = QLineEdit()

        # buttons
        self.btnUpdate = QPushButton("Update")
        self.btnCancel = QPushButton("Cancel")

        # add all rows to mainLayout
        self.mainLayout.addRow(self.lblEmpty, self.lblTitle)
        self.mainLayout.addRow(self.lblId, self.editId)
        self.mainLayout.addRow(self.lblCode, self.editCode)
        self.mainLayout.addRow(self.lblName, self.editName)
        self.mainLayout.addRow(self.lblValidation, self.editValidation)
        self.mainLayout.addRow(self.lblRemark, self.editRemark)
        self.mainLayout.addRow(self.btnUpdate, self.btnCancel)

        data = [selectedItem.text() for selectedItem in self.selectedItems]
        self.editId.setText(data[0])
        self.editCode.setText(data[9])
        self.editName.setText(data[10])
        self.editValidation.setCurrentText(data[11])
        self.editRemark.setText(data[12])
        self.editId.setReadOnly(True)


    def registerEvents(self):
        """
        registers events
        :return: 
        """
        self.btnUpdate.clicked.connect(self.onBtnUpdateClicked)
        self.btnCancel.clicked.connect(self.onBtnCancelClicked)




    @pyqtSlot()
    def onBtnUpdateClicked(self):
        """
        Slot for signal-slot handling .
        Gets invoked when btnUpdate is clicked.
        :return: 
        """
        try:
            errors = []
            id = self.editId.text()
            code = self.editCode.text()
            name = self.editName.text()
            validation = self.editValidation.itemText(self.editValidation.currentIndex())
            remark = self.editRemark.text()
            if not self.validator.validateId(id):
                errors.append("id is incorrect.")

            if not self.validator.validateCode(code):
                errors.append("code is incorrect.")

            if not self.validator.validateName(name):
                errors.append("name is incorrect.")

            if not self.validator.validateValidation(validation):
                errors.append("DateOfBirth is incorrect.")

            if not self.validator.validateRemark(remark):
                errors.append("Remark is incorrect.")

            if len(errors) > 0 :
                raise Exception("\n".join(errors))


            self.dao.update(id, Operator(id, "", "", "", "", "", "", "", "", code, name,
                                  validation, remark))


            self.selectedItems[0].setText(id)
            self.selectedItems[1].setText(code)
            self.selectedItems[2].setText(name)
            self.selectedItems[3].setText(validation)
            self.selectedItems[4].setText(remark)

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
