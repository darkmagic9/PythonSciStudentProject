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
import matplotlib.cbook as cbook

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
        self.addComponents()
        self.registerEvents()


    def addComponents(self):
        # mainLayout
        self.mainLayout = QVBoxLayout()
        self.setLayout(self.mainLayout)

        # title
        self.lblTitle = QLabel("PyQT5 Matplot Integration Example")
        self.mainLayout.addWidget(self.lblTitle)

        # canvas
        self.canvas = PlotCanvas(self, width=5, height=4)
        self.mainLayout.addWidget(self.canvas)

        # widgetControllers and layoutControllers
        self.widgetControllers = QWidget()
        self.layoutControllers = QGridLayout()
        self.widgetControllers.setLayout(self.layoutControllers)
        self.mainLayout.addWidget(self.widgetControllers)

        self.btnLinePlot = QPushButton("Line Plot")
        self.layoutControllers.addWidget(self.btnLinePlot, 0, 0)

        self.btnScatterPlot = QPushButton("Scatter Plot")
        self.layoutControllers.addWidget(self.btnScatterPlot, 0, 1)

        self.btnBarPlot = QPushButton("Bar Plot")
        self.layoutControllers.addWidget(self.btnBarPlot, 1, 0)


        self.btnPieChartPlot = QPushButton("Pie Chart Plot")
        self.layoutControllers.addWidget(self.btnPieChartPlot, 1, 1)



    def registerEvents(self):
        self.btnLinePlot.clicked.connect(self.onBtnLinePlotClicked)
        self.btnScatterPlot.clicked.connect(self.onBtnScatterPlotClicked)
        self.btnBarPlot.clicked.connect(self.onBtnBarPlotClicked)
        self.btnPieChartPlot.clicked.connect(self.onBtnPieChartPlotClicked)

    @pyqtSlot()
    def onBtnLinePlotClicked(self):
        self.canvas.linePlot()

    @pyqtSlot()
    def onBtnScatterPlotClicked(self):
        self.canvas.scatterPlot()

    @pyqtSlot()
    def onBtnBarPlotClicked(self):
        self.canvas.barPlot()

    @pyqtSlot()
    def onBtnPieChartPlotClicked(self):
        self.canvas.pieChartPlot()


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
        self.linePlot()

    def linePlot(self):
        """
        plots matplot line
        :return: 
        """
        self.axes.cla()
        ax = self.figure.add_subplot(111)
        ax.axis("on")
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.spines['left'].set_visible(False)

        # ax.patch.set_visible(False)
        x = np.linspace(-np.pi, np.pi, 100)
        y_sin, y_cos = np.sin(x), np.cos(x)

        ax.plot(x, y_sin, x, y_cos)
        ax.set_title("Line Plot example")
        self.draw()

    def scatterPlot(self):
        """
        plots matplot scatter chart 
        :return: 
        """
        self.axes.cla()
        ax = self.figure.add_subplot(111)
        ax.axis("on")
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.spines['left'].set_visible(False)

        # get random coordinates for 50 points
        N = 50
        x = np.random.rand(N)
        y = np.random.rand(N)
        # get random colors to use for these points
        colors = np.random.rand(N)
        # get random areas of each point (displayed as a shaded circle). Area is given by pi*r^2
        area = np.pi * (15 * np.random.rand(N)) ** 2  # 0 to 15 point radiuses
        # plot all the points scattered across the figure
        ax.scatter(x, y, s=area, c=colors, marker='o')
        ax.set_title("Scatter Plot example")
        self.draw()


    def barPlot(self):
        """
        plots matplot bar chart
        :return: 
        """
        self.axes.cla()
        ax = self.figure.add_subplot(111)
        ax.axis("on")
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.spines['left'].set_visible(False)

        # setup some statistical data
        N = 5
        group1Means = (20, 35, 30, 35, 27)
        group1Std = (2, 3, 4, 1, 2)

        group2Means = (25, 32, 34, 20, 25)
        group2Std = (3, 5, 2, 3, 3)

        # the x locations for the bars
        ind = np.arange(N)

        # the width of the bars
        width = 0.35

        # plot first group
        ax.bar(ind, group1Means, width, color='r', yerr=group1Std)

        # plot second group
        ax.bar(ind + width, group2Means, width, color='y', yerr=group2Std)

        # add some text for labels, title and axes ticks
        ax.set_ylabel('Scores')
        ax.set_title('Scores by group and types')
        ax.set_xticks(ind + width, ('T1', 'T2', 'T3', 'T4', 'T5'))

        # display plot legend
        ax.legend(('Group1', 'Group2'))
        self.draw()


    def pieChartPlot(self):
        """
        plots matplot pie chart
        :return: 
        """
        self.axes.cla()
        ax = self.figure.add_subplot(111)
        ax.axis("on")

        labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
        sizes = [15, 30, 45, 10]
        explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

        # fig1, ax1 = plt.subplots()
        ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        # ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        ax.set_title("Pie Chart Example")
        self.draw()


# app = QApplication(sys.argv)
# window = MatplotIntegrationExample()
# window.show()
# sys.exit(app.exec_())



