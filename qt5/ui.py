from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        xpos = 100
        ypos = 50
        width = 800
        height = 600
        self.setGeometry(xpos, ypos, width, height)
        self.setWindowTitle("My Title")
        self.initUi()

    def initUi(self):
        self.mylabel = QtWidgets.QLabel(self)
        self.mylabel.setText("My Label")
        self.mylabel.move(50, 50)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("My button")
        self.b1.move(10, 10)
        self.b1.clicked.connect(self.clicked)

    def clicked(self):
        self.mylabel.setText(f"My button is Pressed")
        self.update()

    def update(self):
        self.mylabel.adjustSize()
        
