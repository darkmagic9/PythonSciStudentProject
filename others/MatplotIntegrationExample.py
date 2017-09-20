import sys
from PyQt5.QtWidgets import QApplication , QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, QItemSelectionModel
from PyQt5.QtWidgets import QHBoxLayout, QGroupBox , QDialog, QVBoxLayout, QGridLayout
from PyQt5.QtWidgets import QLabel, QTextEdit
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QFormLayout, QLineEdit, QComboBox

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

import numpy as np

class MatplotIntegrationExample(QDialog):
    """
    With this class integration of matplotlib into pygt5 is shown.
    
    """
    def __init__(self):
        """
        constructor 
        
        """
        super().__init__()
        self.left, self.top, self.width, self.height = 10, 10, 700, 500
        self.title = "matplotlib embedded inside pyqt5 "
        self.initGUI()

    def initGUI(self):
        """
        initializes GUI
        :return: 
        """

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        m = PlotCanvas(self, width=5, height=4)
        m.move(0, 0)

        button = QPushButton("PyQt5 button", self)
        button.setToolTip("Simple Push button")
        button.move(500, 0)
        button.resize(140, 50)

        self.show()


class PlotCanvas(FigureCanvas):
    """
    This class is used by MatplotIntegrationExample ,and here matplot figures are plotted. 
    """
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        """
        constructor 
        
        :param parent: QWidget instance
        :param width: int 
        :param height: int 
        :param dpi: int 
        """
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.plot()

    def plot(self):
        """
        plots matplot figures
        :return: 
        """
        x = np.linspace(-np.pi, np.pi, 100)
        y_sin, y_cos = np.sin(x), np.cos(x)
        ax = self.figure.add_subplot(111)
        ax.plot(x, y_sin, x, y_cos)
        ax.set_title("Matplot with pyqt5")
        self.draw()


