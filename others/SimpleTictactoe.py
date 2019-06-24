import sys
from PyQt5.QtWidgets import QApplication , QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, QItemSelectionModel
from PyQt5.QtWidgets import QHBoxLayout, QGroupBox , QDialog, QVBoxLayout, QGridLayout, QComboBox
from PyQt5.QtWidgets import QLabel, QTextEdit
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QSizePolicy, QMainWindow, QStackedWidget
from PyQt5.QtCore import Qt
import numpy as np


class SimpleTictactoe(QDialog):
    """
    With this class simple tictactoe game-app is created.

    """
    def __init__(self):
        """
        constructor
        
        """
        super().__init__()
        self.title = "Simple Tictactoe"
        self.left , self.top , self.width , self.height = 50, 50, -1, -1
        self.initGUI()

    def initGUI(self):
        """
        initializes GUI

        :return: 
        """

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowModality(Qt.ApplicationModal)
        self.addComponents()
        self.registerEvents()

    def addComponents(self):
        """
        sets the mainLayout for this class and adds components into it.
        :return: 
        """

        self.mainLayout = QVBoxLayout()
        # comboChooser
        self.widgetChooser = QWidget()
        self.layoutChooser = QHBoxLayout()
        self.widgetChooser.setLayout(self.layoutChooser)
        self.mainLayout.addWidget(self.widgetChooser)
        self.lblChooser = QLabel("Choose the tictactoe row x column: ")
        self.comboChooser = QComboBox()
        self.comboChooser.addItems([
            "Tictactoe 3x3",
            "Tictactoe 5x5",
            "Tictactoe 7x7"
        ])
        self.layoutChooser.addWidget(self.lblChooser)
        self.layoutChooser.addWidget(self.comboChooser)

        self.setLayout(self.mainLayout)
        self.tictactoe3 = TictactoeWidget()
        self.tictactoe5 = TictactoeWidget( 5, 5)
        self.tictactoe7 = TictactoeWidget(7,7)
        # self.tictactoe9 = TictactoeWidget(9, 9)
        # self.tictactoe11 = TictactoeWidget(11, 11)
        # self.tictactoe13 = TictactoeWidget(13, 13)

        #  stackedWidget
        self.stackedWidget = QStackedWidget()
        self.mainLayout.addWidget(self.stackedWidget)
        self.stackedWidget.addWidget(self.tictactoe3)
        self.stackedWidget.addWidget(self.tictactoe5)
        self.stackedWidget.addWidget(self.tictactoe7)
        # self.stackedWidget.addWidget(self.tictactoe9)
        # self.stackedWidget.addWidget(self.tictactoe11)
        # self.stackedWidget.addWidget(self.tictactoe13)

    def registerEvents(self):
        """
        registers events
        :return: 
        """
        self.comboChooser.currentIndexChanged.connect(self.onCurrentIndexChanged)


    @pyqtSlot()
    def onCurrentIndexChanged(self):
        """
        Slot for signal-slot handling .
        Gets invoked when in comboChooser currentIndexChanged event 
        is triggered.
        :return: 
        """
        currentIndex = self.sender().currentIndex()
        self.stackedWidget.setCurrentIndex(currentIndex)


