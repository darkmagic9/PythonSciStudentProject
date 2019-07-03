import sys
from PyQt5.QtWidgets import QApplication , QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QHBoxLayout, QGroupBox , QDialog, QVBoxLayout, QGridLayout
from PyQt5.QtWidgets import QLabel, QTextEdit
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QFormLayout, QLineEdit

from PyQt5.QtWidgets import QSizePolicy, QMainWindow
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from PyQt5.QtCore import Qt

from validator.OperatorValidator import OperatorValidator
from dao.OperatorDAOSqliteImpl import OperatorDAOSqliteImpl
from model.Operator import Operator



class OperatorDetailsWindow(QDialog):
    """
    With this class the details of one selected Operator is shown.
    
    """

    def __init__(self, data):
        """
        constructor 
        :param data: list of Operator properties as string  
        """
        super().__init__()
        self.data = data
        self.title = "Operator Details"
        self.left , self.top , self.width , self.height = 50, 50, 500, 500
        self.validator = OperatorValidator()
        self.dao = OperatorDAOSqliteImpl()
        self.initGUI()



    def initGUI(self):
        """
        initializes GUI
        :return: 
        """
        self.setWindowTitle(self.title)
        self.setGeometry(self.left , self.top, self.width , self.height)
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
        self.lblTitle = QLabel("Operator Details")
        self.lblEmpty = QLabel()

        # enrolmentNumber
        self.lblID = QLabel("ID: ")
        self.editID = QLineEdit()

        # firstName
        self.lblCode = QLabel("Code: ")
        self.editCode = QLineEdit()


        # lastName
        self.lblLastName = QLabel("LastName: ")
        self.editLastName = QLineEdit()

        # dob
        self.lblValidation = QLabel("Validation: ")
        self.editValidation = QLineEdit()

        # faculty
        self.lblRemark = QLabel("Remark: ")
        self.editRemark = QLineEdit()

        # buttons
        self.btnClose = QPushButton("Close")

        # add all rows to mainLayout
        self.mainLayout.addRow(self.lblEmpty, self.lblTitle)
        self.mainLayout.addRow(self.lblID, self.editID)
        self.mainLayout.addRow(self.lblCode, self.editCode)
        self.mainLayout.addRow(self.lblLastName, self.editLastName)
        self.mainLayout.addRow(self.lblValidation, self.editValidation)
        self.mainLayout.addRow(self.lblRemark, self.editRemark)
        self.mainLayout.addRow(QLabel(), self.btnClose)

        self.editID.setText(self.data[0])
        self.editCode.setText(self.data[9])
        self.editLastName.setText(self.data[10])
        self.editValidation.setText(self.data[11])
        self.editRemark.setText(self.data[12])

        self.editID.setReadOnly(True)
        self.editCode.setReadOnly(True)
        self.editLastName.setReadOnly(True)
        self.editValidation.setReadOnly(True)
        self.editRemark.setReadOnly(True)

    def registerEvents(self):
        """
        registers events
        :return: 
        """
        self.btnClose.clicked.connect(self.onBtnCloseClicked)




    @pyqtSlot()
    def onBtnCloseClicked(self):
        """
        Slot for signal-slot handling .
        Gets invoked when btnClose is clicked.
        
        :return: 
        """
        self.close()
