import sys
from PyQt5.QtWidgets import QApplication , QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, QItemSelectionModel
from PyQt5.QtWidgets import QHBoxLayout, QGroupBox , QDialog, QVBoxLayout, QGridLayout, QComboBox
from PyQt5.QtWidgets import QLabel, QTextEdit
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QFormLayout, QLineEdit

from PyQt5.QtWidgets import QSizePolicy, QMainWindow
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

from PyQt5.QtWidgets import QMenuBar, QMenu, QAction

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QAbstractItemView, QFileDialog
from PyQt5 import QtWidgets

from dao.StudentDAOSqliteImpl import StudentDAOSqliteImpl
from model.Student import Student
from mapper.StudentListMapper import StudentListMapper
from gui.StudentSaveWindow import StudentSaveWindow
from gui.StudentUpdateWindow import StudentUpdateWindow
from gui.StudentDetailsWindow import StudentDetailsWindow

from serializer.StudentXMLSerializer import StudentXMLSerializer
from serializer.StudentJSONSerializer import StudentJSONSerializer
from serializer.StudentCSVSerializer import StudentCSVSerializer
from serializer.StudentPDFSerializer import StudentPDFSerializer

from PyQt5 import QtGui

from gui.StudentFindAllWindow import StudentFindAllWindow
from others.SimpleConverter import SimpleConverter

class LoginWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.title = "Login Window"
        self.left , self.top, self.width , self.height = 10 , 10, 500, -1
        # self.data = self.generate_units()
        self.initGUI()


    def initGUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowModality(Qt.ApplicationModal)
        self.addComponents()
        self.registerEvents()

    def addComponents(self):
        self.mainLayout = QFormLayout()
        self.setLayout(self.mainLayout)

        # title
        self.lblTitle = QLabel("Login Window")
        self.mainLayout.addRow(QLabel(), self.lblTitle)
        # username
        self.lblUsername = QLabel("Username: ")
        self.editUserName = QLineEdit()
        self.mainLayout.addRow(self.lblUsername, self.editUserName)
        # password
        self.lblPassword = QLabel("Password: ")
        self.editPassword = QLineEdit()
        self.editPassword.setEchoMode(QLineEdit.Password)
        self.mainLayout.addRow(self.lblPassword, self.editPassword)
        # buttons
        self.btnLogin = QPushButton("Login")
        self.btnClear = QPushButton("Clear")
        self.mainLayout.addRow(self.btnLogin, self.btnClear)

    def registerEvents(self):
        self.btnLogin.clicked.connect(self.onBtnLoginClicked)
        self.btnClear.clicked.connect(self.onBtnClearClicked)

    @pyqtSlot()
    def onBtnLoginClicked(self):
        try:
            username = self.editUserName.text()
            password = self.editPassword.text()
            if username != "foo" or password != "bar":
                raise Exception("Username or Password was not correct.")

            window = StudentFindAllWindow()
            self.hide()
            window.show()
            window.exec_()
        except Exception as err:
            QMessageBox.critical(self, "<<Login Error>>", str(err))


    @pyqtSlot()
    def onBtnClearClicked(self):
        self.editUserName.setText("")
        self.editPassword.setText("")




app = QApplication(sys.argv)
runner = LoginWindow()
runner.show()
sys.exit(app.exec_())