class TictactoeWidget(QWidget):
    """
    This class is used by SimpleTictactoe class 
    
    """
    def __init__(self, shapeRow= 3, shapeColumn= 3):
        """
        constructor 
        
        :param shapeRow: int  
        :param shapeColumn: int 
        """
        super().__init__()
        self.title = "Tictactoe {0}x{1}".format(shapeRow, shapeColumn)
        self.shapeRow = shapeRow
        self.shapeColumn = shapeColumn
        self.initGUI()


    def initGUI(self):
        """
        initializes GUI

        :return: 
        """

        self.addComponents()
        self.registerEvents()

    def addComponents(self):
        """
        sets the mainLayout for this class and adds components into it.
        :return: 
        """

        self.mainLayout = QVBoxLayout()
        self.setLayout(self.mainLayout)
        # title
        self.lblTitle = QLabel(self.title)
        self.mainLayout.addWidget(self.lblTitle)
        styleTitle = """
font-size: 20px; 
font-style:italic; 
font-weight: bold; 
margin:auto;
margin-bottom: 1px; 
"""
        self.lblTitle.setStyleSheet(styleTitle)

        # controls
        self.widgetControls = QWidget()
        self.layoutControls = QGridLayout()
        # self.layoutControls.setColumnStretch(0, 4)
        # self.layoutControls.setColumnStretch(1, 4)
        # self.layoutControls.setColumnStretch(2, 4)

        self.widgetControls.setLayout(self.layoutControls)
        self.mainLayout.addWidget(self.widgetControls)

        # buttons
        styleControls = """
        width: 60px; 
        height: 50px; 
        """
        self.buttons = []
        for i in range(self.shapeRow):
            self.buttons.append(self.generateColumnButtons())

        for i in range(self.shapeRow):
            for j in range(self.shapeColumn):
                self.buttons[i][j].setStyleSheet(styleControls)
                self.layoutControls.addWidget(self.buttons[i][j], i, j)




    def generateColumnButtons(self):
        """
        Generates list of buttons for one row
        :return: list of QPushButton-s 
        """
        ret = []
        for i in range(self.shapeColumn):
            ret.append(QPushButton(" "))

        return ret


    def registerEvents(self):
        """
        registers events
        :return: 
        """

        self.firstPlayer = True
        for i in range(self.shapeRow):
            for j in range(self.shapeColumn):
                self.buttons[i][j].clicked.connect(self.game)



    @pyqtSlot()
    def game(self):
        """
        Slot for signal-slot handling .
        Gets invoked when any button in self.buttons list is clicked.
        :return: 
        """
        sender = self.sender()
        if(sender.text() == " "):
            sender.setText("x" if self.firstPlayer else "0")
            self.firstPlayer = not(self.firstPlayer)
            res = self.checkForResult()
            if(res[0] == True):
                self.endGame(res[1])


    def extractValuesColumn(self, row):
        """
        Extracts list of string-s(text property of QPushButton in self.buttons) 
        for one given row.
        
        :param row: int  
        :return: list of string-s 
        """

        ret = []
        for j in range(self.shapeColumn):
            ret.append(self.buttons[row][j].text())

        return ret

    def checkForResult(self):
        """
        Checks whether one of the 2 players won. If yes, then it calls self.endGame() 
        with approriate message string 
        
        :return: Tuple(boolean , string)
        """
        values = np.array([self.extractValuesColumn(0)])
        for i in range(1, self.shapeRow):
            values = np.vstack((values, self.extractValuesColumn(i)))


        for i in range(self.shapeRow):
            if(values[i, ::] == 'x').all() or \
            (values[::, i] == 'x').all():
                return (True, "Player x won.")

        if (values.diagonal() == 'x').all() or \
        (np.diag(np.fliplr(values)) == 'x').all():
            return (True, "Player x won.")


        #check for 0
        for i in range(self.shapeRow):
            if (values[i, ::] == '0').all() or \
                    (values[::, i] == '0').all():
                return (True, "Player 0 won.")

        if (values.diagonal() == '0').all() or \
                (np.diag(np.fliplr(values)) == '0').all():
            return (True, "Player 0 won.")


        return (False, "")


    def endGame(self, msg):
        """
        Shows Information QMessageBox to the players and
         calls self.reset()
        :param msg: 
        :return: 
        """
        title = "Game Over"
        QMessageBox.information(self, title, msg)
        self.reset()


    def reset(self):
        """
        Resets the value of text property of QPushButton-s in self.buttons to the 
        initial value 
        
        :return: 
        """
        for i in range(self.shapeRow):
            for j in range(self.shapeColumn):
                self.buttons[i][j].setText(" ")


