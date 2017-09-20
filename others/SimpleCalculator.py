from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QGridLayout
from PyQt5.QtWidgets import QLabel, QTextEdit
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QWidget, QPushButton


class SimpleCalculator(QDialog):
    """
    With this class simple calculator app is created.
    
    """
    def __init__(self):
        """
        constructor
        
        """
        super().__init__()
        self.title = "Simple Calculator"
        self.left, self.top, self.width , self.height = 10 , 10, 500, 500
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

        # mainLayout
        self.mainLayout = QVBoxLayout()
        self.setLayout(self.mainLayout)
        # lblTitle
        self.lblTitle = QLabel("Simple Calculator")
        self.mainLayout.addWidget(self.lblTitle)
        # display
        self.editDisplay = QTextEdit()
        self.mainLayout.addWidget(self.editDisplay)
        # controls
        self.controlLayout = QGridLayout()
        self.controlWidget = QWidget()
        self.controlWidget.setLayout(self.controlLayout)
        self.mainLayout.addWidget(self.controlWidget)

        self.controlLayout.setColumnStretch(0, 4)
        self.controlLayout.setColumnStretch(1, 4)
        self.controlLayout.setColumnStretch(2, 4)
        self.controlLayout.setColumnStretch(3, 4)
        self.controlLayout.setColumnStretch(4, 4)
        self.controlLayout.setColumnStretch(5, 4)

        # 7, 8 , 9, /, <- , del
        self.btn7 = QPushButton("7")
        self.btn8 = QPushButton("8")
        self.btn9 = QPushButton("9")
        self.btnDivide = QPushButton("/")
        self.btnBack = QPushButton("<-")
        self.btnDel = QPushButton("del")
        self.controlLayout.addWidget(self.btn7, 0,0)
        self.controlLayout.addWidget(self.btn8, 0, 1)
        self.controlLayout.addWidget(self.btn9, 0, 2)
        self.controlLayout.addWidget(self.btnDivide, 0, 3)
        self.controlLayout.addWidget(self.btnBack, 0, 4)
        self.controlLayout.addWidget(self.btnDel , 0, 5)

        # 4,5,6,*,(,)
        self.btn4 = QPushButton("4")
        self.btn5 = QPushButton("5")
        self.btn6 = QPushButton("6")
        self.btnMultiply = QPushButton("*")
        self.btnLeftParen = QPushButton("(")
        self.btnRightParen = QPushButton(")")
        self.controlLayout.addWidget(self.btn4, 1, 0)
        self.controlLayout.addWidget(self.btn5, 1, 1)
        self.controlLayout.addWidget(self.btn6, 1, 2)
        self.controlLayout.addWidget(self.btnMultiply, 1, 3)
        self.controlLayout.addWidget(self.btnLeftParen, 1, 4)
        self.controlLayout.addWidget(self.btnRightParen, 1, 5)

        # 1,2,3,-,x**2, sqrt
        self.btn1 = QPushButton("1")
        self.btn2 = QPushButton("2")
        self.btn3 = QPushButton("3")
        self.btnSubtract = QPushButton("-")
        self.btnSquare = QPushButton("x**2")
        self.btnSqrt = QPushButton("sqrt(x)")
        self.controlLayout.addWidget(self.btn1, 2, 0)
        self.controlLayout.addWidget(self.btn2, 2, 1)
        self.controlLayout.addWidget(self.btn3, 2, 2)
        self.controlLayout.addWidget(self.btnSubtract, 2, 3)
        self.controlLayout.addWidget(self.btnSquare, 2, 4)
        self.controlLayout.addWidget(self.btnSqrt, 2, 5)

        # 0, . , %, + , =
        self.btn0 = QPushButton("0")
        self.btnDot = QPushButton(".")
        self.btnModulo = QPushButton("%")
        self.btnAdd = QPushButton("+")
        self.btnEqual = QPushButton("=")
        self.controlLayout.addWidget(self.btn0, 3, 0)
        self.controlLayout.addWidget(self.btnDot, 3, 1)
        self.controlLayout.addWidget(self.btnModulo, 3, 2)
        self.controlLayout.addWidget(self.btnAdd, 3, 3)
        self.controlLayout.addWidget(self.btnEqual, 3, 4,1, 2)



    def registerEvents(self):
        """
        registers events
        :return: 
        """

        self.btn0.clicked.connect(self.onDigitOrParenClicked)
        self.btn1.clicked.connect(self.onDigitOrParenClicked)
        self.btn2.clicked.connect(self.onDigitOrParenClicked)
        self.btn3.clicked.connect(self.onDigitOrParenClicked)
        self.btn4.clicked.connect(self.onDigitOrParenClicked)
        self.btn5.clicked.connect(self.onDigitOrParenClicked)
        self.btn6.clicked.connect(self.onDigitOrParenClicked)
        self.btn7.clicked.connect(self.onDigitOrParenClicked)
        self.btn8.clicked.connect(self.onDigitOrParenClicked)
        self.btn9.clicked.connect(self.onDigitOrParenClicked)
        self.btnLeftParen.clicked.connect(self.onDigitOrParenClicked)
        self.btnRightParen.clicked.connect(self.onDigitOrParenClicked)

        self.btnAdd.clicked.connect(self.onBinaryOperatorClicked)
        self.btnSubtract.clicked.connect(self.onBinaryOperatorClicked)
        self.btnMultiply.clicked.connect(self.onBinaryOperatorClicked)
        self.btnDivide.clicked.connect(self.onBinaryOperatorClicked)
        self.btnModulo.clicked.connect(self.onBinaryOperatorClicked)

        self.btnSquare.clicked.connect(self.onBtnSquareClicked)
        self.btnSqrt.clicked.connect(self.onBtnSqrtClicked)

        self.btnBack.clicked.connect(self.onBtnBackClicked)
        self.btnDel.clicked.connect(self.onBtnDelClicked)
        self.btnEqual.clicked.connect(self.onBtnEqualClicked)


    @pyqtSlot()
    def onDigitOrParenClicked(self):
        """
        Slot for signal-slot handling .
        Gets invoked when btn0|btn1|btn2|btn3|btn4|btn5|btn6|btn7|btn8
         |btn9|btnLeftParen|btnRightParen are clicked.
         
        :return: 
        """

        text = self.sender().text()
        content = self.editDisplay.toPlainText()
        content = "{0}{1}".format(content,text)
        self.editDisplay.setText(content)

    @pyqtSlot()
    def onBinaryOperatorClicked(self):
        """
        Slot for signal-slot handling .
        Gets invoked when btnAdd|btnSubtract|btnMultiply|btnDivide
        |btnModulo are clicked.
        
        :return: 
        """

        text = self.sender().text()
        content = self.editDisplay.toPlainText()
        content = "{0} {1}".format(content, text)
        self.editDisplay.setText(content)


    @pyqtSlot()
    def onBtnSquareClicked(self):
        """
        Slot for signal-slot handling .
        Gets invoked when btnSquare is clicked.
        :return: 
        """
        content = self.editDisplay.toPlainText()
        if(len(content) == 0): return
        content = "({0}) ** 2".format(content)
        self.editDisplay.setText(content)

    @pyqtSlot()
    def onBtnSqrtClicked(self):
        """
        Slot for signal-slot handling .
        Gets invoked when btnSqrt is clicked.
        
        :return: 
        """
        content = self.editDisplay.toPlainText()
        if (len(content) == 0): return
        content = "sqrt({0})".format(content)
        self.editDisplay.setText(content)


    @pyqtSlot()
    def onBtnBackClicked(self):
        """
        Slot for signal-slot handling .
        Gets invoked when btnBack is clicked.
        
        :return: 
        """
        content = self.editDisplay.toPlainText()
        if (len(content) == 0): return
        content = content[0:len(content)-1]
        self.editDisplay.setText(content)

    @pyqtSlot()
    def onBtnDelClicked(self):
        """
        Slot for signal-slot handling .
        Gets invoked when btnDel is clicked.
        
        :return: 
        """
        self.editDisplay.setText("")

    @pyqtSlot()
    def onBtnEqualClicked(self):
        """
        Slot for signal-slot handling .
        Gets invoked when btnEqual is clicked.
        
        :return: 
        """
        try:
            content = self.editDisplay.toPlainText()
            ret = eval(content)
            content = "{0} = {1}".format(content, ret)
            self.editDisplay.setText(content)
        except Exception as err:
            title = "<<Error>>"
            # msg = str(err)
            msg = "Malformed Expression"
            QMessageBox.critical(self, title, msg)



