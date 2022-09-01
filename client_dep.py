from PySide6 import QtCore, QtWidgets, QtGui


class Bemc(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(QtWidgets.QPushButton("Click Me"))


