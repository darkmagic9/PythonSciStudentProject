import sys
from PyQt5.QtWidgets import QApplication , QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, QItemSelectionModel
from PyQt5.QtWidgets import QHBoxLayout, QGroupBox , QDialog, QVBoxLayout, QGridLayout
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

from dao.OperatorDAOPymysqlImpl import OperatorDAOPymysqlImpl
from model.Operator import Operator
from mapper.OperatorListMapper import OperatorListMapper
from gui.OperatorSaveWindow import OperatorSaveWindow
from gui.OperatorUpdateWindow import OperatorUpdateWindow
from gui.OperatorDetailsWindow import OperatorDetailsWindow

from serializer.OperatorXMLSerializer import OperatorXMLSerializer
from serializer.OperatorJSONSerializer import OperatorJSONSerializer
from serializer.OperatorCSVSerializer import OperatorCSVSerializer
from serializer.OperatorPDFSerializer import OperatorPDFSerializer

from others.SimpleCalculator import SimpleCalculator
from others.SimpleConverter import SimpleConverter
from others.MatplotIntegrationExample import MatplotIntegrationExample
from others.SimpleTictactoe import SimpleTictactoe

class OperatorFindAllWindow(QDialog):
    """
    After successful login by user this window is shown. 

    """
    def __init__(self):
        """
        constructor 
        
        """
        super().__init__()
        self.title = "All Operators"
        self.left , self.top, self.width , self.height = 50 , 50, 900, 500
        self.dao = OperatorDAOPymysqlImpl()
        self.mapper = OperatorListMapper()
        self.initGUI()


    def initGUI(self):
        """
        initializes GUI
        :return: 
        """
        self.setWindowTitle(self.title)
        self.setGeometry(self.left , self.top, self.width, self.height)
        # self.setWindowModality(Qt.WindowModal)
        self.addComponents()
        self.registerEvents()




    def populateTable(self):
        """
        adds QTableWidgetItem-s into QTableWidget instance(self.tableWidget)
        :return: 
        """
        data = self.dao.find_all()
        self.tableWidget.setRowCount(len(data))
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setColumnCount(13)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        for i, operator in enumerate(data):
            # print(type(operator))
            l = self.mapper.map_to_list(operator)
            self.tableWidget.setItem(i, 0, QTableWidgetItem(l[0]))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(l[1]))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(l[2]))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(l[3]))
            self.tableWidget.setItem(i, 4, QTableWidgetItem(l[4]))
            self.tableWidget.setItem(i, 5, QTableWidgetItem(l[5]))
            self.tableWidget.setItem(i, 6, QTableWidgetItem(l[6]))
            self.tableWidget.setItem(i, 7, QTableWidgetItem(l[7]))
            self.tableWidget.setItem(i, 8, QTableWidgetItem(l[8]))
            self.tableWidget.setItem(i, 9, QTableWidgetItem(l[9]))
            self.tableWidget.setItem(i, 10, QTableWidgetItem(l[10]))
            self.tableWidget.setItem(i, 11, QTableWidgetItem(l[11]))
            self.tableWidget.setItem(i, 12, QTableWidgetItem(l[12]))

        self.tableWidget.setHorizontalHeaderLabels(["id", "create_date", "create_time", "create_userfullname",
                                                    "create_userid", "update_date", "update_time", "update_userfullname",
                                                    "update_userid", "emp_id", "emp_name", "is_validator", "remark"])
        # self.tableWidget.resizeColumnsToContents()


    def addComponents(self):
        """
        sets the mainLayout for this class and adds components into it.
        :return: 
        """

        # layout
        # self.mainWidget = QWidget()
        self.mainLayout = QVBoxLayout()
        # self.mainWidget.setLayout(self.mainLayout)
        # self.mainWidget.setGeometry(self.left, self.top, self.width, self.height)
        self.setLayout(self.mainLayout)
        
        self.mainMenu = QMenuBar(self)
        self.mainLayout.addWidget(self.mainMenu)
        
        self.menuActions = self.mainMenu.addMenu("Actions")
        # actions
        self.actionSave = QAction("Add New Operator...", self)
        self.menuActions.addAction(self.actionSave)
        self.actionUpdate = QAction("Update the Selected Operator...", self)
        self.menuActions.addAction(self.actionUpdate)
        self.actionRemove = QAction("Remove the Selected Operator", self)
        self.menuActions.addAction(self.actionRemove)
        self.actionDetails = QAction("Details of the Selected Operator...", self)
        self.menuActions.addAction(self.actionDetails)

        # serializers
        self.menuSerializers = self.mainMenu.addMenu("Serializers")

        self.actionExportAsXML = QAction("Export As XML...", self)
        self.actionExportAsJSON = QAction("Export As JSON...", self)
        self.actionExportAsCSV = QAction("Export As CSV...", self)
        self.actionExportAsPDF = QAction("Export As PDF...", self)

        self.actionImportFromXML = QAction("Import From XML...", self)
        self.actionImportFromJSON = QAction("Import From JSON...", self)
        self.actionImportFromCSV = QAction("Import From CSV...", self)

        self.menuSerializers.addAction(self.actionExportAsXML)
        self.menuSerializers.addAction(self.actionExportAsJSON)
        self.menuSerializers.addAction(self.actionExportAsCSV)
        self.menuSerializers.addAction(self.actionExportAsPDF)

        self.menuSerializers.addAction(self.actionImportFromXML)
        self.menuSerializers.addAction(self.actionImportFromJSON)
        self.menuSerializers.addAction(self.actionImportFromCSV)

        # others
        self.menuOthers = self.mainMenu.addMenu("Others")

        self.actionSimpleCalculator = QAction("Open SimpleCalculator...", self)
        self.actionSimpleConverter = QAction("Open SimpleConverter...", self)
        self.actionMatplotIntegrationExample = QAction("Matplot Integration Example...", self)
        self.actionSimpleTictactoe = QAction("Open SimpleTictactoe...", self)

        self.menuOthers.addAction(self.actionSimpleCalculator)
        self.menuOthers.addAction(self.actionSimpleConverter)
        self.menuOthers.addAction(self.actionMatplotIntegrationExample)
        self.menuOthers.addAction(self.actionSimpleTictactoe)

        # table widget
        self.tableWidget = QTableWidget()

        self.mainLayout.addWidget(self.tableWidget)

        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)

        self.populateTable()
        self.tableWidget.resizeColumnsToContents()


        # self.tableWidget.setSelectionModel(QItemSelectionModel.Rows)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)



        # Sync button
        self.btnSync = QPushButton("Synchronize table content with database.")
        self.mainLayout.addWidget(self.btnSync)



    def registerEvents(self):
        """
        registers events
        :return: 
        """
        self.actionSave.triggered.connect(self.onActionSaveTriggered)
        self.actionUpdate.triggered.connect(self.onActionUpdateTriggered)
        self.actionRemove.triggered.connect(self.onActionRemoveTriggered)
        self.actionDetails.triggered.connect(self.onActionDetailsTriggered)
        self.btnSync.clicked.connect(self.onBtnSyncClicked)
        self.actionExportAsXML.triggered.connect(self.onActionExportAsXMLTriggered)
        self.actionExportAsJSON.triggered.connect(self.onActionExportAsJSONTriggered)
        self.actionExportAsCSV.triggered.connect(self.onActionExportAsCSVTriggered)
        self.actionExportAsPDF.triggered.connect(self.onActionExportAsPDFTriggered)
        self.actionImportFromXML.triggered.connect(self.onActionImportFromXMLTriggered)
        self.actionImportFromJSON.triggered.connect(self.onActionImportFromJSONTriggered)
        self.actionImportFromCSV.triggered.connect(self.onActionImportFromCSVTriggered)

        self.actionSimpleCalculator.triggered.connect(self.onActionSimpleCalculatorTriggered)
        self.actionSimpleConverter.triggered.connect(self.onActionSimpleConverterTriggered)
        self.actionMatplotIntegrationExample.triggered.connect(self.onActionMatplotIntegrationExampleTriggered)
        self.actionSimpleTictactoe.triggered.connect(self.onActionSimpleTictactoeTriggered)


    @pyqtSlot()
    def onActionSaveTriggered(self):
        """
        Slot for signal-slot handling .
        Gets invoked when actionSave is triggered.
        :return: 
        """
        window = OperatorSaveWindow(self.tableWidget)
        window.show()
        window.exec_()
        # self.tableWidget.resizeColumnsToContents()
        self.populateTable()

    @pyqtSlot()
    def onActionUpdateTriggered(self):
        """
        Slot for signal-slot handling .
        Gets invoked when actionUpdate is triggered.
        :return: 
        """
        selectedItems = self.tableWidget.selectedItems()
        if len(selectedItems)  == 0:
            QMessageBox.critical(self, "<<Error>>", "No row was selected.")
            return

        # data = [selectedItem.text() for selectedItem in selectedItems]
        # selectedItems[1].setText("updated firstname")

        # print(data)
        window = OperatorUpdateWindow(selectedItems)
        window.show()
        window.exec_()
        # self.tableWidget.resizeColumnsToContents()
        self.populateTable()


    @pyqtSlot()
    def onActionRemoveTriggered(self):
        """
        Slot for signal-slot handling .
        Gets invoked when actionRemove is triggered.
        :return: 
        """
        selectedItems = self.tableWidget.selectedItems()
        if len(selectedItems) == 0:
            QMessageBox.critical(self, "<<Error>>", "No row was selected.")
            return
        selectedRow = self.tableWidget.selectedIndexes()[0].row()
        data = [selectedItem.text() for selectedItem in selectedItems]
        self.tableWidget.removeRow(selectedRow)
        self.dao.remove(data[0])



    @pyqtSlot()
    def onActionDetailsTriggered(self):
        """
        Slot for signal-slot handling .
        Gets invoked when actionDetails is triggered.
        :return: 
        """
        selectedItems = self.tableWidget.selectedItems()
        if len(selectedItems) == 0:
            QMessageBox.critical(self, "<<Error>>", "No row was selected.")
            return

        data = [selectedItem.text() for selectedItem in selectedItems]
        window = OperatorDetailsWindow(data)
        window.show()
        window.exec_()



    @pyqtSlot()
    def onBtnSyncClicked(self):
        """
        Slot for signal-slot handling .
        Gets invoked when btnSync is clicked.
        :return: 
        """
        rowCount = self.tableWidget.rowCount()
        while(rowCount > 0):
            self.tableWidget.removeRow(rowCount-1)
            rowCount = self.tableWidget.rowCount()


        self.populateTable()




    def saveFileDialog(self, title, directory = "files" , fileType = "Text", fileExtension="txt"):
        """
        opens Save-Dialog for saving file 
        
        :param title: string 
        :param directory: string 
        :param fileType: string 
        :param fileExtension: string
        :return: 
        """
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self, title, directory,
                                                  "{0} Files (*.{1})".format(fileType, fileExtension), options=options)
        if fileName:
            return fileName

        return None



    @pyqtSlot()
    def onActionExportAsXMLTriggered(self):
        """
        Slot for signal-slot handling .
        Gets invoked when actionExportAsXML is triggered.
        :return: 
        """
        fileName = self.saveFileDialog("Export As XML" , fileType="XML", fileExtension="xml")
        if fileName:
            try:
                serializer = OperatorXMLSerializer()
                operator = self.dao.find_all()
                serializer.exportAsXMLToFile(operator, fileName+'.xml')
                QMessageBox.information(self, "<<Information>>", "Exported As XML successfully.")

            except Exception as err:
                QMessageBox.critical(self, "<<Error>>", str(err))


        else:
            QMessageBox.critical(self, "<<Error>>", "No fileName was given.")




    @pyqtSlot()
    def onActionExportAsJSONTriggered(self):
        """
        Slot for signal-slot handling .
        Gets invoked when actionExportAsJSON is triggered.
        :return: 
        """
        fileName = self.saveFileDialog("Export As JSON" , fileType="JSON", fileExtension="json")
        if fileName:
            try:
                serializer = OperatorJSONSerializer()
                operator = self.dao.find_all()
                serializer.exportAsJSONToFile(operator, fileName+'.json')
                QMessageBox.information(self, "<<Information>>", "Exported As JSON successfully.")

            except Exception as err:
                QMessageBox.critical(self, "<<Error>>", str(err))


        else:
            QMessageBox.critical(self, "<<Error>>", "No fileName was given.")

    @pyqtSlot()
    def onActionExportAsCSVTriggered(self):
        """
        Slot for signal-slot handling .
        Gets invoked when actionExportAsCSV is triggered.
        :return: 
        """
        fileName = self.saveFileDialog("Export As CSV", fileType="CSV", fileExtension="csv")
        if fileName:
            try:
                serializer = OperatorCSVSerializer()
                operator = self.dao.find_all()
                serializer.exportAsCSVToFile(operator, fileName+'.csv')
                QMessageBox.information(self, "<<Information>>", "Exported As CSV successfully.")

            except Exception as err:
                QMessageBox.critical(self, "<<Error>>", str(err))


        else:
            QMessageBox.critical(self, "<<Error>>", "No fileName was given.")



    @pyqtSlot()
    def onActionExportAsPDFTriggered(self):
        """
        Slot for signal-slot handling .
        Gets invoked when actionExportAsPDF is triggered.
        :return: 
        """
        fileName = self.saveFileDialog("Export As PDF", fileType="PDF", fileExtension="pdf")
        if fileName:
            try:
                serializer = OperatorPDFSerializer()
                operator = self.dao.find_all()
                serializer.exportAsPDFToFile(operator, fileName+'.pdf')
                QMessageBox.information(self, "<<Information>>", "Exported As PDF successfully.")

            except Exception as err:
                QMessageBox.critical(self, "<<Error>>", str(err))


        else:
            QMessageBox.critical(self, "<<Error>>", "No fileName was given.")




    def openFileDialog(self, title, directory = "files", fileType = "Text", fileExtension = "txt"):
        """
        opens Open-Dialog for choosing a file
        
        :param title: string 
        :param directory: string 
        :param fileType: string 
        :param fileExtension: string 
        :return: 
        """
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,title,directory,"{0} Files (*.{1})".format(fileType, fileExtension),
                                                  options=options)
        if fileName:
            return fileName
        else:
            return None


    def generateWindowWithTableWidget(self, operator, title ):
        """
        generates and show QDialog instance with QTableWidget, which contains 
        operator as its rows
        
        :param operator: list of model.Operator.Operator - s
        :param title: string 
        :return: 
        """
        mainWidget = QDialog()
        mainWidget.setWindowTitle(title)
        mainWidget.setGeometry(50, 50, 800, 500)
        mainWidget.setWindowModality(Qt.WindowModal)
        # set layout
        mainLayout = QVBoxLayout()
        mainWidget.setLayout(mainLayout)
        # add components
        # title
        lblTitle = QLabel(title)
        mainLayout.addWidget(lblTitle)
        # table widget
        tableOperators = QTableWidget()
        tableOperators.setRowCount(len(operator))
        tableOperators.setAlternatingRowColors(True)
        tableOperators.setColumnCount(13)
        tableOperators.horizontalHeader().setCascadingSectionResizes(False)
        tableOperators.horizontalHeader().setSortIndicatorShown(False)
        tableOperators.horizontalHeader().setStretchLastSection(True)
        tableOperators.verticalHeader().setVisible(False)
        tableOperators.verticalHeader().setCascadingSectionResizes(False)
        tableOperators.verticalHeader().setStretchLastSection(False)


        for i, operator in enumerate(operator):
            # print(type(operator))
            l = self.mapper.map_to_list(operator)
            tableOperators.setItem(i, 0, QTableWidgetItem(l[0]))
            tableOperators.setItem(i, 1, QTableWidgetItem(l[1]))
            tableOperators.setItem(i, 2, QTableWidgetItem(l[2]))
            tableOperators.setItem(i, 3, QTableWidgetItem(l[3]))
            tableOperators.setItem(i, 4, QTableWidgetItem(l[4]))
            tableOperators.setItem(i, 5, QTableWidgetItem(l[5]))
            tableOperators.setItem(i, 6, QTableWidgetItem(l[6]))
            tableOperators.setItem(i, 7, QTableWidgetItem(l[7]))
            tableOperators.setItem(i, 8, QTableWidgetItem(l[8]))
            tableOperators.setItem(i, 9, QTableWidgetItem(l[9]))
            tableOperators.setItem(i, 10, QTableWidgetItem(l[10]))
            tableOperators.setItem(i, 11, QTableWidgetItem(l[11]))
            tableOperators.setItem(i, 12, QTableWidgetItem(l[12]))



        tableOperators.setHorizontalHeaderLabels(["id", "create_date", "create_time", "create_userfullname",
                                                    "create_userid", "update_date", "update_time", "update_userfullname",
                                                    "update_userid", "emp_id", "emp_name", "is_validator", "remark"])
        tableOperators.resizeColumnsToContents()

        mainLayout.addWidget(tableOperators)
        mainWidget.show()
        mainWidget.exec_()



    @pyqtSlot()
    def onActionImportFromXMLTriggered(self):
        """
        Slot for signal-slot handling .
        Gets invoked when actionImportFromXML is triggered.
        :return: 
        """
        fileName = self.openFileDialog("Import From XML", fileType="XML", fileExtension="xml")
        if fileName:
            serializer = OperatorXMLSerializer()
            operator = serializer.importFromXML(fileName)
            # print(operator)
            self.generateWindowWithTableWidget(operator, "Import From XML")
        else:
            QMessageBox.critical(self, "<<Error>>", "No fileName was given.")

    @pyqtSlot()
    def onActionImportFromJSONTriggered(self):
        """
        Slot for signal-slot handling .
        Gets invoked when actionImportFromJSON is triggered.
        :return: 
        """
        fileName = self.openFileDialog("Import From JSON", fileType="JSON", fileExtension="json")
        if fileName:
            serializer = OperatorJSONSerializer()
            operator = serializer.importFromJSON(fileName)
            # print(operator)
            self.generateWindowWithTableWidget(operator, "Import From JSON")
        else:
            QMessageBox.critical(self, "<<Error>>", "No fileName was given.")

    @pyqtSlot()
    def onActionImportFromCSVTriggered(self):
        fileName = self.openFileDialog("Import From CSV", fileType="CSV", fileExtension="csv")
        if fileName:
            serializer = OperatorCSVSerializer()
            operator = serializer.importFromCSV(fileName)
            # print(operator)
            self.generateWindowWithTableWidget(operator, "Import From CSV")
        else:
            QMessageBox.critical(self, "<<Error>>", "No fileName was given.")


    @pyqtSlot()
    def onActionSimpleCalculatorTriggered(self):
        """
        Slot for signal-slot handling .
        Gets invoked when actionSimpleCalculator is triggered.
        :return: 
        """
        simpleCalculator = SimpleCalculator()
        simpleCalculator.show()
        simpleCalculator.exec_()

    @pyqtSlot()
    def onActionSimpleConverterTriggered(self):
        """
        Slot for signal-slot handling .
        Gets invoked when actionSimpleConverter is triggered.
        :return: 
        """
        simpleConverter = SimpleConverter()
        simpleConverter.show()
        simpleConverter.exec_()


    @pyqtSlot()
    def onActionMatplotIntegrationExampleTriggered(self):
        """
        Slot for signal-slot handling .
        Gets invoked when actionMatplotIntegrationExample is triggered.
        :return: 
        """
        integration = MatplotIntegrationExample()
        integration.show()
        integration.exec_()


    @pyqtSlot()
    def onActionSimpleTictactoeTriggered(self):
        """
        Slot for signal-slot handling .
        Gets invoked when actionSimpleTictactoe is triggered.
        :return: 
        """
        tictactoe = SimpleTictactoe()
        tictactoe.show()
        tictactoe.exec_()






