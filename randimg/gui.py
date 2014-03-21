#!/usr/bin/env python

import sys
import os
from randimg import lib as randlib 
from PyQt4 import QtGui, QtCore

class MainWindow(QtGui.QWidget):
    dir = None

    def __init__(self):
        super(MainWindow, self).__init__()
        self.initControls()

    def initControls(self):
        mainLayout = QtGui.QVBoxLayout(self)
        buttonLayout = QtGui.QHBoxLayout(self)

        setDirButton = QtGui.QPushButton("Set dir...", self)
        getRandButton = QtGui.QPushButton("Get random image", self)
        buttonLayout.addWidget(setDirButton)
        buttonLayout.addWidget(getRandButton)

        self._imageLabel = QtGui.QLabel(self)
        self._imageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self._imagePathBox = QtGui.QLineEdit(self)

        mainLayout.addLayout(buttonLayout)
        mainLayout.addWidget(self._imageLabel)
        mainLayout.addWidget(self._imagePathBox)

        setDirButton.clicked.connect(self.openSetDirDialogue)
        getRandButton.clicked.connect(self.getRandImage)

    def openSetDirDialogue(self):
        self.dir = QtGui.QFileDialog.getExistingDirectory(
                self,
                "Choose directory",
                os.path.expanduser("~"),
                QtGui.QFileDialog.ShowDirsOnly | QtGui.QFileDialog.DontResolveSymlinks)

    def getRandImage(self):
        if(self.dir != None):
            self.setImage(randlib.get(self.dir))

    def setImage(self, path):
        self._imagePathBox.setText(path)
        self._imageLabel.setPixmap(QtGui.QPixmap(path).scaled(self._imageLabel.size(), QtCore.Qt.KeepAspectRatio))
        self._imageLabel.adjustSize()


def main():
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.resize(640, 480)
    window.show()
    sys.exit(app.exec_())

