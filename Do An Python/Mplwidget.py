from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from Custom_Widgets.Widgets import *
from PySide2 import QtCore, QtGui, QtWidgets
import ui_interface_2

class MplWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Create the Figure and FigureCanvas
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)

        # Set up the layout
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)