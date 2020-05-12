import sys
import random
import matplotlib as plt
import numpy as np
plt.use('Qt5Agg')

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QHBoxLayout

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class MplCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        fig2 = Figure(figsize=(width, height), dpi=dpi)
        fig3 = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(311)
        self.axes2 = fig.add_subplot(312)
        self.axes3 = fig.add_subplot(313)
        super(MplCanvas, self).__init__(fig)


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.canvas = MplCanvas(self, width=20, height=20, dpi=100)
        self.setCentralWidget(self.canvas)

        n_data = 50
        self.xdata = list(range(n_data))
        self.ydata = [random.randint(0, 10) for i in range(n_data)]
        self.ydata2 = [random.randint(0, 10) for i in range(n_data)]
        self.ydata3 = [random.randint(0, 10) for i in range(n_data)]
        self.update_plot()

        self.show()

        # Setup a timer to trigger the redraw by calling update_plot.
        self.timer = QtCore.QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()

    def update_plot(self):
        # Drop off the first y element, append a new one.
        self.ydata = self.ydata[1:] + [random.randint(0, 100)]
        self.canvas.axes.cla()  # Clear the canvas.
        self.canvas.axes.set_title("X Axis")
        #self.canvas.axes.set_xlabel("Time")
        self.canvas.axes.set_ylabel("Acceleration")
        self.canvas.axes.plot(self.xdata, self.ydata)
        # Trigger the canvas to update and redraw.
        # *************
        self.ydata2 = self.ydata2[1:] + [random.randint(0, 100)]
        self.canvas.axes2.cla()  # Clear the canvas.
        self.canvas.axes2.set_title("Y Axis")
        #self.canvas.axes2.set_xlabel("test Time")
        self.canvas.axes2.set_ylabel("test Acceleration")
        self.canvas.axes2.plot(self.xdata, self.ydata2)
        # ************
        self.ydata3 = self.ydata3[1:] + [random.randint(0, 100)]
        self.canvas.axes3.cla()  # Clear the canvas.
        self.canvas.axes3.set_title("Z Axis")
        self.canvas.axes3.set_xlabel("Time")
        self.canvas.axes3.set_ylabel("test Acceleration")
        self.canvas.axes3.plot(self.xdata, self.ydata3)
        # ************

        
        self.canvas.draw()


app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
app.exec_()



# from PyQt5.QtWidgets import QApplication, QPushButton
# app = QApplication([])
# app.setStyleSheet("QPushButton { margin: 10ex; }")
# button = QPushButton('Hello World')
# button.show()
# app.exec_()