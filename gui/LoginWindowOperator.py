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
sys.path.append('.')
from dao.OperatorDAOSqliteImpl import OperatorDAOSqliteImpl
from model.Operator import Operator
from mapper.OperatorListMapper import OperatorListMapper
from gui.OperatorSaveWindow import OperatorSaveWindow
from gui.OperatorUpdateWindow import OperatorUpdateWindow
from gui.OperatorDetailsWindow import OperatorDetailsWindow

from serializer.OperatorXMLSerializer import OperatorXMLSerializer
from serializer.OperatorJSONSerializer import OperatorJSONSerializer
from serializer.OperatorCSVSerializer import OperatorCSVSerializer
from serializer.OperatorPDFSerializer import OperatorPDFSerializer

from PyQt5 import QtGui

from gui.OperatorFindAllWindow import OperatorFindAllWindow
from others.SimpleConverter import SimpleConverter
from encryption.UserManager import UserManager
from encryption.User import User
from encryption.Sha256Hasher import Sha256Hasher

class LoginWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.title = "Login Window"
        self.left , self.top, self.width , self.height = 50 , 50, 500, -1
        self.userManager = UserManager()
        self.hasher = Sha256Hasher()
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
        self.lblTitle = QLabel("Login Operator Window")
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


    def checkIfUserExists(self, username, password):
        allUsers = self.userManager.find_all()
        for user in allUsers:
            if(username == user.userName and self.hasher.check_password(user.password, password)):
                return True
        return False

    @pyqtSlot()
    def onBtnLoginClicked(self):
        try:
            username = self.editUserName.text()
            password = self.editPassword.text()

            if not(self.checkIfUserExists(username, password)):
                raise Exception("Username or Password was not correct.")

            window = OperatorFindAllWindow()
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