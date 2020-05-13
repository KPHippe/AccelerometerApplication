#This was written by Kyle, Sola, Adam, Spenser

import sys
import json
import socket
import random
import threading
import numpy as np
import matplotlib as plt
from PyQt5 import QtCore, QtWidgets
from matplotlib.figure import Figure
from PyQt5.QtWidgets import QHBoxLayout
from multiprocessing import Process, Pipe
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

plt.use('Qt5Agg')
# GLOBAL_X = [0] * 50
# GLOBAL_Y = [0] * 50
# GLOBAL_Z = [0] * 50
        
def recData(pipe_connection):
    #Change this address to the IP address of the computer that is running the server
    RPIADDR= '10.0.0.112'
    LOCAL = '127.0.0.1'
    #creates a TCP socket, we might end up using TCP, but we will see about the future
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #Using the socket object we created, connect to the server IP at the given port number
    s.connect((RPIADDR,9999))


    while True:
        recMessage = s.recv(256).decode("utf-8")

        #if we actually received something from the server, print it out and continue
        if(len(recMessage) > 0):
            recMessage = recMessage.split()
            x = int(recMessage[0])
            y = int(recMessage[1])
            z = int(recMessage[2])

            #Send the messages through the pipe to the parent process
            pipe_connection.send(f"{x}\n{y}\n{z}")
        #Else, something went wrong
        #TCP creates a 'tunnell' so if you don't get anything back that means your connection failed
        #if it does fail, you have to close everything and restart
        else:
            print(f"Error receiving, closing")
            sys.exit()

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, pipe, *args, **kwargs):
        # global GLOBAL_X, GLOBAL_Y, GLOBAL_Z
        super(MainWindow, self).__init__(*args, **kwargs)
        self.pipe = pipe
        self.canvas = MplCanvas(self, width=20, height=20, dpi=100)
        self.setCentralWidget(self.canvas)

        n_data = 50
        self.xdata = list(range(n_data))

        self.ydata = [0] * 50
        self.ydata2 = [0] * 50
        self.ydata3 = [0] * 50


        self.update_plot()
        self.show()

    def update_plot(self):
        x, y, z = self.pipe.recv().split()
        # Setup a timer to trigger the redraw by calling update_plot.
        self.timer = QtCore.QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()# print(f"received '{recMessage}' from server")
        # Drop off the first y element, append a new one.
        self.ydata = self.ydata[1:] + [int(x)]
        self.canvas.axes.cla()  # Clear the canvas.
        self.canvas.axes.set_title("X Axis")
        #self.canvas.axes.set_xlabel("Time")
        self.canvas.axes.set_ylabel("X Acceleration")
        self.canvas.axes.plot(self.xdata, self.ydata)
        # Trigger the canvas to update and redraw.
        # *************
        self.ydata2 = self.ydata2[1:] + [int(y)]
        self.canvas.axes2.cla()  # Clear the canvas.
        self.canvas.axes2.set_title("Y Axis")
        #self.canvas.axes2.set_xlabel("test Time")
        self.canvas.axes2.set_ylabel("Y Acceleration")
        self.canvas.axes2.plot(self.xdata, self.ydata2)
        # ************
        self.ydata3 = self.ydata3[1:] + [int(z)]
        self.canvas.axes3.cla()  # Clear the canvas.
        self.canvas.axes3.set_title("Z Axis")
        self.canvas.axes3.set_xlabel("Time")
        self.canvas.axes3.set_ylabel("Z Acceleration")
        self.canvas.axes3.plot(self.xdata, self.ydata3)
        # ************    
        self.canvas.draw()

class MplCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        fig2 = Figure(figsize=(width, height), dpi=dpi)
        fig3 = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(311)
        self.axes2 = fig.add_subplot(312)
        self.axes3 = fig.add_subplot(313)
        super(MplCanvas, self).__init__(fig)
     



if __name__ == "__main__":
    parent_connection, child_connection = Pipe()
    network_process = Process(target=recData, args=[(child_connection)])
    network_process.start()

    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow(parent_connection)
    app.exec_()

    networkThread.join()
