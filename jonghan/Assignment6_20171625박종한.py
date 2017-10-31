import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel,
    QComboBox, QTextEdit, QLineEdit, QMessageBox, QGridLayout)
from PyQt5.QtCore import*

import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel,
    QComboBox, QTextEdit, QLineEdit, QMessageBox, QGridLayout)
from PyQt5.QtCore import*


class ScoreDB(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB()


    def initUI(self):

        self.setGeometry(300, 300, 600, 250)
        self.setWindowTitle('Assignment6')
        #name = QLineEdit("Name")

        layout = QHBoxLayout()
        layout2 = QVBoxLayout()
        layout.addStretch(1)
        layout.addWidget(QPushButton("Add", self))
        layout.addWidget(QPushButton("Del", self))
        layout.addWidget(QPushButton("Find", self))
        layout.addWidget(QPushButton('Inc', self))
        layout.addWidget(QPushButton('Show', self))

        layout2.addStretch(1)
        layout2.addWidget(QLabel("Name", self))
        layout2.addWidget(QLineEdit("", self))

        self.setLayout(layout)

        #btn1.clicked.connect(QCoreApplication.instance().quit)
        self.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'EXIT', 'Are you sure to quit?',
                                     QMessageBox.YES | QMessageBox.no,
                                     QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return

        try:
            self.scoredb =  pickle.load(fH)
        except:
            pass
        else:
            pass
        fH.close()


    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    def showScoreDB(self):
        pass

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())






class ScoreDB(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB()


    def initUI(self):

        self.setGeometry(300, 300, 600, 250)
        self.setWindowTitle('Assignment6')
        #name = QLineEdit("Name")

        layout = QHBoxLayout()
        layout2 = QVBoxLayout()
        layout.addStretch(1)
        layout.addWidget(QPushButton("Add", self))
        layout.addWidget(QPushButton("Del", self))
        layout.addWidget(QPushButton("Find", self))
        layout.addWidget(QPushButton('Inc', self))
        layout.addWidget(QPushButton('Show', self))

        layout2.addStretch(1)
        layout2.addWidget(QLabel("Name", self))
        layout2.addWidget(QLineEdit("", self))

        self.setLayout(layout)

        #btn1.clicked.connect(QCoreApplication.instance().quit)
        self.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'EXIT', 'Are you sure to quit?',
                                     QMessageBox.YES | QMessageBox.no,
                                     QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return

        try:
            self.scoredb =  pickle.load(fH)
        except:
            pass
        else:
            pass
        fH.close()


    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    def showScoreDB(self):
        pass

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())





