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
        self.lblEnrolmentNumber = QLabel("EnrolmentNumber: ")
        self.editEnrolmentNumber = QLineEdit()

        # firstName
        self.lblFirstName = QLabel("FirstName: ")
        self.editFirstName = QLineEdit()


        # lastName
        self.lblLastName = QLabel("LastName: ")
        self.editLastName = QLineEdit()

        # dob
        self.lblDob = QLabel("DateOfBirth: ")
        self.editDob = QLineEdit()

        # faculty
        self.lblFaculty = QLabel("Faculty: ")
        self.editFaculty = QLineEdit()

        # email
        self.lblEmail = QLabel("Email: ")
        self.editEmail = QLineEdit()

        # buttons
        self.btnClose = QPushButton("Close")

        # add all rows to mainLayout
        self.mainLayout.addRow(self.lblEmpty, self.lblTitle)
        self.mainLayout.addRow(self.lblEnrolmentNumber, self.editEnrolmentNumber)
        self.mainLayout.addRow(self.lblFirstName, self.editFirstName)
        self.mainLayout.addRow(self.lblLastName, self.editLastName)
        self.mainLayout.addRow(self.lblDob, self.editDob)
        self.mainLayout.addRow(self.lblFaculty, self.editFaculty)
        self.mainLayout.addRow(self.lblEmail, self.editEmail)
        self.mainLayout.addRow(QLabel(), self.btnClose)

        self.editEnrolmentNumber.setText(self.data[0])
        self.editFirstName.setText(self.data[1])
        self.editLastName.setText(self.data[2])
        self.editDob.setText(self.data[3])
        self.editFaculty.setText(self.data[4])
        self.editEmail.setText(self.data[5])

        self.editEnrolmentNumber.setReadOnly(True)
        self.editFirstName.setReadOnly(True)
        self.editLastName.setReadOnly(True)
        self.editDob.setReadOnly(True)
        self.editFaculty.setReadOnly(True)
        self.editEmail.setReadOnly(True)

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
