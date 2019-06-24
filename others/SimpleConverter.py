import sys
from PyQt5.QtWidgets import QApplication , QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, QItemSelectionModel
from PyQt5.QtWidgets import QHBoxLayout, QGroupBox , QDialog, QVBoxLayout, QGridLayout, QComboBox
from PyQt5.QtWidgets import QLabel, QTextEdit
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QFormLayout, QLineEdit


from PyQt5.QtCore import Qt



class SimpleConverter(QDialog):
    """
    With this class simple unit converter app is created.
    
    """

    def __init__(self):
        """
        constructor

        """
        super().__init__()
        self.title = "Simple Converter"
        self.left , self.top, self.width , self.height = 50 , 50, 500, -1
        self.data = self.generate_units()
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
        # title
        self.lblTitle = QLabel("Simple Converter")
        self.mainLayout.addWidget(self.lblTitle)

        # comboCategoryChooser
        self.lblCategoryChooser = QLabel("Choose A Category...")
        self.comboCategoryChooser = QComboBox()
        self.comboCategoryChooser.addItems(["Volumes",
            "Distances",
            "Weights",
            "Temperatures",
            "Areas" ,
            "Times"
        ])

        self.mainLayout.addWidget(self.lblCategoryChooser)
        self.mainLayout.addWidget(self.comboCategoryChooser)


        # control
        self.controlWidget = QWidget()
        self.controlLayout = QHBoxLayout()
        self.controlWidget.setLayout(self.controlLayout)
        self.mainLayout.addWidget(self.controlWidget)

        # comboFrom
        self.widgetFrom = QWidget()
        self.layoutFrom = QFormLayout()
        self.widgetFrom.setLayout(self.layoutFrom)
        self.controlLayout.addWidget(self.widgetFrom)
        # label , combo  and lineEdit
        self.lblFrom = QLabel("From")
        self.comboFrom = QComboBox()
        self.editFrom = QLineEdit()
        self.layoutFrom.addRow(self.lblFrom, self.comboFrom)
        self.layoutFrom.addRow(QLabel(), self.editFrom)
        self.comboFrom.addItems(self.data[self.comboCategoryChooser.currentText()])

        # comboTo
        self.widgetTo = QWidget()
        self.layoutTo = QFormLayout()
        self.widgetTo.setLayout(self.layoutTo)
        self.controlLayout.addWidget(self.widgetTo)
        # label , combo  and lineEdit
        self.lblTo = QLabel("To")
        self.comboTo = QComboBox()
        self.editTo = QLineEdit()
        self.layoutTo.addRow(self.lblTo, self.comboTo)
        self.layoutTo.addRow(QLabel(), self.editTo)
        self.comboTo.addItems(self.data[self.comboCategoryChooser.currentText()])


        # buttons
        self.widgetButtons = QWidget()
        self.layoutButtons = QHBoxLayout()
        self.widgetButtons.setLayout(self.layoutButtons)
        self.mainLayout.addWidget(self.widgetButtons)
        # btnConvert, btnReset
        self.btnConvert = QPushButton("Convert")
        self.btnReset = QPushButton("Reset")
        self.layoutButtons.addWidget(self.btnConvert)
        self.layoutButtons.addWidget(self.btnReset)



    def registerEvents(self):
        """
        registers events
        :return: 
        """

        # or
        # self.comboCategoryChooser.currentTextChanged.connect(self.onComboCategoryChooserChanged)
        self.comboCategoryChooser.currentIndexChanged.connect(self.onComboCategoryChooserChanged)
        self.btnReset.clicked.connect(self.onBtnResetClicked)
        self.btnConvert.clicked.connect(self.onBtnConvertClicked)

    @pyqtSlot()
    def onComboCategoryChooserChanged(self):
        """
        Slot for signal-slot handling .
        Gets invoked when in comboCategoryChooser currentIndexChanged event 
        is triggered.
        :return: 
        """
        currentText = self.sender().currentText()
        self.comboFrom.clear()
        self.comboFrom.addItems(self.data[currentText])
        self.comboTo.clear()
        self.comboTo.addItems(self.data[currentText])


    @pyqtSlot()
    def onBtnConvertClicked(self):
        """
        Slot for signal-slot handling .
        Gets invoked when btnConvert is clicked.
        :return: 
        """
        try:
            currentText = self.comboCategoryChooser.currentText()
            valueFrom = float(self.editFrom.text())
            labelFrom = self.comboFrom.currentText()
            labelTo = self.comboTo.currentText()

            valueTo = None
            if currentText == "Volumes":
                valueTo = self.convertVolumes(labelFrom , labelTo, valueFrom)
            elif currentText == "Distances":
                valueTo = self.convertDistances(labelFrom , labelTo, valueFrom)
            elif currentText == "Weights":
                valueTo = self.convertWeights(labelFrom, labelTo, valueFrom)
            elif currentText == "Temperatures":
                valueTo = self.convertTemperatures(labelFrom , labelTo, valueFrom)
            elif currentText == "Areas":
                valueTo = self.convertAreas(labelFrom, labelTo, valueFrom)
            elif currentText == "Times":
                valueTo = self.convertTimes(labelFrom,labelTo, valueFrom)


            self.editTo.setText(str(valueTo))

        except Exception as err:
            QMessageBox.critical(self, "<<Error>>", str(err))




    def convertTimes(self, fromLabel, toLabel, fromValue):
        """
        Converts time from one unit into another
        
        :param fromLabel: string 
        :param toLabel: string 
        :param fromValue: float
        :return: float 
        """
        if fromLabel == "Microsecond":
            fromValue = fromValue*(10**(-6))
        if fromLabel == "Millisecond":
            fromValue = fromValue*(10**(-3))
        if fromLabel == "Second":
            pass
        if fromLabel == "Minute":
            fromValue = fromValue*60
        if fromLabel == "Hour":
            fromValue = fromValue*(60**2)
        if fromLabel == "Day":
            fromValue = fromValue*(24*(60**2))
        if fromLabel == "Week":
            fromValue = fromValue*(7*24*(60**2))
        if fromLabel == "Year":
            fromValue = fromValue*(52*7*24*(60**2))


        if toLabel == "Microsecond":
            fromValue = fromValue/(10**(-6))
        if toLabel == "Millisecond":
            fromValue = fromValue/(10**(-3))
        if toLabel == "Second":
            pass
        if toLabel == "Minute":
            fromValue = fromValue/60
        if toLabel == "Hour":
            fromValue = fromValue/(60**2)
        if toLabel == "Day":
            fromValue = fromValue/(24*(60**2))
        if toLabel == "Week":
            fromValue = fromValue/(7*24*(60**2))
        if toLabel == "Year":
            fromValue = fromValue/(52*7*24*(60**2))


        return fromValue

    def convertAreas(self, fromLabel, toLabel, fromValue):
        """
        Converts area from one unit into another
        
        :param fromLabel: string  
        :param toLabel: string 
        :param fromValue: float
        :return: float 
        """
        if fromLabel == "Square Millimeter":
            fromValue = fromValue * (10**(-6))
        if fromLabel == "Square Centimeter":
            fromValue = fromValue*(10**(-4))
        if fromLabel == "Square Meter":
            pass
        if fromLabel == "Hectar":
            fromValue = fromValue*(10**4)
        if fromLabel == "Square Kilometer":
            fromValue = fromValue*(10**6)
        if fromLabel == "Square Inch":
            fromValue = fromValue*(645*(10**(-6)))
        if fromLabel == "Square Foot":
            fromValue = fromValue*(92903*(10**(-6)))
        if fromLabel == "Square Yard":
            fromValue = fromValue*(836127*(10**(-6)))
        if fromLabel == "Acre":
            fromValue = fromValue*4046.856
        if fromLabel == "Square Mile":
            fromValue = fromValue*2589988

        if toLabel == "Square Millimeter":
            fromValue = fromValue / (10 ** (-6))
        if toLabel == "Square Centimeter":
            fromValue = fromValue / (10 ** (-4))
        if toLabel == "Square Meter":
            pass
        if toLabel == "Hectar":
            fromValue = fromValue / (10 ** 4)
        if toLabel == "Square Kilometer":
            fromValue = fromValue / (10 ** 6)
        if toLabel == "Square Inch":
            fromValue = fromValue / (645 * (10 ** (-6)))
        if toLabel == "Square Foot":
            fromValue = fromValue / (92903 * (10 ** (-6)))
        if toLabel == "Square Yard":
            fromValue = fromValue / (836127 * (10 ** (-6)))
        if toLabel == "Acre":
            fromValue = fromValue / 4046.856
        if toLabel == "Square Mile":
            fromValue = fromValue / 2589988

        return fromValue

    def convertTemperatures(self, fromLabel, toLabel, fromValue):
        """
        Converts temperature from one unit into another 
        
        :param fromLabel: string  
        :param toLabel: string 
        :param fromValue: float 
        :return: float 
        """
        if fromLabel == "Celcius":
            fromValue = fromValue * 33.8
        if fromLabel == "Fahrenheit":
            pass
        if fromLabel == "Kelvin":
            fromValue = fromValue*(-457.87)


        if toLabel == "Celcius":
            fromValue = fromValue / 33.8
        if toLabel == "Fahrenheit":
            pass
        if toLabel == "Kelvin":
            fromValue = fromValue/(-457.87)

        return fromValue



    def convertWeights(self, fromLabel, toLabel, fromValue):
        """
        Converts weight from one unit into another
        
        :param fromLabel: string  
        :param toLabel:  string 
        :param fromValue: float 
        :return: float 
        """
        if fromLabel == "Carat":
            fromValue = fromValue * 0.2
        if fromLabel == "Milligram":
            fromValue = fromValue *(10**(-3))
        if fromLabel == "Centigram":
            fromValue = fromValue *(10**(-2))
        if fromLabel == "Decigram":
            fromValue = fromValue * 0.1
        if fromLabel == "Gram":
            pass
        if fromLabel == "Decagram":
            fromValue = fromValue*10
        if fromLabel == "Hectogram":
            fromValue = fromValue*100
        if fromLabel == "Kilogram":
            fromValue = fromValue * 1000
        if fromLabel == "Ton":
            fromValue = fromValue*(10**6)
        if fromLabel == "Ounce":
            fromValue = fromValue*28.34952
        if fromLabel == "Pound":
            fromValue = fromValue*453.5924
        if fromLabel == "Stone":
            fromValue = fromValue*6350.293




        if toLabel == "Carat":
            fromValue = fromValue / 0.2
        if toLabel == "Milligram":
            fromValue = fromValue /(10**(-3))
        if toLabel == "Centigram":
            fromValue = fromValue /(10**(-2))
        if toLabel == "Decigram":
            fromValue = fromValue / 0.1
        if toLabel == "Gram":
            pass
        if toLabel == "Decagram":
            fromValue = fromValue/10
        if toLabel == "Hectogram":
            fromValue = fromValue/100
        if toLabel == "Kilogram":
            fromValue = fromValue / 1000
        if toLabel == "Ton":
            fromValue = fromValue/(10**6)
        if toLabel == "Ounce":
            fromValue = fromValue/28.34952
        if toLabel == "Pound":
            fromValue = fromValue/453.5924
        if toLabel == "Stone":
            fromValue = fromValue/6350.293

        return fromValue




    def convertDistances(self, fromLabel, toLabel, fromValue):
        """
        Converts distance from one unit into another
        
        :param fromLabel: string  
        :param toLabel: string 
        :param fromValue: float 
        :return: float 
        """
        if fromLabel == "Nanometer":
            fromValue = fromValue * (10**(-9))
        if fromLabel == "Micrometer":
            fromValue = fromValue * (10**(-6))
        if fromLabel == "Millimeter":
            fromValue = fromValue*(10**(-3))
        if fromLabel == "Centimeter":
            fromValue = fromValue *(10**(-2))
        if fromLabel == "Meter":
            fromValue = fromValue
        if fromLabel == "Kilometer":
            fromValue = fromValue*(10**3)
        if fromLabel == "Inch":
            fromValue = fromValue*(254*(10**(-4)))
        if fromLabel == "Foot":
            fromValue = fromValue*(3048*(10**(-4)))
        if fromLabel == "Yard":
            fromValue = fromValue*(9144*(10**(-4)))
        if fromLabel == "Mile":
            fromValue = fromValue*1609.344
        if fromLabel == "Seemile":
            fromValue = fromValue * 1852



        if toLabel == "Nanometer":
            fromValue = fromValue / (10**(-9))
        if toLabel == "Micrometer":
            fromValue = fromValue / (10**(-6))
        if toLabel == "Millimeter":
            fromValue = fromValue/(10**(-3))
        if toLabel == "Centimeter":
            fromValue = fromValue /(10**(-2))
        if toLabel == "Meter":
            fromValue = fromValue
        if toLabel == "Kilometer":
            fromValue = fromValue/(10**3)
        if toLabel == "Inch":
            fromValue = fromValue/(254*(10**(-4)))
        if toLabel == "Foot":
            fromValue = fromValue/(3048*(10**(-4)))
        if toLabel == "Yard":
            fromValue = fromValue/(9144*(10**(-4)))
        if toLabel == "Mile":
            fromValue = fromValue/1609.344
        if toLabel == "Seemile":
            fromValue = fromValue / 1852

        return fromValue


    def convertVolumes(self, fromLabel, toLabel, fromValue):
        """
        Converts volume from one unit into another
        
        :param fromLabel: string  
        :param toLabel: string 
        :param fromValue: float 
        :return: float 
        """
        if fromLabel == "Milliliter":
            fromValue = fromValue * (10**(-6))
        if fromLabel == "Cubic Centimeter":
            fromValue = fromValue * (10 ** (-6))
        if fromLabel == "Liter":
            fromValue = fromValue* 0.001
        if fromLabel == "Cubic Meter":
            fromValue = fromValue
        if fromLabel == "Teaspoon(USA)":
            fromValue = fromValue * 5* (10**(-6))
        if fromLabel == "Tablespoon(USA)":
            fromValue = fromValue * 15 * (10**(-6))
        if fromLabel == "Fluid Ounce(USA)":
            fromValue = fromValue * 3* (10**(-5))
        if fromLabel == "Jigger(USA)":
            fromValue = fromValue * 237* (10**(-6))
        if fromLabel == "Pint(USA)":
            fromValue = fromValue * 473* (10**(-6))
        if fromLabel == "Quart(USA)":
            fromValue = fromValue* 946 * (10**(-6))
        if fromLabel == "Gallon(USA)":
            fromValue = fromValue*3785*(10**(-6))
        if fromLabel == "Cubic Inch":
            fromValue = fromValue*16* (10**(-6))
        if fromLabel == "Cubic Foot":
            fromValue = fromValue*28317* (10**(-6))
        if fromLabel == "Cubic Yard":
            fromValue = fromValue*764555* (10**(-6))
        if fromLabel ==  "Teaspoon(GB)":
            fromValue = fromValue*6*(10**(-6))
        if fromLabel == "Tablespoon(GB)":
            fromValue = fromValue*18*(10**(-6))
        if fromLabel == "Fluid Ounce(GB)":
            fromValue = fromValue*28*(10**(-6))
        if fromLabel == "Pint(GB)":
            fromValue = fromValue*568*(10**(-6))
        if fromLabel == "Quart(GB)":
            fromValue = fromValue*1137*(10**(-6))
        if fromLabel == "Gallon(GB)":
            fromValue = fromValue*4546*(10**(-6))



        if toLabel == "Milliliter":
            fromValue = fromValue / (10**(-6))
        if toLabel == "Cubic Centimeter":
            fromValue = fromValue / (10 ** (-6))
        if toLabel == "Liter":
            fromValue = fromValue / 0.001
        if toLabel == "Cubic Meter":
            fromValue = fromValue
        if toLabel == "Teaspoon(USA)":
            fromValue = fromValue / (5* (10**(-6)))
        if toLabel == "Tablespoon(USA)":
            fromValue = fromValue / (15 * (10**(-6)))
        if toLabel == "Fluid Ounce(USA)":
            fromValue = fromValue / (3* (10**(-5)))
        if toLabel == "Jigger(USA)":
            fromValue = fromValue / (237* (10**(-6)))
        if toLabel == "Pint(USA)":
            fromValue = fromValue / (473* (10**(-6)))
        if toLabel == "Quart(USA)":
            fromValue = fromValue/  (946 * (10**(-6)))
        if toLabel == "Gallon(USA)":
            fromValue = fromValue / (3785*(10**(-6)))
        if toLabel == "Cubic Inch":
            fromValue = fromValue/ (16* (10**(-6)))
        if toLabel == "Cubic Foot":
            fromValue = fromValue / (28317* (10**(-6)))
        if toLabel == "Cubic Yard":
            fromValue = fromValue/ (764555* (10**(-6)))
        if toLabel ==  "Teaspoon(GB)":
            fromValue = fromValue/ (6*(10**(-6)))
        if toLabel == "Tablespoon(GB)":
            fromValue = fromValue/ (18*(10**(-6)))
        if toLabel == "Fluid Ounce(GB)":
            fromValue = fromValue/ (28*(10**(-6)))
        if toLabel == "Pint(GB)":
            fromValue = fromValue/ (568*(10**(-6)))
        if toLabel == "Quart(GB)":
            fromValue = fromValue/ (1137*(10**(-6)))
        if toLabel == "Gallon(GB)":
            fromValue = fromValue /(4546*(10**(-6)))

        return fromValue


    @pyqtSlot()
    def onBtnResetClicked(self):
        """
        Slot for signal-slot handling .
        Gets invoked when btnReset is clicked.
        
        :return: 
        """
        self.comboCategoryChooser.setCurrentIndex(0)
        self.editFrom.setText("")
        self.editTo.setText("")


    def generate_units(self):
        """
        Generates map of different category-units , and each category has its 
        own list of units. 
        
        :return: map of list of string 
        """
        volumes = ["Milliliter", "Cubic Centimeter", "Liter", "Cubic Meter",
                   "Teaspoon(USA)", "Tablespoon(USA)", "Fluid Ounce(USA)",
                   "Jigger(USA)", "Pint(USA)", "Quart(USA)", "Gallon(USA)",
                   "Cubic Inch", "Cubic Foot", "Cubic Yard",
                   "Teaspoon(GB)", "Tablespoon(GB)", "Fluid Ounce(GB)",
                   "Pint(GB)", "Quart(GB)", "Gallon(GB)"]

        distances = ["Nanometer", "Micrometer", "Millimeter", "Centimeter",
                     "Meter", "Kilometer", "Inch", "Foot", "Yard", "Mile", "Seemile"]

        weights = ["Carat", "Milligram", "Centigram", "Decigram", "Gram", "Decagram",
                   "Hectogram", "Kilogram", "Ton", "Ounce", "Pound", "Stone"]

        temperatures = ["Celcius", "Fahrenheit", "Kelvin"]

        areas = ["Square Millimeter", "Square Centimeter", "Square Meter",
                 "Hectar", "Square Kilometer", "Square Inch", "Square Foot",
                 "Square Yard", "Acre", "Square Mile"]

        times = ["Microsecond", "Millisecond", "Second", "Minute",
                 "Hour", "Day", "Week", "Year"]

        units = {
            "Volumes": volumes,
            "Distances": distances,
            "Weights": weights ,
            "Temperatures": temperatures,
            "Areas": areas ,
            "Times": times

        }

        return units


