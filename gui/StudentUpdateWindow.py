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

from validator.StudentValidator import StudentValidator
from dao.StudentDAOPymysqlImpl import StudentDAOPymysqlImpl
from model.Student import Student



class StudentUpdateWindow(QDialog):
    """
    With this class QDialog for updating the selected model.Student into database 
    is shown.

    """

    def __init__(self, selectedItems):
        """
        constructor 
        
        :param selectedItems:list of QTableWidget-s  
        """
        super().__init__()
        self.selectedItems = selectedItems
        self.title = "Update The Selected Student"
        self.left , self.top , self.width , self.height = 50, 50, 500, 500
        self.validator = StudentValidator()
        self.dao = StudentDAOPymysqlImpl()
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
        self.lblTitle = QLabel("Update The Selected Student")
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
        self.btnUpdate = QPushButton("Update")
        self.btnCancel = QPushButton("Cancel")

        # add all rows to mainLayout
        self.mainLayout.addRow(self.lblEmpty, self.lblTitle)
        self.mainLayout.addRow(self.lblEnrolmentNumber, self.editEnrolmentNumber)
        self.mainLayout.addRow(self.lblFirstName, self.editFirstName)
        self.mainLayout.addRow(self.lblLastName, self.editLastName)
        self.mainLayout.addRow(self.lblDob, self.editDob)
        self.mainLayout.addRow(self.lblFaculty, self.editFaculty)
        self.mainLayout.addRow(self.lblEmail, self.editEmail)
        self.mainLayout.addRow(self.btnUpdate, self.btnCancel)

        data = [selectedItem.text() for selectedItem in self.selectedItems]
        self.editEnrolmentNumber.setText(data[0])
        self.editFirstName.setText(data[1])
        self.editLastName.setText(data[2])
        self.editDob.setText(data[3])
        self.editFaculty.setText(data[4])
        self.editEmail.setText(data[5])
        self.editEnrolmentNumber.setReadOnly(True)


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
            enrolmentNumber = self.editEnrolmentNumber.text()
            firstName = self.editFirstName.text()
            lastName = self.editLastName.text()
            dob = self.editDob.text()
            faculty = self.editFaculty.text()
            email = self.editEmail.text()
            if not self.validator.validateEnrolmentNumber(enrolmentNumber):
                errors.append("enrolmentNumber is incorrect.")

            if not self.validator.validateFirstName(firstName):
                errors.append("firstName is incorrect.")

            if not self.validator.validateLastName(lastName):
                errors.append("lastName is incorrect.")

            if not self.validator.validateDob(dob):
                errors.append("DateOfBirth is incorrect.")

            if not self.validator.validateFaculty(faculty):
                errors.append("Faculty is incorrect.")

            if not self.validator.validateEmail(email):
                errors.append("Email is incorrect.")

            if len(errors) > 0 :
                raise Exception("\n".join(errors))


            self.dao.update(enrolmentNumber, Student(enrolmentNumber, firstName, lastName,
                                  dob, faculty, email))


            # self.selectedItems[0].setText(enrolmentNumber)
            # self.selectedItems[1].setText(firstName)
            # self.selectedItems[2].setText(lastName)
            # self.selectedItems[3].setText(dob)
            # self.selectedItems[4].setText(faculty)
            # self.selectedItems[5].setText(email)

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
